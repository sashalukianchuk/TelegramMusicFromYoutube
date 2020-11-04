import os
import eyed3

from src.youtubeSource import *
from src.utils import *




def prepareTrack(trackPath, trackFileName, trackSign=" "):


    track = trackFileName[:-4].split(" - ")

    if len(track) < 2:
        track = track[0].split(" | ")
        if len(track) < 2:
            title = track[0]
            artist = trackSign
        else:
            artist = track[0]
            title = "".join(track[1:])
    else:
        artist = track[0]
        title = "".join(track[1:])


    audiofile = eyed3.load(trackPath + trackFileName)

    audiofile.tag.artist = artist
    audiofile.tag.title = title
    audiofile.tag.album = trackSign

    audiofile.tag.save()


def channelUpdate(channel, TelegramClientInstance, maxDurationInSeconds=None):
    flag = True
    for youtubeChannelURL in channel.getYouTubeChannelList():

        print("[downloading] channel {0}, to tg {1}".format(youtubeChannelURL, channel.getTelegramChanelID()))

        try:
            downloadLatestFromChannel(youtubeChannelURL, maxDurationInSeconds)
        except DateRangeError:
            pass
        except:
            print("an error occurred while downloading channel {0}".format(youtubeChannelURL))
            flag = False
            continue

        print("Done downloading")

        path = DEFAULT_DOWNLOAD_PATH + getYouTubeChannelIdFromURL(youtubeChannelURL) + "/"

        print("save path: {0}".format(path))

        try:
            files = os.listdir(path)
        except FileNotFoundError:
            print("Directory {} not found, no files downloaded or bad path".format(path))
            continue

        musicFiles = [file for file in files if file.endswith(".mp3")]


        if len(musicFiles) == 0:
            print("empty music list")
            continue


        for i in musicFiles: prepareTrack(path, i, channel.getTrackSign())

        with TelegramClientInstance:
            for musicFile in musicFiles:
                print("uploading {0} to tg chat {1}".format(musicFile, channel.getTelegramChanelID()))

                try:
                    TelegramClientInstance.send_file(channel.getTelegramChanelID(), path + musicFile)
                except Exception as e:
                    print("not uploaded {0}, keep in folder with error: {1}".format(musicFile, e))
                    continue

                print("uploaded {0}, removing...".format(musicFile))
                os.remove(path + musicFile)

        print("Uploaded")
        continue

    return flag



if __name__ == '__main__':
    from src.Channel import Channel

    ch = Channel("./channelConfig/test.json")

    import configparser

    from telethon.sync import TelegramClient

    config = configparser.ConfigParser()
    config.read("Config.ini")

    # Присваиваем значения внутренним переменным
    api_id = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']
    session = config['Telegram']['session']
    client = TelegramClient(session=session, api_id=api_id, api_hash=api_hash)
    client.start()

    channelUpdate(ch, client)


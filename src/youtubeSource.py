# import src.youtube_dl.youtube_dl as youtube_dl
import youtube_dl

from src.utils import *




def downloadLatestFromChannel(chanelURL, maxDurationInSeconds=None, path=DEFAULT_DOWNLOAD_PATH):

    def match_filter(info_dict):

        # duration in seconds

        duration = info_dict.get('duration')
        if duration is not None and maxDurationInSeconds is not None:
            if duration > maxDurationInSeconds:
                return "Skipping {0}, because it has not correct duration {1}/{2}".format(info_dict.get('title'), duration, maxDurationInSeconds)


    channel_id = getYouTubeChannelIdFromURL(chanelURL)

    ydl_opts = {
        'format': 'bestaudio',
        # 'quiet': True,
        'outtmpl': path + channel_id + "/" + "%(title)s.%(ext)s",
        'download_archive': "downloadedLog.log",
        'audio_format': 'mp3',
        'match_filter': match_filter,
        'playlistend': 15,
        # 'progress_hooks': [_finished_hook],  # func who called after download/conversion
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    ydl = youtube_dl.YoutubeDL(ydl_opts)

    ydl.download([chanelURL])




if __name__ == '__main__':
    lastTimeDownloaded = '20000101'


    # def afterDownloadAction(a): pass
    # downloadLatestFromChannel("https://www.youtube.com/channel/UCNZq4pkZa4Wk5mHzMLEgO3g", lastTimeDownloaded, afterDownloadAction)

    downloadLatestFromChannel("https://www.youtube.com/channel/UCNZq4pkZa4Wk5mHzMLEgO3g", 720)
    # downloadLatestFromChannel("https://www.youtube.com/watch?v=Uw2iL6r3NhA", lastTimeDownloaded, 10)
    # ["https://www.youtube.com/channel/UCNZq4pkZa4Wk5mHzMLEgO3g"], "sukanz", '20210801'


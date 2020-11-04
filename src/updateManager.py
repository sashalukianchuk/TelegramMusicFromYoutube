import configparser
from time import sleep
import os

from telethon.sync import TelegramClient

from src.Channel import Channel
from src.channelUpdate import channelUpdate


config = configparser.ConfigParser()
config.read("Config.ini")

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
session = config['Telegram']['session']


if __name__ == '__main__':

    TelegramClientInstance = TelegramClient(session=session, api_id=api_id, api_hash=api_hash)
    TelegramClientInstance.start()

    channelConfigFilesFolder = "./src/channelConfig/"

    channelList = [Channel(channelConfigFilesFolder + config) for config in os.listdir(channelConfigFilesFolder) if
                   config.endswith(".json")]

    while True:
        for channel in channelList:
            channelUpdate(channel, TelegramClientInstance, maxDurationInSeconds=720)
            print("sleep.... 360sec")
            sleep(360)
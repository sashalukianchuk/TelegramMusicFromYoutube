import json


class Channel():


    def __init__(self, filename):

        self.filename = filename
        self.__load()


    def __load(self, ):

        with open(self.filename, 'r') as f:
            configDict = json.load(f)

        if type(configDict['youtubeChannelURLList']) not in (list, tuple):
            raise ValueError('youtubeChannelURLList must be a list or a tuple')

        if 'telegramChannelID' not in configDict:
            raise ValueError('required parapeter telegramChannelID not be configured')
        if 'youtubeChannelURLList' not in configDict:
            raise ValueError('required parapeter youtubeChannelURLList not be configured')
        if 'trackSign' not in configDict:
            raise ValueError('required parapeter telegramChannelName not be configured')

        self._channelConfig = configDict

    def getYouTubeChannelList(self):
        return self._channelConfig['youtubeChannelURLList']

    def getTrackSign(self):
        return self._channelConfig['trackSign']

    def getTelegramChanelID(self):
        return self._channelConfig['telegramChannelID']

    def __repr__(self):
        return self._channelConfig['telegramChannelID'] + '/-/' \
               + str(self._channelConfig['youtubeChannelURLList']) \
               + '/-/' + self._channelConfig['trackSign']


if __name__ == '__main__':
    pass
    a = Channel("./channelConfig/typeBeatParadise.json")
    print(a)
    print(a)
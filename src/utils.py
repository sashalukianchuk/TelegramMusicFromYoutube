class DateRangeError(Exception):
    pass


class Singleton(object):
    __obj = False  # Private class variable.

    def __new__(cls, *args, **kwargs):
        if cls.__obj:
            return cls.__obj
        cls.__obj = super(Singleton, cls).__new__(cls)
        return cls.__obj



def getYouTubeChannelIdFromURL(url):
    return url.split("/")[-1]


DEFAULT_DOWNLOAD_PATH = './tmpTacksFolder/'

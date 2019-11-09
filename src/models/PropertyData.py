from datetime import timedelta

class PropertyData:
    __address = ''
    __name = ''
    __url = ''
    __timeByWalk = timedelta()

    def __init__(
        self,
        name,
        address,
        url
    ):
        self.__name = name
        self.__address = address
        self.__url = url

    def address(self):
        return self.__address

    def name(self):
        return self.__name

    def url(self):
        return self.__url

    def timeByWalk(self):
        return self.__timeByWalk

    def setTimeByWalk(self, time):
        self.__timeByWalk = time

    def toString(self):
        return f"{self.__name}\n{self.__address}\n{self.__url}\n{self.__timeByWalk}\n"

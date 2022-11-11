import configparser
config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURl():
        gurl = config.get("common info","url")
        return gurl

    @staticmethod
    def getusername():
        username1 = config.get("common info","username")
        return username1

    @staticmethod
    def getpassword():
        password1 = config.get("common info","password")
        return password1
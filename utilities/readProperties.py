import configparser
config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURl():
        gurl = config.get("common info","url")
        return gurl

    # @staticmethod
    # def getUrl2():
    #     newurl = config.get("common info","url2")
    #     return newurl

    @staticmethod
    def getusername():
        username1 = config.get("common info","username")
        return username1

    @staticmethod
    def getpassword():
        password1 = config.get("common info","password")
        return password1

#     # @staticmethod
#     # def get_username_in_url():
#     #     url_username = config.get("common info","username_in_url")
#     #     return url_username
#
#     # @staticmethod
#     # def get_password_in_url():
#     #     url_password =config.get("common info","password_in_url")
#     #     return url_password

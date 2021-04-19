import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\Soumya.Mohanty\\Desktop\\python39\\PytestProject\\configurationfolder\\config.ini")#copyrelative path and .\\ means current project location)

class Readconfig:

    @staticmethod
    def geturl():
        url=config.get('common info','baseurl')
        return url

    @staticmethod
    def getusername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password
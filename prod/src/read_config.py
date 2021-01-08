import configparser
import os
class ReadConfig:
    """Read the configuration file"""

    def __init__(self, filepath=None):
        if filepath:
            print("nn")
            configpath = filepath
        else:
            root_dir = os.path.dirname(os.path.abspath('.'))
            configpath = os.path.join(root_dir, "prod","config.ini")
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_db(self, param):
        value = self.cf.get("local-mysql-database", param)
        return value


if __name__ == '__main__':
    test = ReadConfig()
    t = test.get_db("host")
    print(t)


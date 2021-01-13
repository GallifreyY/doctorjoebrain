import configparser
import os
class ReadConfig:
    """Read the configuration file"""

    def __init__(self, filepath=None):
        if filepath:
            print("nn")
            config_file_path = filepath
        else:
            current_path = os.path.dirname(os.path.abspath(__file__))
            father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
            config_file_path = os.path.join(father_path,'config.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(config_file_path)

    def get_db(self, param):
        value = self.cf.get("local-mysql-database", param)
        return value


if __name__ == '__main__':
    test = ReadConfig()
    t = test.get_db("host")
    print(t)


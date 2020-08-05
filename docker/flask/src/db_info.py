from read_config import ReadConfig
data = ReadConfig()
HOSTNAME = data.get_db("HOSTNAME")
PORT = data.get_db("PORT")
DATABASE = data.get_db("DATABASE")
USERNAME = data.get_db("USERNAME")
PASSWORD = data.get_db("PASSWORD")

DB_URI =  'mysql+pymysql://{}:{}@{}:{}/{}' \
          '?charset=utf8mb4'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_POOL_SIZE=20
SQLALCHEMY_POOL_TIMEOUT=300

# mysql+mysqldb://root:04081350@127.0.0.1:3306/DoctorJoe
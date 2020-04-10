# HOSTNAME = '127.0.0.1'
# PORT = '3306'
# DATABASE = 'DoctorJoe'
# USERNAME = 'root'
# PASSWORD = '04081350'

HOSTNAME = '10.117.43.99'
PORT = '3306'
DATABASE = 'doctorjoe'
USERNAME = 'zwx'
PASSWORD = '123456'

DB_URI =  'mysql+pymysql://{}:{}@{}:{}/{}' \
          '?charset=utf8mb4'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# mysql+mysqldb://root:04081350@127.0.0.1:3306/DoctorJoe
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir="./instantclient_19_8") # init Oracle instant client 位置
connection = cx_Oracle.connect('GROUP3', '9bMnh4jMl0', cx_Oracle.makedsn('140.117.69.60', 1521, service_name='ORCLPDB1'))
cursor = connection.cursor()

'''import getpass
import oracledb

connection = oracledb.connect(
    user="GROUP3",
    password='9bMnh4jMl0',
    dsn="140.117.69.60/ORCLPDB1")

print("Successfully connected to Oracle Database")
cursor = connection.cursor()'''
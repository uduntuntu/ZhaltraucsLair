# -*- coding: utf-8
import yaml
import mysql.connector
from mysql.connector import errorcode

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

try:
  cnx = mysql.connector.connect(user=cfg['MariaDB']['user'],
                              password=cfg['MariaDB']['passwd'],
                              host=cfg['MariaDB']['host'],
                              database=cfg['MariaDB']['db'])
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    cnx.close()
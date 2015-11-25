# -*- coding: utf-8 -*-

import yaml
import mysql.connector
from mysql.connector import errorcode

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

TABLES = {}

TABLES['ZL_Room'] = (
    "CREATE TABLE `ZL_Room` ("
    "   `ID` SMALLINT NOT NULL,"
    "   `Description` VARCHAR(2000),"
    "   `State` SMALLINT,"
    "   `PointsModifier` TINYINT,"
    "   PRIMARY KEY (`ID`)"
    ")"
)

TABLES['ZL_RoomState'] = (
    "CREATE TABLE `ZL_RoomState` ("
    "   `ID` SMALLINT NOT NULL,"
    "   `RoomID` SMALLINT NOT NULL,"
    "   `Description` VARCHAR(2000),"
    "   PRIMARY KEY (`ID`,`RoomID`)"
    ")"
)

TABLES['ZL_Player'] = (
    "CREATE TABLE `ZL_Player` ("
    "   `Name` VARCHAR(40) NOT NULL,"
    "   `HP` TINYINT NOT NULL,"
    "   `Class` VARCHAR(25) NOT NULL,"
    "   `RoomID` SMALLINT,"
    "   `Points` INT NOT NULL,"
    "   `Agility` TINYINT NOT NULL,"
    "   `Intelligence` TINYINT NOT NULL,"
    "   `Strength` TINYINT NOT NULL,"
    "   PRIMARY KEY(`Name`)"
    ")"
)

TABLES['ZL_NPC'] = (
    "CREATE TABLE `ZL_NPC` ("
    "   `Name` VARCHAR(40) NOT NULL,"
    "   `ID` SMALLINT NOT NULL,"
    "   `HP` TINYINT NOT NULL,"
    "   `Agility` TINYINT NOT NULL,"
    "   `Strength` TINYINT NOT NULL,"
    "   `RoomID` SMALLINT,"
    "   `PointModifier` TINYINT,"
    "   `Description` VARCHAR(50),"
    "   PRIMARY KEY(`ID`)"
    ")"
)

TABLES['ZL_Item'] = (
    "CREATE TABLE `ZL_Item` ("
    "   `ID` SMALLINT NOT NULL,"
    "   `Name` VARCHAR(40) NOT NULL,"
    "   `RoomID` SMALLINT,"
    "   `Description` VARCHAR(2000),"
    "   `PointsModifier` TINYINT,"
    "   `AttackModifier` TINYINT,"
    "   `DefenceModifier` TINYINT,"
    "   `NPCID` SMALLINT,"
    "   `PlayerName` VARCHAR(40),"
    "   PRIMARY KEY(`ID`)"
    ")"
)

TABLES['ZL_HallOfFame'] = (
    "CREATE TABLE `ZL_HallOfFame` ("
    "   `ID` SMALLINT NOT NULL,"
    "   `Timestamp` DATETIME,"
    "   `PlayerName` VARCHAR(40) NOT NULL,"
    "   `Class` VARCHAR(25) NOT NULL,"
    "   `Points` INT NOT NULL,"
    "   PRIMARY KEY(`ID`)"
    ")"
)

TABLES['ZL_Movement'] = (
    "CREATE TABLE `ZL_Movement` ("
    "   `Door` SMALLINT NOT NULL,"
    "   `RoomID` SMALLINT NOT NULL,"
    "   `RoomInLeft` SMALLINT,"
    "   `RoomInRight` SMALLINT,"
    "   `RoomInFront` SMALLINT,"
    "   `RoomInBack` SMALLINT,"
    "   `RoomInUp` SMALLINT,"
    "   `RoomInDown` SMALLINT,"
    "   PRIMARY KEY(`Door`, `RoomID`)"
    ")"
)

CONSTRAINTS_ADD = {}

CONSTRAINTS_ADD['ZL_Player'] = (
    "ALTER TABLE `ZL_Player`"
    "   ADD CONSTRAINT `fk_RoomID_1` FOREIGN KEY (`RoomID`) "
    "       REFERENCES `ZL_Room` (`ID`) ON DELETE CASCADE"
)

CONSTRAINTS_ADD['ZL_NPC'] = (
    "ALTER TABLE `ZL_NPC`"
    "   ADD CONSTRAINT `fk_RoomID_2` FOREIGN KEY (`RoomID`) "
    "       REFERENCES `ZL_Room` (`ID`) ON DELETE CASCADE"
)

CONSTRAINTS_ADD['ZL_Item'] = (
    "ALTER TABLE `ZL_Item`"
    "   ADD CONSTRAINT `fk_RoomID_3` FOREIGN KEY (`RoomID`) "
    "       REFERENCES `ZL_Room` (`ID`) ON DELETE CASCADE,"
    "   ADD CONSTRAINT `fk_NPCID` FOREIGN KEY (`NPCID`) "
    "       REFERENCES `ZL_NPC` (`ID`) ON DELETE CASCADE,"
    "   ADD CONSTRAINT `fk_PlayerName_1` FOREIGN KEY (`PlayerName`) "
    "       REFERENCES `ZL_Player` (`Name`) ON DELETE CASCADE"
)

CONSTRAINTS_ADD['ZL_HallOfFame'] = (
    "ALTER TABLE `ZL_HallOfFame`"
    "   add CONSTRAINT `fk_PlayerName_2` FOREIGN KEY (`PlayerName`) "
    "       REFERENCES `ZL_Player` (`Name`) ON DELETE CASCADE"
)

CONSTRAINTS_ADD['ZL_Movement'] = (
    "ALTER TABLE `ZL_Movement`"
    "   ADD CONSTRAINT `fk_RoomID_4` FOREIGN KEY (`RoomID`) "
    "       REFERENCES `ZL_Room` (`ID`),"
    "   ADD CONSTRAINT `fk_RoomInLeft_1` FOREIGN KEY (`RoomInLeft`) "
    "       REFERENCES `ZL_Room` (`ID`),"
    "   ADD CONSTRAINT `fk_RoomInRight_1` FOREIGN KEY (`RoomInRight`) "
    "       REFERENCES `ZL_Room` (`ID`),"
    "   ADD CONSTRAINT `fk_RoomInFront_1` FOREIGN KEY (`RoomInFront`) "
    "       REFERENCES `ZL_Room` (`ID`),"
    "   ADD CONSTRAINT `fk_RoomInBack` FOREIGN KEY (`RoomInBack`) "
    "       REFERENCES `ZL_Room` (`ID`),"
    "   ADD CONSTRAINT `fk_RoomInUp` FOREIGN KEY (`RoomInUp`) "
    "       REFERENCES `ZL_Room` (`ID`),"
    "   ADD CONSTRAINT `fk_RoomInDown` FOREIGN KEY (`RoomInDown`) "
    "       REFERENCES `ZL_Room` (`ID`)"
)

CONSTRAINTS_ADD['ZL_RoomState'] = (
    "ALTER TABLE `ZL_RoomState`"
    "   add CONSTRAINT `fk_RoomID_5` FOREIGN KEY (`RoomID`) "
    "       REFERENCES `ZL_Room` (`ID`) ON DELETE CASCADE"
)

CONSTRAINTS_DROP = {}

CONSTRAINTS_DROP['ZL_Player'] = (
    "ALTER TABLE `ZL_Player`"
    "   DROP FOREIGN KEY `fk_RoomID_1`"
)

CONSTRAINTS_DROP['ZL_NPC'] = (
    "ALTER TABLE `ZL_NPC`"
    "   DROP FOREIGN KEY `fk_RoomID_2`"
)

CONSTRAINTS_DROP['ZL_Item'] = (
    "ALTER TABLE `ZL_Item`"
    "   DROP FOREIGN KEY `fk_RoomID_3`,"
    "   DROP FOREIGN KEY `fk_NPCID`,"
    "   DROP FOREIGN KEY `fk_PlayerName_1`"
)

CONSTRAINTS_DROP['ZL_HallOfFame'] = (
    "ALTER TABLE `ZL_HallOfFame`"
    "   DROP FOREIGN KEY `fk_PlayerName_2`"
)

CONSTRAINTS_DROP['ZL_Movement'] = (
    "ALTER TABLE `ZL_Movement`"
    "   DROP FOREIGN KEY `fk_RoomID_4`,"
    "   DROP FOREIGN KEY `fk_RoomInLeft_1`,"
    "   DROP FOREIGN KEY `fk_RoomInRight_1`,"
    "   DROP FOREIGN KEY `fk_RoomInFront_1`,"
    "   DROP FOREIGN KEY `fk_RoomInBack`,"
    "   DROP FOREIGN KEY `fk_RoomInUp`,"
    "   DROP FOREIGN KEY `fk_RoomInDown`"
)

CONSTRAINTS_DROP['ZL_RoomState'] = (
    "ALTER TABLE `ZL_RoomState`"
    "   DROP FOREIGN KEY `fk_RoomID_5`"
)


def testConnection():
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
        print("Connection complete.")
        cnx.close()


def initializeDatabase():
    cnx = mysql.connector.connect(user=cfg['MariaDB']['user'],
                                      password=cfg['MariaDB']['passwd'],
                                      host=cfg['MariaDB']['host'],
                                      database=cfg['MariaDB']['db'])
    cursor = cnx.cursor()

    for name, dropConstraintLine in CONSTRAINTS_DROP.items():
        try:
            print("Dropping constraints for table {}: ".format(name), end='')
            cursor.execute(dropConstraintLine)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            print("OK")

    for name in TABLES.keys():
        try:
            print("Dropping table {}: ".format(name), end='')
            cursor.execute("DROP TABLE IF EXISTS {}".format(name))
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            print("OK")


    for name, creationLine in TABLES.items():
        try:
            print("Creating table {}: ".format(name), end='')
            cursor.execute(creationLine)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    for name, constraintLine in CONSTRAINTS_ADD.items():
        try:
            print("Adding constraints for table {}: ".format(name), end='')
            cursor.execute(constraintLine)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.commit()
    cnx.close()


def createPlayer():
    cnx = mysql.connector.connect(user=cfg['MariaDB']['user'],
                                      password=cfg['MariaDB']['passwd'],
                                      host=cfg['MariaDB']['host'],
                                      database=cfg['MariaDB']['db'])
    cur = cnx.cursor()
    sql = "LOAD DATA LOCAL INFILE '{}' INTO TABLE ZL_Player " \
          "FIELDS TERMINATED BY ';' LINES TERMINATED BY '\r\n'" \
          "".format(cfg['Datafiles']['ZL_Player'])
    try:
        print("Populating table ZL_Player: ", end='')
        cur.execute(sql)
    except mysql.connector.Error as err:
            print(err.msg)
    else:
        print("OK")

    cur.close()
    cnx.commit()
    cnx.close()


def createNPC():
    cnx = mysql.connector.connect(user=cfg['MariaDB']['user'],
                                      password=cfg['MariaDB']['passwd'],
                                      host=cfg['MariaDB']['host'],
                                      database=cfg['MariaDB']['db'])
    cur = cnx.cursor()
    sql = "LOAD DATA LOCAL INFILE '{}' INTO TABLE ZL_NPC " \
          "FIELDS TERMINATED BY ';' LINES TERMINATED BY '\r\n'" \
          "".format(cfg['Datafiles']['ZL_NPC'])
    try:
        print("Populating table ZL_NPC: ", end='')
        cur.execute(sql)
    except mysql.connector.Error as err:
            print(err.msg)
    else:
        print("OK")

    cur.close()
    cnx.commit()
    cnx.close()


def createRoom():
    cnx = mysql.connector.connect(user=cfg['MariaDB']['user'],
                                      password=cfg['MariaDB']['passwd'],
                                      host=cfg['MariaDB']['host'],
                                      database=cfg['MariaDB']['db'])
    cur = cnx.cursor()
    sql = "LOAD DATA LOCAL INFILE '{}' INTO TABLE ZL_Room " \
          "FIELDS TERMINATED BY ';' LINES TERMINATED BY '\r\n'" \
          "".format(cfg['Datafiles']['ZL_Room'])

    try:
        print("Populating table ZL_Room: ", end='')
        cur.execute(sql)
    except mysql.connector.Error as err:
            print(err.msg)
    else:
        print("OK")

    cur.close()
    cnx.commit()
    cnx.close()


def createRoomState():
    cnx = mysql.connector.connect(user=cfg['MariaDB']['user'],
                                      password=cfg['MariaDB']['passwd'],
                                      host=cfg['MariaDB']['host'],
                                      database=cfg['MariaDB']['db'])
    cur = cnx.cursor()
    sql = "LOAD DATA LOCAL INFILE '{}' INTO TABLE ZL_RoomState " \
          "FIELDS TERMINATED BY ';' LINES TERMINATED BY '\r\n'" \
          "".format(cfg['Datafiles']['ZL_RoomState'])
    try:
        print("Populating table ZL_RoomState: ", end='')
        cur.execute(sql)
    except mysql.connector.Error as err:
            print(err.msg)
    else:
        print("OK")

    cur.close()
    cnx.commit()
    cnx.close()


def createItem():
    cnx = mysql.connector.connect(user=cfg['MariaDB']['user'],
                                      password=cfg['MariaDB']['passwd'],
                                      host=cfg['MariaDB']['host'],
                                      database=cfg['MariaDB']['db'])
    cur = cnx.cursor()
    sql = "LOAD DATA LOCAL INFILE '{}' INTO TABLE ZL_Item " \
          "FIELDS TERMINATED BY ';' LINES TERMINATED BY '\r\n'" \
          "".format(cfg['Datafiles']['ZL_Item'])
    try:
        print("Populating table ZL_Item: ", end='')
        cur.execute(sql)
    except mysql.connector.Error as err:
            print(err.msg)
    else:
        print("OK")

    cur.close()
    cnx.commit()
    cnx.close()

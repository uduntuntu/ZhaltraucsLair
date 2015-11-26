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
    "   `ID` SMALLINT NOT NULL,"
    "   `RoomID` SMALLINT NOT NULL,"
    "   `RoomInNorth` SMALLINT,"
    "   `RoomInSouth` SMALLINT,"
    "   `RoomInEast` SMALLINT,"
    "   `RoomInWest` SMALLINT,"
    "   `RoomInUp` SMALLINT,"
    "   `RoomInDown` SMALLINT,"
    "   PRIMARY KEY(`ID`, `RoomID`)"
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
    "   ADD CONSTRAINT `fk_RoomInNorth` FOREIGN KEY (`RoomInNorth`) "
    "       REFERENCES `ZL_Room` (`ID`),"
    "   ADD CONSTRAINT `fk_RoomInSouth` FOREIGN KEY (`RoomInSouth`) "
    "       REFERENCES `ZL_Room` (`ID`),"
    "   ADD CONSTRAINT `fk_RoomInEast` FOREIGN KEY (`RoomInEast`) "
    "       REFERENCES `ZL_Room` (`ID`),"
    "   ADD CONSTRAINT `fk_RoomInWest` FOREIGN KEY (`RoomInWest`) "
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
    "   DROP FOREIGN KEY `fk_RoomInNorth`,"
    "   DROP FOREIGN KEY `fk_RoomInSouth`,"
    "   DROP FOREIGN KEY `fk_RoomInWest`,"
    "   DROP FOREIGN KEY `fk_RoomInEast`,"
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
        print("Connection to database complete.")
        cnx.close()


def initializeDatabase():
    cnx = mysql.connector.connect(user=cfg['MariaDB']['user'],
                                  password=cfg['MariaDB']['passwd'],
                                  host=cfg['MariaDB']['host'],
                                  database=cfg['MariaDB']['db'])
    cursor = cnx.cursor()

    for name, dropConstraintLine in CONSTRAINTS_DROP.items():
        try:
            cursor.execute(dropConstraintLine)
        except mysql.connector.Error as err:
            print("Error when dropping constraints for table {}: {}"
                  "".format(name, err.msg))

    for name in TABLES.keys():
        try:
            cursor.execute("DROP TABLE IF EXISTS {}".format(name))
        except mysql.connector.Error as err:
            print("Error when Dropping table {}: {}".format(name, err.msg))

    for name, creationLine in TABLES.items():
        try:
            cursor.execute(creationLine)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table {} already exists.".format(name))
            else:
                print("Error when creating table {}: {}".format(name, err.msg))

    for name, constraintLine in CONSTRAINTS_ADD.items():
        try:
            cursor.execute(constraintLine)
        except mysql.connector.Error as err:
            print("Error when adding constraints for table {}: {}"
                  "".format(name, err.msg))

    cursor.close()
    cnx.commit()
    cnx.close()


def populateTables():
    if cfg['OS'] == "Windows":
        lineEnding = '\r\n'
    elif cfg['OS'] == "Linux":
        lineEnding = '\n'

    for table in ('ZL_Room', 'ZL_RoomState', 'ZL_Player', 'ZL_NPC', 'ZL_Item',
                  'ZL_HallOfFame', 'ZL_Movement'):
        cnx = mysql.connector.connect(user=cfg['MariaDB']['user'],
                                      password=cfg['MariaDB']['passwd'],
                                      host=cfg['MariaDB']['host'],
                                      database=cfg['MariaDB']['db'])
        cur = cnx.cursor()

        sql = "LOAD DATA LOCAL INFILE '{}' INTO TABLE {} " \
              "FIELDS TERMINATED BY ';' LINES TERMINATED BY '{}' " \
              "IGNORE 1 LINES" \
              "".format(cfg['Datafiles'][table], table, lineEnding)

        try:
            cur.execute(sql)
        except mysql.connector.Error as err:
            print("Error when populating table {}: ".format(table, err.msg))

        cur.close()
        cnx.commit()
        cnx.close()


def doQuery(sql):
    cnx = mysql.connector.connect(user=cfg['MariaDB']['user'],
                                  password=cfg['MariaDB']['passwd'],
                                  host=cfg['MariaDB']['host'],
                                  database=cfg['MariaDB']['db'])
    cur = cnx.cursor()

    result = []
    try:
        cur.execute(sql)
        result = cur.fetchall()
    except mysql.connector.Error as err:
        ## By next statement we can catch "No result set to fetch from." error.
        ## errno is so general that we don't want catch it during development.
        # if err.errno == -1:
        #     pass
        # else:
        print('Error in query "{}": ({}) {}'
              ''.format(sql, err.errno, err.msg)
              )

    cur.close()
    cnx.commit()
    cnx.close()

    return result


def getPosition(playerRoom):
    sql = "SELECT ZL_Room.Description " \
          "FROM ZL_Room " \
          "WHERE ZL_Room.ID = {}".format(playerRoom)
    result = doQuery(sql)
    if len(result) == 1:
        return result[0][0]


class Player:
    def __init__(self, playerName, playerClass):
        self.playerName = playerName
        self.playerClass = playerClass
        self.roomID = 1
        self.points = 0
        self.inventory = []

        if self.playerClass == "barbarian":
            self.HP = 50
            self.agility = 5
            self.intelligence = 1
            self.strength = 4
        elif self.playerClass == "thief":
            self.HP = 40
            self.agility = 9
            self.intelligence = 8
            self.strength = 4


def createPlayer():
    playerName = input("What's your name? ")
    playerClass = input("Do you want to be a Barbarian or a Thief? ").lower()
    while playerClass not in ("barbarian", "thief"):
        playerClass = input(
            "Do you want to be a Barbarian or a Thief? ").lower()
    player = Player(playerName, playerClass)

    sql = "SELECT Name FROM ZL_Player WHERE Name = '{}'" \
          "".format(player.playerName)
    result = doQuery(sql)
    if len(result) > 0:
        print("Player exists. Cannot create player")
    else:
        sql = "INSERT INTO `ZL_Player` " \
              "(Name, HP, Class,RoomID,Points,Agility,Intelligence,Strength) " \
              "VALUES ('{}',{},'{}',{},{},{},{},{})".format(player.playerName,
                                                            player.HP,
                                                            player.playerClass,
                                                            player.roomID,
                                                            player.points,
                                                            player.agility,
                                                            player.intelligence,
                                                            player.strength
                                                            )
        result = doQuery(sql)

    return player


def getPlayer():
    sql = "SELECT Name,Class FROM ZL_Player"
    result = doQuery(sql)
    if len(result) == 1:
        player = Player(result[0][0], result[0][1])

        return player

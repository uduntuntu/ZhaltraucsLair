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
    "   `Description` VARCHAR(2000),"
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
            return False
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            return False
        else:
            print(err)
            return False
    else:
        print("Connection to database complete.")
        cnx.close()
        return True


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
            print("Error when populating table {}: {}".format(table, err.msg))

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
        # Discartd error: "(-1) No result set to fetch from."
        # when doing import or update query.
        if err.errno == -1:
            pass
        else:
            print('Error in query "{}": ({}) {}'
                  ''.format(sql, err.errno, err.msg)
                  )

    cur.close()
    cnx.commit()
    cnx.close()

    return result


def getRoomDescription(playerRoom):
    sql = "SELECT ZL_Room.Description " \
          "FROM ZL_Room " \
          "WHERE ZL_Room.ID = {}".format(playerRoom)
    result = doQuery(sql)
    if len(result) == 1:
        return result[0][0]


def getRoomState(playerRoom):
    sql = "SELECT ZL_RoomState.Description, ZL_Room.ID " \
          "FROM ZL_RoomState INNER JOIN ZL_Room " \
          "ON ZL_Room.State = ZL_RoomState.ID " \
          "WHERE ZL_RoomState.RoomID = {} " \
          "AND ZL_Room.ID = {}".format(playerRoom,playerRoom)
    result = doQuery(sql)
    if len(result) == 1:
        return result[0][0]
    else:
        return None


def getRoomStateID(playerRoom):
    sql = "SELECT ZL_Room.State FROM ZL_Room WHERE ZL_Room.ID = {}" \
          "".format(playerRoom)
    result = doQuery(sql)
    if len(result) == 1:
        return result[0][0]
    else:
        return None


class Player:
    def __init__(self, playerName, playerClass,
                 roomID=1, points=0, inventory=[]):
        self.playerName = playerName
        self.playerClass = playerClass
        self.roomID = roomID
        self.points = 0
        self.inventory = inventory

        if self.playerClass == "barbarian":
            self.HP = 50
            self.agility = 5
            self.intelligence = 1
            self.strength = 12
        elif self.playerClass == "thief":
            self.HP = 40
            self.agility = 12
            self.intelligence = 8
            self.strength = 5


class NPC:
    def __init__(self,
                 NPCName,
                 HP,
                 Agility,
                 Strength,
                 Pointsmodifier,
                 roomID,
                 ID
                 ):
        self.NPCName = NPCName
        self.roomID = roomID
        self.HP = HP
        self.agility = Agility
        self.strength = Strength
        self.pointsmodifier = Pointsmodifier
        self.ID = ID


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
    sql = "SELECT Name,Class,RoomID FROM ZL_Player"
    result = doQuery(sql)

    if len(result) != 0:
        sql = "Select ZL_Item.Name FROM ZL_Item " \
              "WHERE ZL_Item.PlayerName = '{}'".format(result[0][0])
        inv = doQuery(sql)
        inventory = []
        for i in range(0,len(inv)):
            inventory.append(inv[i][0])

    # Because our database is initialized when starting new game, we can't have
    # more than one player in database. In case something is gone wrong in
    # player creation process, result can be empty.
    if len(result) != 0:
        player = Player(result[0][0], result[0][1], result[0][2],inventory)

        return player
    else:
        initializeDatabase()
        populateTables()
        player = createPlayer()
        return player

def updatePlayer(player):
    sql = "SELECT Name,RoomID,HP,Points FROM ZL_Player"
    result = doQuery(sql)
    sql = "Select ZL_Item.Name FROM ZL_Item " \
          "WHERE ZL_Item.PlayerName = '{}'".format(result[0][0])
    inv = doQuery(sql)
    player.playerName = result[0][0]
    player.roomID = result[0][1]
    player.HP = result[0][2]
    player.points = result[0][3]
    inventory = []
    for i in range(0,len(inv)):
        inventory.append(inv[i][0])
    player.inventory = inventory

    return player


def updateNPC(npc):
    sql = "SELECT HP FROM ZL_NPC WHERE ID = {}".format(npc.ID)
    result = doQuery(sql)
    npc.HP = result[0][0]

    return npc


def cleanNPCFromRoom(npc):
    sql = "UPDATE ZL_NPC SET RoomID = NULL WHERE ID = {}".format(npc.ID)
    doQuery(sql)


def dropNPCItem(npc):
    sql = "UPDATE ZL_Item SET RoomID={} WHERE NPCID={}".format(npc.roomID,
                                                               npc.ID)
    doQuery(sql)


def getDirections(roomID):
    sql = "SELECT RoomInNorth,RoomInSouth,RoomInEast,RoomInWest," \
          "RoomInUp,RoomInDown FROM ZL_Movement WHERE RoomID = {}" \
          "".format(roomID)
    result = doQuery(sql)
    directions = {}
    if result != []:
        if result[0][0] is not None:
            directions['north'] = result[0][0]
        if result[0][1] is not None:
            directions['south'] = result[0][1]
        if result[0][2] is not None:
            directions['east'] = result[0][2]
        if result[0][3] is not None:
            directions['west'] = result[0][3]
        if result[0][4] is not None:
            directions['up'] = result[0][4]
        if result[0][5] is not None:
            directions['down'] = result[0][5]
    else:
        print("No movement set in database for this room.")
    return directions


def setPlayerRoomID(roomID):
    sql = "UPDATE ZL_Player SET RoomID = {}".format(roomID)
    doQuery(sql)


def getItemsInRoom(roomID):
    sql = "SELECT ZL_Item.Name " \
          "FROM ZL_Item " \
          "INNER JOIN ZL_Room " \
          "ON ZL_Item.RoomID = ZL_Room.ID " \
          "WHERE ZL_Item.RoomID = {}".format(roomID)
    result = doQuery(sql)
    items = []
    if result != []:
        for i in range(0,len(result)):
            items.append(result[i][0])

    return items

def getNPCsInRoom(roomID):
    sql = "SELECT ZL_NPC.Name," \
          " ZL_NPC.HP, " \
          "ZL_NPC.Agility, " \
          "ZL_NPC.Strength, " \
          "ZL_NPC.PointModifier, " \
          "ZL_NPC.RoomID, "  \
          "ZL_NPC.ID " \
          "FROM ZL_NPC " \
          "INNER JOIN ZL_Room " \
          "ON ZL_NPC.RoomID = ZL_Room.ID " \
          "WHERE ZL_NPC.RoomID = {}".format(roomID)
    result = doQuery(sql)
    npcs = {}
    if result != []:
        for i in range(0,len(result)):
            npc = NPC(result[i][0],
                      result[i][1],
                      result[i][2],
                      result[i][3],
                      result[i][4],
                      result[i][5],
                      result[i][6]
                      )
            npcs[str(i)] = (npc)

    return npcs


def getNPCDescription(npc):
    sql = "SELECT Description FROM ZL_NPC WHERE ID = {}".format(npc.ID)
    result = doQuery(sql)
    return result[0][0]


def bringNPCToRoom(roomID, ID):
    sql = "UPDATE ZL_NPC SET RoomID = {} WHERE RoomID IS NULL AND ID = {}" \
          "".format(roomID, ID)
    doQuery(sql)


def getItemDescription(item):
    sql = "SELECT ZL_Item.Description FROM ZL_Item " \
              "WHERE ZL_Item.Name = '{}'".format(item)
    result = doQuery(sql)
    if result[0][0] != None:
        return result[0][0]
    else:
        return ('Item "{}" doesn\'t have a description'.format(item))


def takeItem(item, player):
    sql = "UPDATE ZL_Item SET PlayerName='{}', " \
          "RoomID = NULL " \
          "WHERE ZL_Item.Name = '{}' AND " \
          "ZL_Item.RoomID = {}".format(player.playerName,item,player.roomID)
    doQuery(sql)


def dropItem(item,player):
    sql = "UPDATE ZL_Item SET PlayerName=NULL," \
          "RoomID = {} WHERE ZL_Item.Name='{}' AND " \
          "PlayerName = '{}'" \
          "".format(player.roomID,item,player.playerName)
    doQuery(sql)


def useItem(item):
    sql = "UPDATE ZL_Item SET PlayerName = NULL " \
          "WHERE Name = '{}'" \
          "".format(item)
    doQuery(sql)


def updateRoomState(roomID,stateToDo):
    sql = "UPDATE ZL_Room SET State = {} WHERE ID = {}" \
          "".format(stateToDo,roomID)
    doQuery(sql)


def updateMovements(player,north, south, east, west, up, down):
    sql = "UPDATE ZL_Movement SET " \
          "RoomInNorth={}," \
          "RoomInSouth={}," \
          "RoomInEast={}," \
          "RoomInWest={}," \
          "RoomInUp={}," \
          "RoomInDown={} " \
          "WHERE ZL_Movement.RoomID={}" \
          "".format(north, south, east, west, up, down,player.roomID)
    doQuery(sql)


def modifyhp(HP):
    sql = "UPDATE ZL_Player SET HP = HP + {}".format(HP)
    doQuery(sql)


def modifyNPCHP(HP,npc):
    sql = "UPDATE ZL_NPC SET HP = HP + {} " \
          "WHERE ID = {}".format(HP,npc.ID)
    doQuery(sql)


def gethp():
    sql = "SELECT hp FROM ZL_Player"
    hp = doQuery(sql)
    return hp[0][0]

def modifypoints(points):
    sql = "UPDATE ZL_Player SET Points = Points + {}".format(points)
    doQuery(sql)

def getPointsFromPlayer():
    sql = "SELECT Points FROM ZL_Player"
    points = doQuery(sql)

    return points[0][0]


def getPointsFromItem(itemName):
    sql = "SELECT PointsModifier FROM ZL_Item WHERE Name = '{}'".format(itemName)
    points = doQuery(sql)

    return points[0][0]


def getPointsFromRoom(roomID):
    sql = "SELECT PointsModifier FROM ZL_Room WHERE ID = {}".format(roomID)
    points = doQuery(sql)

    return points[0][0]


def getPointsFromNPC(ID):
    sql = "SELECT PointModifier FROM ZL_NPC WHERE ID = {}".format(ID)
    points = doQuery(sql)

    return points[0][0]


def getPlayerArmor(player):
    sql = "SELECT ZL_Item.DefenceModifier FROM ZL_Item " \
          "WHERE PlayerName = '{}'".format(player.playerName)
    result = doQuery(sql)
    if len(result) != 0:
        if result[0][0] != None:
            return result[0][0]
        else:
            return 0
    else:
        return 0


def getPlayerWeapon(player):
    sql = "SELECT ZL_Item.AttackModifier FROM ZL_Item " \
          "WHERE PlayerName = '{}'".format(player.playerName)
    result = doQuery(sql)
    if len(result) != 0:
        if result[0][0] != None:
            return result[0][0]
        else:
            return 0
    else:
        return 0

def getNPCArmor(npc):
    sql = "SELECT ZL_Item.DefenceModifier FROM ZL_Item " \
          "WHERE NPCID = '{}'".format(npc.ID)
    result = doQuery(sql)
    if len(result) != 0:
        if result[0][0] != None:
            return result[0][0]
        else:
            return 0
    else:
        return 0


def getNPCWeapon(npc):
    sql = "SELECT ZL_Item.DefenceModifier FROM ZL_Item " \
          "WHERE NPCID = '{}'".format(npc.ID)
    result = doQuery(sql)
    if len(result) != 0:
        if result[0][0] != None:
            return result[0][0]
        else:
            return 0
    else:
        return 0
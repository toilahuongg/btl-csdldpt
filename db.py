import mysql.connector
from typing import List
from character import Character
from imageFeature import ImageFeature
from utils import str_to_hog
from hog import compare_hog


conn = mysql.connector.connect(user='root', host='localhost', database='feature')

def createTable():
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE IF EXISTS `ImageFeature`''')
    cursor.execute('''DROP TABLE IF EXISTS `Character`''')

    cursor.execute('''CREATE TABLE `Character` (
        ID INTEGER AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(100),
        `Desc` TEXT,
        Folder VARCHAR(100) NULL
    )''')

    cursor.execute('''CREATE TABLE `ImageFeature` (
        ID INTEGER AUTO_INCREMENT PRIMARY KEY,
        CharacterID INTEGER,
        Src VARCHAR(255),
        Feature TEXT,
        FOREIGN KEY (CharacterID) REFERENCES `Character`(ID)
    )''')

    conn.commit()
    cursor.close()
  
def createCharacter(name: str, desc: str, folder: str):
    cursor = conn.cursor()
    insert_query = "INSERT INTO `Character` (Name, `Desc`, Folder) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (name, desc, folder))
    conn.commit()
    cursor.close()

def createImageFeature(id: int, src: str, feature: str):
    cursor = conn.cursor()
    insert_query = "INSERT INTO `ImageFeature` (CharacterID, Src, Feature) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (id, src, feature))
    conn.commit()
    cursor.close()

def getCharacterByID(ID: int):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `Character` WHERE ID = %s LIMIT 1", (ID,))
    rows = cursor.fetchall()
    cursor.close()
    if len(rows) == 0: return None
    row = rows[0]
    return Character(row[0], row[1], row[2], row[3])

def getAllCharacters():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `Character`")
    rows = cursor.fetchall()
    cursor.close()
    character_list: List[Character] = []
    for row in rows:
        character = Character(row[0], row[1], row[2], row[3])
        character_list.append(character)
    return character_list


def getFeaturesByCharacter(ID: int):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `ImageFeature` WHERE CharacterID = %s", (ID,))
    rows = cursor.fetchall()
    image_feature_list: List[ImageFeature] = []
    cursor.close()
    for row in rows:
        image_feature = ImageFeature(row[0], row[1], row[2], row[3])
        image_feature_list.append(image_feature)
    return image_feature_list

def getImagesByHOG(ID: int, hog, n = 5):
    image_feature_list = getFeaturesByCharacter(ID)
    similarity_results = []

    for image in image_feature_list: 
        image_hog = str_to_hog(image.Feature)
        similarity_results.append({ "src": image.Src, "distance": compare_hog(image_hog, hog)})


    similarity_results.sort(key=lambda x: x.get('distance'))
    similar_images = similarity_results[:n]

    return similar_images
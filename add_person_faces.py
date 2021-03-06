import sys
import os
import time
import cognitive_face as CF
from global_variables import personGroupId
import urllib
import sqlite3

Key = 'aeac52f65e1a44da90aaeeab84360441'
CF.Key.set(Key)


def get_person_id():
    person_id = ''
    extractId = str(sys.argv[1])[-2:]
    connect = sqlite3.connect("Face-DataBase")
    c = connect.cursor()
    cmd = "SELECT * FROM Students WHERE ID = " + extractId
    c.execute(cmd)
    row = c.fetchone()
    person_id = row[3]
    connect.close()
    return person_id


if len(sys.argv) != 1:
    currentDir = os.path.dirname(os.path.abspath(__file__))
    imageFolder = os.path.join(currentDir, "dataset/" + str(sys.argv[1]))
    person_id = get_person_id()

    print(person_id)
    for filename in os.listdir(imageFolder):
        if filename.endswith(".jpg"):
            print(filename)
            imgurl = urllib.pathname2url(os.path.join(imageFolder, filename))
            print(imgurl)
            imgurl = "C:/Users/Dharmathej/Downloads/attendancesystem-master/attendancesystem-master/bluetooth_jpg.jpg"
            res = CF.face.detect(imgurl)
            if len(res) != 1:
                print()
            else:
                res = CF.person.add_face(imgurl, personGroupId, person_id)
                print(res)
            time.sleep(6)

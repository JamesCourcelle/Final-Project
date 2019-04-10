import subprocess
import os
from pathlib import Path
from pymongo import MongoClient

def export_collection(file_name):
    connection = MongoClient('localhost', 27017)
    db = connection['CityData']
    collection = db['bids']

    path = ("C:\\Program Files\\MongoDB\\Server\\4.0\\bin\\")
    os.chdir(path)
    file = "C:\\data\\dump\\CityData\\" + file_name + ".csv"
    command = ("mongoexport --db CityData --collection bids --type=csv --fields AuctionID,AuctionTitle,Fund,AuctionFeeTotal --out %s" % (file))

    subprocess.run(command, creationflags = subprocess.CREATE_NEW_CONSOLE)

import os
import subprocess

from pymongo import MongoClient


def check_for_database(host, port, db_name):
    connection = MongoClient(host, port)

    database_name = connection.list_database_names()

    if db_name in database_name:
        print("{0} found...".format(db_name))
    else:
        os.chdir('C:\\')
        try:
            os.mkdir("\\data\\db")
            print("Directory successfully created...")
        except OSError:
            print("Directory creation failed...")

        try:
            os.chdir('C:\\Program Files\\MongoDB\\Server\\4.0\\bin')

            command = ("mongoimport -d CityData -c bids --type CSV --file eBid_Monthly_Sales.csv --headerline")

            subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)
            print("Database successfully created...")
        except OSError:
            print("Database creation failed...")


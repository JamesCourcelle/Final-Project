from os import abort
from pymongo import MongoClient

def find_bid_in_range(host, port, udb, ucollection):
    connection = MongoClient(host, port)
    db = connection[udb]
    collection = db[udb]
    cursor = collection
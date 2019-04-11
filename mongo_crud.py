import json
from bson import json_util
from pymongo import MongoClient
import pprint

def find_bid(host, port, udb, ucollection, bid_id):
    connection = MongoClient(host, port)
    db = connection [udb]
    collection = db[ucollection]


    pipeline = [
        {"$match" : {"AuctionID" : bid_id}},
        {"$project" : {"AuctionID" : 1, "AuctionTitle" : 1, "Fund" : 1, "AuctionFeeTotal" : 1, "_id" : 0}}
        ]
    
    # Convert the pipline values to a printable format
    cursor = collection.aggregate(pipeline)
    results = list(cursor)

    # Pull the dictionary object out of the list
    results_string = results[0]
    listed_values = []

    for i in results_string:
        value = results_string[i]
        listed_values.append(value)
    print_results(listed_values)

def print_results(values):
    print("{0} | {1} | {2} | {3}".format(values[1], values[0], values[2], values[3]))

    



if __name__ == '__main__':
    bid = int(input("Enter a bid ID: "))
    find_bid('localhost', 27017, 'CityData', 'bids', bid)
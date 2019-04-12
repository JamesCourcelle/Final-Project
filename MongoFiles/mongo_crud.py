from os import abort
from pymongo import MongoClient

def print_results(values):
    print("{0} | {1} | {2} | {3}".format(values[0], values[1], values[2], values[3]))

# creates an index based on the field passed in and puts it in ascending order.
def create_index(host, port, udb, ucollection, field):
    connection = MongoClient(host, port)
    db = connection [udb]
    collection = db[ucollection]

    collection.create_index(field)


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

    if not results:
        print("No bid found....")
        return None

    # Pull the dictionary object out of the list
    results_string = results[0]
    listed_values = []

    for i in results_string:
        value = results_string[i]
        listed_values.append(value)
   
    return listed_values


def create_bid(host, port, udb, ucollection):
    connection = MongoClient(host, port)
    db = connection [udb]
    collection = db[ucollection]

    field_list = ["AuctionID", "AuctionTitle", "Fund", "AuctionFeeTotal"]
    new_bid = []

    for field in field_list:
        user_value = input("Enter {0}:  ".format(field))
        new_bid.append(user_value)

        # Check if bid exists with AuctionID and stop creation if it does.
        check_bid = find_bid(host, port, udb, ucollection, int(user_value))

        if check_bid:
            print("Bid with that AuctionID already exists...")
            return None

    bid = {"AuctionID" : int(new_bid[0]),
           "AuctionTitle" : new_bid[1],
           "Fund" : new_bid[2],
           "AuctionFeeTotal" : new_bid[3]}

    try:
        collection.insert_one(bid).inserted_id
        find_bid(host, port, udb, ucollection, int(new_bid[0]))
    except:
        abort(400, str("Error in process. Aborted."))


def update_bid(host, port, udb, ucollection, bid_id):
    connection = MongoClient(host, port)
    db = connection [udb]
    collection = db[ucollection]

    value = {"AuctionID" : bid_id}
    bid = collection.find_one(value)

    field_list = ["AuctionTitle", "Fund", "AuctionFeeTotal"]
    
    # Check if bid exists before trying to update it.
    check_bid = find_bid(host, port, udb, ucollection, int(bid_id))
    if not check_bid:
        return None

    for field in field_list:
        # Loop here is for input validation.
        loop_condition = True
        while loop_condition:
            user_choice = input("Update {0}... (Y/N) ".format(field))
            if user_choice is 'Y' or user_choice is 'y':
                try:
                    user_value = input("Enter a new value: ")
                    update = {field : user_value}
                    collection.update_one({"AuctionID" : bid_id} , {"$set" : update})
                except:
                    abort(400, str("Error in process. Aborted."))

                loop_condition = False
            elif user_choice is 'N' or user_choice is 'n':
                loop_condition = False
            else:
                print("Invalid input, please enter valid input")

def delete_bid(host, port, udb, ucollection, bid_id):
    connection = MongoClient(host, port)
    db = connection [udb]
    collection = db[ucollection]

    value = {"AuctionID" : bid_id}
    bid = collection.find_one(value)

    try:
        collection.delete_one({'AuctionID' : bid_id})
        print("Bid successfully removed from the database")
    except:
        abort(400, str("Error in process. Aborted."))

if __name__ == '__main__':
    bid = int(input("Enter a bid ID: "))
    found_bid = find_bid('localhost', 27017, 'CityData', 'bids', bid)
    print(found_bid)

    #update_bid('localhost', 27017, 'CityData', 'bids', bid)
    #create_index('localhost', 27017, 'CityData', 'bids', 'AuctionID')
    #create_bid('localhost', 27017, 'CityData', 'bids')
    #delete_bid('localhost', 27017, 'CityData', 'bids', bid)


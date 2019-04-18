from pymongo import MongoClient


def find_bid_in_range(host, port, udb, ucollection, gte, lte):
    connection = MongoClient(host, port)
    db = connection[udb]
    collection = db[ucollection]

    # cursor finds the bids within the given range. This is then converted to a Python list object
    # so that it can be printed below.
    cursor = collection.find({"AuctionFeeTotal": {"$gte": gte, "$lte" : lte}})
    results = list(cursor)

    # Validates that there are bids to be printed.
    if results is None:
        print("No bids found...")
        return None

    # Print column titles
    field_list = ["AuctionID", "AuctionTitle", "Fund", "AuctionFeeTotal"]

    print("{0} | {1} | {2} | {3}".format(field_list[0], field_list[1], field_list[2], field_list[3]))

    for i in results:
        listed_values = []
        for j in i:
            listed_values.append(i[j])
        print("{0} | {1} | {2} | {3}".format(listed_values[2], listed_values[1], listed_values[3], listed_values[9]))

    return None


# check_values abstracts the code for finding bids in the given range. The functions and logic below
# validate the user input.
def check_values():
    loop_condition = True
    print("Find bids between a lesser and greater value Auction Fee Total")
    while loop_condition:
        try:
            lesser = int(input("Enter the lesser value: "))
            greater = int(input("Enter the greater value: "))
        except:
            print("Enter a valid input...")
        if lesser > greater:
            print("The lower value is greater than the higher value. Please enter valid inputs...")
        else:
            find_bid_in_range('localhost', 27017, 'CityData', 'bids', lesser, greater)
            loop_condition = False


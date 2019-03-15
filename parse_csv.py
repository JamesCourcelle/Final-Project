import csv


# Opening file to be read and creating a list that contains each bid. DictReader is used to store each bid value with
# its associated key value.
def open_file(file):
    bid_list = []
    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for bid in csv_reader:
            bid_list.append(bid)

        return bid_list


def print_bid(bid):
    print("%s | %s | %s | %s" % (bid.bid_id, bid.title, bid.fund, bid.amount))




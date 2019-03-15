from operator import itemgetter
import parse_csv


class Bid():
    def __init__(self, bid):
        self.bid_id = int(bid["Auction ID"])
        self.title = bid["Auction Title"]
        self.fund = bid["Fund"]
        self.amount = bid["Auction Fee Total"]
        
class Node():
    def __init__(self, bid):
        self.right = None
        self.left = None
        self.bid = bid
        

class BinarySearchTree():
    def __init__(self):
        self.root = None
        
    
    def load_bids(self, csv_path):
        print("Loading CSV file...")   
        list_bids = parse_csv.open_file(csv_path)
        sorted_list = sorted(list_bids, key=itemgetter("Auction ID"))
        start = 0
        end = len(sorted_list) - 1
        print("%s files loaded..." % len(sorted_list))
    
        
        try:
            self.root = self.create_tree(sorted_list, start, end)
            print("Loading Complete...")
        except IOError:
            print("An error occurred when trying to read the file")

        
    def create_tree(self, bid_list, start, end):
        if start > end:
            return None
        
        try:
            midpoint = int((start + end) / 2)
            root = Node(Bid(bid_list[midpoint]))
            root.left = self.create_tree(bid_list, start, midpoint-1)
            root.right = self.create_tree(bid_list, midpoint+1, end)
            
            return root
        except:
            print("Out of bounds thrown. Midpoint is %s and end is %s" % (midpoint, end))
        

    def display_all_bids(self, node):
        if node is not None:
            self.display_all_bids(node.left)
            parse_csv.print_bid(node.bid)        
            self.display_all_bids(node.right)
        
    
    def search_tree(self):
        if self.root is None:
            print("No file loaded...")
            return
        
        current_node = self.root
        search_bid = int(input("Enter a Bid ID: "))
        found = False
        
        while not found:              
            if search_bid == current_node.bid.bid_id:
                parse_csv.print_bid(self.root.bid)
                found = True
            elif search_bid < current_node.bid.bid_id:
                current_node = current_node.left
            else:
                current_node = current_node.right
                
            if current_node == None:
                print("No bid found...")
                found = True
    
    
bst = BinarySearchTree()
csv_path = 'eBid_Monthly_Sales.csv'
user_choice = 0

while user_choice is not 9:
    print("Menu:")
    print("  1. Load Bids")
    print("  2. Display all Bids")
    print("  3. Find Bid")
    print("  4. Remove Bid")
    print("  9. Exit")
    user_choice = int(input("Enter your choice: "))
    
    if user_choice is 1:
        bst.load_bids(csv_path)
    elif user_choice is 2:
        node = bst.root
        bst.display_all_bids(node)
    elif user_choice is 3:
        bst.search_tree()
    
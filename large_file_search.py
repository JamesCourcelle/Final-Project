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
        
# Count created for the purpose of testing in its current state.
# TODO create an option for the user to get a count of how many entries were taken in
# from the CSV file.
class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.node_count = 0
        
    
    def load_bids(self, csv_path):
        print("Loading CSV file...")   
        list_bids = parse_csv.open_file(csv_path)
        
        # Sorting the entries taken in from the CSV file so that the BST is balanced. This results
        # in the most efficient traversal of the BST when searching or deleting an entry.
        sorted_list = sorted(list_bids, key=itemgetter("Auction ID"))
        start = 0
        end = len(sorted_list) - 1
        print("%s files loaded..." % len(sorted_list))
    
        
        try:
            self.root = self.create_tree(sorted_list, start, end)
            print("Loading Complete...")
        except IOError:
            print("An error occurred when trying to read the file")
       
    # Recursive function below handles the creation of the BST. This is called in the load_bids function
    # directly above. We will also handle a count for node numbers in this function.  
    def create_tree(self, bid_list, start, end):
        if start > end:
            return None
        

        try:
            self.node_count += 1
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
        
    
    def search_tree(self, search_bid):
        if self.root is None:
            print("No file loaded...")
            return

        current_node = self.root
        found = False
        
        while not found:
            # This is statement handles if a bid has been deleted.
            if current_node.bid == None:
                return None
            if search_bid == current_node.bid.bid_id:
                return current_node
            elif search_bid < current_node.bid.bid_id:
                current_node = current_node.left
            else:
                current_node = current_node.right
                
            if current_node == None:
                return None

    # Function to check if a bid for deletion is found. This function acts as the actual
    # deletion of the found bid along with validating the input.
    def check_bid_for_deletion(self, bid, bid_id):
        if self.search_tree(bid_id) is None:
            return "No bid found for deletion..."
        else:
            deleted_bid = self.delete_bid(bid, bid_id)
            deleted_bid.bid = None
            return "Bid successfully deleted..."
      

    # This function runs in check_bid_for_deletion method.    
    def delete_bid(self, bid, bid_id):
        parent = None
        current_bid = bid

        if current_bid is None:
            return None

        while (current_bid != None):
            if current_bid.bid.bid_id == bid_id:
                if current_bid.left == None and current_bid.right == None:
                    if parent.bid == None:
                        current_bid = None
                    elif parent.left == current_bid:
                        parent.left = None
                    else:
                        parent.right = None
                elif current_bid.left != None and current_bid.right == None:
                    if parent == None:
                        current_bid = current_bid.left
                    elif parent.left == current_bid:
                        parent.left = current_bid.left
                    else:
                        parent.right = current_bid.left
                elif current_bid.left == None and current_bid.right != None:
                    if parent == None:
                        current_bid = parent.right
                    elif parent.left == current_bid:
                        parent.left = current_bid.right
                    else:
                        parent.right = current_bid.right
                else:
                    successor = current_bid.right
                    while successor.left is not None:
                        successor = successor.left
                    self.delete_bid(successor, current_bid.bid.bid_id)
                return current_bid
            elif current_bid.bid.bid_id < bid_id:
                parent = current_bid
                current_bid = current_bid.right
            else:
                parent = current_bid
                current_bid = current_bid.left
            

if __name__ == "__main__":    
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
            search_bid = int(input("Enter a Bid ID: "))
            found_bid = bst.search_tree(search_bid)

            if found_bid is not None:
                parse_csv.print_bid(found_bid.bid)
            else:
                print("No bid found...")
        elif user_choice is 4:
            deleted_bid = int(input("Enter a Bid ID: "))
            deleted_bid = bst.check_bid_for_deletion(bst.root, deleted_bid)
            print(deleted_bid)
    
from operator import itemgetter
import parse_csv
import file_output


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
        
        # Code below sets the root as the middle most bid based on ID values. This process creates a balanced tree
        # making the most efficient traversal.
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
            print("No bid found for deletion...")
            return None
        else:
            print("Bid successfully deleted...")
            #deleted_bid = self.delete_bid(bid, bid_id)
            return self.delete_bid(bid, bid_id)
    
    # Method used in delete_bid 
    def minimum_value_bid(self, bid):
        current_bid = bid
        while current_bid.left is not None:
            current_bid = current_bid.left

        return current_bid
            

    # This function runs in check_bid_for_deletion method.    
    def delete_bid(self, bid, bid_id):
        # Setting up base case
        if bid is None:
            return None

        # If bid_id passed in is smaller than root.
        if bid_id < bid.bid.bid_id:
            bid.left = self.delete_bid(bid.left, bid_id)
        # If bid_id passed in is larger than root.
        elif bid_id > bid.bid.bid_id:
            bid.right = self.delete_bid(bid.right, bid_id)
        # If bid_id matches the bid_id of the bid passed into the function
        else:
            # Two conditions handle if there is one or no children nodes to the root
            if bid.left is None:
                temp = bid.right
                bid = None
                return temp
            elif bid.right is None:
                temp = bid.left
                bid = None
                return temp
            
            # if there are two children, the following code traverses the code to
            # the smallest successor

            temp = self.minimum_value_bid(bid.right)
          
            bid.bid = temp.bid
            bid.right = self.delete_bid(bid.right, temp.bid.bid_id)
        return bid

      

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
        print("  5. Create File")
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
            bst.root = bst.check_bid_for_deletion(bst.root, deleted_bid)
         
        elif user_choice is 5:
            file_name = input("Enter a file name: ")
            labels = ["Auction ID", "Auction Title", "Fund", "Auction Fee Total"]
            try:
                file_output.create_csv(file_name, bst, labels)
                print("File successfully created...")
            except:
                print("File creation failed...")
    
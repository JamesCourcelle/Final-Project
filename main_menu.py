# TODO complete a menu to select between local file search and database
from pathlib import Path
import subprocess
import large_file_search
import parse_csv
import start_mongod


if __name__ == "__main__":
    start_mongod.start_mongod()


    bst = large_file_search.BinarySearchTree()
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
            bst.root = bst.delete_bid(bst.root, deleted_bid)
         
        elif user_choice is 5:
            file_name = input("Enter a file name: ")
            labels = ["Auction ID", "Auction Title", "Fund", "Auction Fee Total"]
            try:
                file_output.create_csv(file_name, bst, labels)
                print("File successfully created...")
            except:
                print("File creation failed...")
    # Killing the MongoDB database
    print("Shutting down MongdoDB database...")
    start_mongod.kill_mongod()
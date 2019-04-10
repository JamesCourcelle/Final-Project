# TODO complete a menu to select between local file search and database
from pathlib import Path
import subprocess
import large_file_search
import parse_csv
import start_kill_mongod
import time


if __name__ == "__main__":
    system_choice = 0

    while system_choice is not 3:
        print("Load from local file or from database\n(database has more advanced querying)")
        print("  1. Local File")
        print("  2. Database")
        print("  3. Exit")
        system_choice = int(input("Enter your choice: "))
        
        if system_choice is 1:
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

        elif system_choice is 2:
            start_kill_mongod.start_mongod()
            time.sleep(4)

            # Killing the MongoDB database
            print("Shutting down MongdoDB database...")
            start_kill_mongod.kill_mongod()
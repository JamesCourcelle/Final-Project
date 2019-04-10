from pathlib import Path
import subprocess
import time
import os.path

import large_file_search
import parse_csv
import start_kill_mongod
import file_output
import mongo_file_export


if __name__ == "__main__":
    system_choice = 0

    while system_choice is not 3:
        print("Load from local file or from database\n(database has more advanced querying)")
        print("  1. Local File")
        print("  2. Database")
        print("  3. Exit")
        try:
            system_choice = int(input("Enter your choice: "))
        except:
            print("Please enter a valid input...\n")


        if system_choice is 1:
            bst = large_file_search.BinarySearchTree()
            csv_path = input("Enter the file name including extension: ")
            
            # Validate that the file is in the currenty working directory.
            if os.path.isfile(csv_path) is not True:
                print("No file found...\n")
                continue

            user_choice = 0

            while user_choice is not 9:
                print("Menu:")
                print("  1. Load Bids")
                print("  2. Display all Bids")
                print("  3. Find Bid")
                print("  4. Remove Bid")
                print("  5. Create File")
                print("  9. Exit")
                try:
                    user_choice = int(input("Enter your choice: "))
                except:
                    print("Please enter a valid input...\n")
                    continue
    
                if user_choice is 1:
                    bst.load_bids(csv_path)
                elif user_choice is 2:
                    node = bst.root
                    bst.display_all_bids(node)
                elif user_choice is 3:
                    try:
                        search_bid = int(input("Enter a Bid ID: "))
                    except:
                        print("Invalid input...\n")
                        continue
                    found_bid = bst.search_tree(search_bid)

                    if found_bid is not None:
                        parse_csv.print_bid(found_bid.bid)
                    else:
                        print("No bid found...")
                elif user_choice is 4:
                    try:
                        deleted_bid = int(input("Enter a Bid ID: "))
                    except:
                        print("Invalid input...\n")
                    bst.root = bst.delete_bid(bst.root, deleted_bid)
         
                elif user_choice is 5:
                    file_name = input("Enter a file name: ")
                    labels = ["Auction ID", "Auction Title", "Fund", "Auction Fee Total"]
                    
                    file_output.create_csv(file_name, bst, labels)
                    print("File successfully created...")


        elif system_choice is 2:
            start_kill_mongod.start_mongod()
            time.sleep(4)

            
            print("Exporting collection to CSV\n")
            mongo_file_export.export_collection("test")

            # Killing the MongoDB database
            print("Shutting down MongdoDB database...\n")
            start_kill_mongod.kill_mongod()
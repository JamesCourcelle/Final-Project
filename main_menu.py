import time
import os.path

from LocalFileProgram import file_output, large_file_search, parse_csv
from MongoFiles import mongo_crud, mongo_file_export, start_kill_mongod

if __name__ == "__main__":
    system_choice = 0

    while system_choice is not 9:
        print("Load from local file or from the database")
        print("  1. Local File")
        print("  2. Database")
        print("  9. Exit")
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

                    if bst.search_tree(deleted_bid) is None:
                        print("No bid found for deletion...")
                        continue

                    bst.root = bst.delete_bid(bst.root, deleted_bid)
                    print("Bid successfully deleted...")

                elif user_choice is 5:
                    file_name = input("Enter a file name: ")
                    labels = ["Auction ID", "Auction Title", "Fund", "Auction Fee Total"]

                    file_output.create_csv(file_name, bst, labels)
                    print("File successfully created...")

        elif system_choice is 2:
            start_kill_mongod.start_mongod()
            time.sleep(0.25)

            # Ensures index for AuctionID is created
            mongo_crud.create_index('localhost', 27017, 'CityData', 'bids', 'AuctionID')

            mongo_choice = 0

            while mongo_choice is not 9:
                print("Menu:")
                print("  1. Create Bid")
                print("  2. Find Bid")
                print("  3. Update Bid")
                print("  4. Remove Bid")
                print("  5. Export Database to CSV")
                print("  9. Exit")
                try:
                    mongo_choice = int(input("Enter your choice: "))
                except:
                    print("Please enter a valid input...\n")
                    continue

                if mongo_choice == 1:
                    mongo_crud.create_bid('localhost', 27017, 'CityData', 'bids')
                if mongo_choice == 2:
                    try:
                        search_bid = int(input("Enter a Bid ID: "))
                    except:
                        print("Invalid input...\n")
                        continue

                    found_bid = mongo_crud.find_bid('localhost', 27017, 'CityData', 'bids', search_bid)

                    # handles TypeError if found_bid returns None.
                    if found_bid is None:
                        continue

                    mongo_crud.print_results(found_bid)
                if mongo_choice == 3:
                    try:
                        search_bid = int(input("Enter a Bid ID: "))
                    except:
                        print("Invalid input...\n")
                        continue

                    found_bid = mongo_crud.find_bid('localhost', 27017, 'CityData', 'bids', search_bid)

                    # handles TypeError if found_bid returns None.
                    if found_bid is None:
                        continue

                    mongo_crud.update_bid('localhost', 27017, 'CityData', 'bids', search_bid)
                    print("Update Successful...")
                if mongo_choice == 4:
                    try:
                        search_bid = int(input("Enter a Bid ID: "))
                    except:
                        print("Invalid input...\n")
                        continue

                    found_bid = mongo_crud.find_bid('localhost', 27017, 'CityData', 'bids', search_bid)

                    # handles TypeError if found_bid returns None.
                    if found_bid is None:
                        continue

                    mongo_crud.delete_bid('localhost', 27017, 'CityData', 'bids', search_bid)

                if mongo_choice == 5:
                    # Exports the database to a CSV file located in 'C:\data\'
                    new_file_name = input("Enter a file name fore exporting: ")
                    mongo_file_export.export_collection(new_file_name)
                    time.sleep(2)

            # Killing the MongoDB database
            print("Shutting down MongdoDB database...\n")
            start_kill_mongod.kill_mongod()
            print("")

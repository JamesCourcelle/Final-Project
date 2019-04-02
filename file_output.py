import csv
import large_file_search
import parse_csv

# Assistance with building function to create CSV files from https://pythonspot.com/files-spreadsheets-csv/

# code takes in a file name, binary search tree, and labels when called. 
def create_csv(file_name, source_code, labels):
    with open(file_name + '.csv', 'w', newline = '') as csv_file:
        file_writer = csv.writer(csv_file, delimiter = ',',
                                 quotechar = '|', quoting = csv.QUOTE_MINIMAL)
        file_writer.writerow(labels)

        node = source_code.root

        def export_bids(node):
            if node is not None:
                export_bids(node.left)
                file_writer.writerow([node.bid.bid_id, node.bid.title, node.bid.fund, node.bid.amount])
                export_bids(node.right)
        
        export_bids(node)

if __name__ == "__main__":
    bst = large_file_search.BinarySearchTree()
    csv_path = 'eBid_Monthly_Sales.csv'
    bst.load_bids(csv_path)
    labels = ["Auction ID", "Auction Title", "Fund", "Auction Fee Total"]

    create_csv("test.csv", bst, labels)

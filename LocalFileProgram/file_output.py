import csv


# Assistance with building function to create CSV files from https://pythonspot.com/files-spreadsheets-csv/

# code takes in a file name, binary search tree, and labels when called. Uses Python's csv module
# to open and close the the file writer. The program takes a file name, a BinarySearchTree and the labels
# for each column in the outputted file. 
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


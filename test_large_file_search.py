import large_file_search
import parse_csv
import unittest
import random

class TestLargeFile(unittest.TestCase):
    # function to ensure the number of nodes match the number of entries in the CSV file.
    # The count for a node occurs in the create_tree function in the BinarySearchTree. 
    # As long as the try block in the function is successful, the count will match the
    # count pulled from the CSV file.
    def test_entry_count(self):
        print("Starting test_entry_count test...")
        bst = large_file_search.BinarySearchTree()
        csv_path = 'eBid_Monthly_Sales.csv'
        
        bst.load_bids(csv_path)
        list_bids = parse_csv.open_file(csv_path)
        
        self.assertEqual(bst.node_count, len(list_bids))
        
        # clearing memory
        del bst
        del list_bids
        del csv_path

    def test_delete(self):
        print("starting test_delete test...")
        bst = large_file_search.BinarySearchTree()
        csv_path = 'eBid_Monthly_Sales.csv'
        bst.load_bids(csv_path)

        current_node = bst.root
        test_nodes = [79519, 98912, 98854, 98479, 97236, 86371, 84540] # First value is lowest ID #, second is highest ID #, additional values are randomly taken

        current_bid = bst.search_tree(98854)
        print(current_bid.left.bid.bid_id, current_bid.right.bid.bid_id)            

if __name__ == '__main__':
    unittest.main()

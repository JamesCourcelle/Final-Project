Changelog

## 3/14/2018:
Code was previously written that was not intiialy put into a repository.
For this reason, the initial push is a larger code base than I would normally push at once.
It is also important to note the lack of testing and any current plan for the project.
My next steps will be to write the appropriate unit tests for the current code.
From there, I will take a TDD approach to development.

## 04/01/2019 - 04/02/2019
Completed the addition of some unit tests to validate deletion and node count. Completed the addition of a deletion feature using two functions, check_bid_for_deletion and delete_bid. This function use a recursive algorithm to not only delete the bid object, but to set the left and right pointers appropriately.

## 04/03/2019
Overhauled the deletion function due to errors with completing the delete operation. Rewrote code to be simplier and confirmed that it behaves as intended. Added basic file output feature that outputs the BST in its current state and is formated to only include the four fields passed in.

# TODO
Complete a basic MongoDB integration with CRUD operations available.

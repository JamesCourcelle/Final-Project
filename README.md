# Final-Project
For my capstone at SNHU for my CS degree I will be converting a previous project from C++ to python.
The project takes in two csv files that are sorted and then placed into a binary search tree data structure.
From there, the user can display each entry of data sorted by ID number in ascending order. 
The user is also able to search for one entry with by entering the ID number associated with the entry.

## Dependencies
Project is currently using Python 3.7.0 32-bit

Project is currently using MongoDB server version: 4.0.8

Project is currently using MongoDB shell version v4.0.8

Project uses the current version of PyMonogo. To install PyMongo, open a Command Prompt and enter the following line
```python -m pip install pymongo```

MUST BE USING WINDOWS OS

## Installation and setup for MongoDB
#IMPORTANT!
in order for this program to work correctly you must install the 64-bit version of MongoDB to the C:\Program Files\ (default directory) directory. This program will not work otherwise.

MongoDB can be downloaded and installed from [here](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/#install-mdb-edition)

Follow the instructions to download the MongoDB Community Edition.

The current version of Python code starts the mongod.exe when you launch the main_menu.py. The main_menu.py also kills the mongod.exe server at the exiting of the program.

### mongoimport
The only action needed by the user to create the database and import the eBid_Monthly_Sales.csv into the database is to move the csv file to the appropriate directory. The program handles creating the directory and the database without user input.

USER MUST MOVE eBid_Monthly_Sales.csv TO ```C:\Program Files\MongoDB\Server\4.0\bin``` (This location only exists after MongoDB is installed to the proper directory)

## mongoexport
The mongoexport is handled by the Python program and does not require the user to interact with the command line.
* When the database is created the C:\data\ directory is created. The export is dumped here.


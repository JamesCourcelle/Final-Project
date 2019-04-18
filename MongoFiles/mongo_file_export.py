import subprocess
import os



def export_collection(file_name):
    # change the path to point to where mongoexport.exe is located.
    path = ("C:\\Program Files\\MongoDB\\Server\\4.0\\bin\\")
    os.chdir(path)

    # Set the file name passed on what the user passes in.
    file = "C:\\data\\" + file_name + ".csv"
    command = ("mongoexport --db CityData --collection bids --type=csv --fields AuctionID,AuctionTitle,Fund,AuctionFeeTotal --out %s"
               % (file))

    subprocess.run(command, creationflags = subprocess.CREATE_NEW_CONSOLE)

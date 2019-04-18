from pathlib import Path
import subprocess


def start_mongod():
    # Code below starts up MongoDB database for the user.
    try:
        path_loop = True
        while path_loop:
            print("Is your mongod.exe C:\\Program Files\\MongoDB\\Server\\4.0\\bin\\mongod.exe?")
            default_path = input("Y/N: ")

            if default_path is 'Y' or default_path is 'y':
                exe_location = Path("C:/Program Files/MongoDB/Server/4.0/bin/mongod.exe")
                path_loop = False
            else:
                if default_path is 'N' or default_path is 'n':
                    print("Enter the location of mongod.exe: (use '/'not '\\')")
                    exe_location = Path(input())
                    path_loop = False
                else:
                    print("Invalid input...")

        directory_loop = True
        while directory_loop:
            print("Is the database directory located at C:\\data\\db?")
            default_directory = input("Y/N: ")

            if default_directory is 'Y' or default_directory is 'y':
                directory_location = Path("C:/data/db")
                directory_loop = False
            else:
                if default_directory is 'N' or 'n':
                    print("Enter the database directory location: (use '/ 'not '\\')")
                    directory_location = Path(input())
                    directory_loop = False
                else:
                    print("Invalid input...")

        command = ("{0} --dbpath={1}".format(exe_location, directory_location))

        # Creating a process that allows other processes to continue while this runs. 
        # mongod.exe runs in a seperate console.
        subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)



    except:
        print("Database failed to start...")


# Function to kill the mongod.exe and stop the MongoDB batabase
def kill_mongod():
    subprocess.run("taskkill /f /im mongod.exe")

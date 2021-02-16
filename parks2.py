#Python database project
#AnElizabeth Henry & Jacob Smith
import csv
import os.path
import re
import sys
from pathlib import Path
import configparser
record_size = 152

def main():
    DbCheck = False #this is a boolean varible that checks if a database is open or not
    DbNOTOPEN = True #this boolean is variable that is strictly for preventing the creation of new database while one is currenlty open
    DbCREATED = False
    loop = True
    while loop:
        menu_options()
        choice = input("\nYour response here: ")

        if choice == '1':
            if(DbNOTOPEN):                                                     #if the user chooses the 1 menu option
                file = input ("\nEnter in the database prefix you would like to create: ") #Prompt the user to say what file they are looking for
                filename = file + '.csv'
                print("You are creating a database called " + file)
                creatDB(filename)
                DbCREATED = True
            else:
                print("A Database is currently open. Close it to create another one.")

        elif choice == '2':
            if(DbCREATED):                                                   #if the user chooses the 2 menu option
                DbCheck = True
                DbNOTOPEN = False
                print("You have picked option 2: Open database")
                file = input("Please enter the prefix of a file you are wanting to open: ")
                if not os.path.isfile(file + ".data" and file + ".config"):
                    print(file,"not found.")
                    exit()                                                          #NEEDS TO BE WORKED ON TO NOT EXIT THE PROGRAM
                else:
                    print("data base is " + file + ".data and " + file + ".config found")
                    dfile = file + '.data'                                          #save the file name with.data to dfile
                    cfile = file + '.config'                                        #save the file name with .config to cfile
                    data = openCloseDB(dfile, 'open')                               #save the return files variable to data variable
                    config = openCloseDB(cfile, 'open')                             #save the return files variable to config varaible
                    if data == 'opened':                                            #if data equals to opened
                        dataStore('.data',data)
                    else:                                                           #else meaning if config equals opened
                        dataStore('.data',data)
                    if config == 'closed':                                          #if config equals closed
                        dataStore('.config',config)
                    else:                                                           #else meaning if config equals opened
                        dataStore('.config',config)
            else:
                print("No Database has been created or is currently open!")
        elif choice == '3':                                                   #if the user chooses the 3 menu option
            if(DbCheck):
                print("Option 3")
                file = input('Please enter the file perfix you are wanting to close: ')
                end = input('Please enter either .data or .config on which you would like to close: ')

                if end == '.data':                                                  #if the end from the user's input == .data
                    f = file + '.data'                                              #make variabel F = file.data
                    data = openCloseDB(f,'close')                                   #opens the function openClosedDB to close the certain .data file
                    dataStore('.data', data)
                    DbNOTOPEN = False
                    DbCheck = False
                    DbCREATED = False
                elif end == '.config':                                              #if the end from the user's input == .config
                    c = file + '.config'                                            #make the variable C = file.config
                    config = openCloseDB(c, 'close')                                #opens the function openCloseDB to close the certain .config file
                    dataStore('.config', config)
                    DbNOTOPEN = False
                    DbCheck = False
                    DbCREATED = False
                else:
                    print('Sorry that is not a file..')                         #if the file isn't available then print the statement
            else:
                print("No Database is currently open")
        elif choice == '4':                                                     #if the user chooses the 4 menu option
            if(DbCheck):
                print("Option 4")
                f = open("Parks.data", 'r')
                print("\n------------- Running ID Search ------------\n")
                ID = input ("\n Enter the ID for the Record you would like to pull up: ")
                Record, Middle = binarySearch(f, ID)
                if Record != -1:
                    print("ID ",ID,"found at Record",Middle)
                    print("Record", middle,":", Record,"\n")
                else:
                    print("ID",ID,"not found in our records\n")
            else:
                print("No Database is currently open")

        elif choice == '5':                                                 #if the user chooses the 5 menu option
            if(DbCheck):
                print("Option 5")
                print("\n\n------------- Testing Update ------------\n\n")
                update()
            else:
                    print("No Database is currently open")
        elif choice == '6':                                                     #if the user chooses the 6 menu option
            if(DbCheck):
                print("Option 6")
                with open('Parks.data', 'r') as parkData:                           #opens the parks.data file
                    count = 0                                                       #sets the count to 0
                    for line in parkData:                                           #for loop that will loop through the lines in parkData
                        count += 1                                                  #adds one to the value of count during every loop
                        if count %2 == 1:                                           #if count module 2 equals 1
                            print (line)                                            #print the line then it will skip the blanks because they will equal 0
                        if count == 20:                                             #if the count equals 20 then break because we will have the 10 records we want.
                            break
            else:
                print("No Database is currently open")
        elif choice == '7':                                                     #if the user chooses the 7 menu option
            if(DbCheck):
                print("Option 7")
                insert()
            else:
                print("No Database is currently open")
        elif choice == '8':                                                     #if the user chooses the 8 menu option
            if(DbCheck):
                print("Option 8")
                delete()
            else:
                print("No Database is currently open")
        elif choice == '9':
            print('You are exiting the program.. Good Bye!')
            loop = False
        else:                                                                   #if the user chooses a number that isn't a menu option
            print("sorry that wasn't an option.. Good Bye!")
            loop = False
    exit()

def dataStore(filename, store):
    if filename == '.data':
        print(store)
    elif filename == '.config':
        print(store)
    else:
        print('sorry this file isn\'t in our system')

def menu_options():
    #menu of operations
    print("\nPlease pick on of the following to continue: ")
    #1.create new database
    print("1. Create new database")
    #2. Open database
    print("2. Open database")
    #3.close database
    print("3. Close database")
    #4.display record
    print("4. Display record")
    #5.update record
    print("5. Update record")
    #6.create report
    print("6. Create report")
    #7.add a record
    print("7. Add a record")
    #8.delete a record
    print("8. Delete a record")

    print("9: exit")

def update():
    ID = input('What is the ID of the record you would like to update? ')
    f = open("Parks.data", 'r+')
    Record, Middle = binarySearch(f, ID)
    if Record != -1:
        print("ID ",ID,"found at Record",Middle)
        print("Record", middle,":", Record,"\n")
        print('What is field would you like to update?')
        print('1. Region')
        print('2. State')
        print('3. Code')
        print('4. Visitors')
        print('5. Type')
        print('6. Name')
        command = input('Enter in the number that corresponds with the field you want to update: ')

        global State
        global Region
        global Type
        global Name
        global Code
        global Visitors
        f.seek(record_size * middle)
        field = Record.split()
        ID = field[0]
        Region = field[1]
        State = field[2]
        Code = field[3]
        Visitors = field[4]
        Type = field[5]
        Name = field[6]

        if command == '1':
            print('Region')
            new = input('What are you wanting to change it to? ')
            total = len(new)
            if total > 2:
                new =new[0:2]
            Region = Region.replace(Region,new)
            print('{0:7s} {1:2s} {2:2s} {3:4s} {6:10s} {5:37s} {4:83s}'.format(ID, Region,State,Code,Name,Type,Visitors), file=f)
        elif command == '2':
            print('State')
            new = input('What are you wanting to change it to? ')
            total = len(new)
            if total > 2:
                new =new[0:2]
            State = State.replace(State,new)
            print('{0:7s} {1:2s} {2:2s} {3:4s} {6:10s} {5:37s} {4:83s}'.format(ID, Region,State,Code,Name,Type,Visitors), file=f)
        elif command == '3':
            print('Code')
            new = input('What are you wanting to change it to? ')
            total = len(new)
            if total > 4:
                new =new[0:4]
            Code = Code.replace(Code,new)
            print('{0:7s} {1:2s} {2:2s} {3:4s} {6:10s} {5:37s} {4:83s}'.format(ID, Region,State,Code,Name,Type,Visitors), file=f)
        elif command == '4':
            print('Visitors')
            new = input('What are you wanting to change it to? ')
            new =new.replace(' ','_')
            total = len(new)
            if total > 10:
                new =new[0:10]
            Visitors = Visitors.replace(Visitors,new)
            print('{0:7s} {1:2s} {2:2s} {3:4s} {6:10s} {5:37s} {4:83s}'.format(ID, Region,State,Code,Name,Type,Visitors), file=f)
        elif command == '5':
            print('Type')
            new = input('What are you wanting to change it to? ')
            new =new.replace(' ','_')
            total = len(new)
            if total > 37:
                new =new[0:37]
            Type = Type.replace(Type,new)
            print('{0:7s} {1:2s} {2:2s} {3:4s} {6:10s} {5:37s} {4:83s}'.format(ID, Region,State,Code,Name,Type,Visitors), file=f)
        elif command == '6':
            print('Name')
            new = input('What are you wanting to change it to? ')
            new =new.replace(' ','_')
            total = len(new)
            if total > 83:
                new =new[0:83]
            Name = Name.replace(Name,new)
            print('{0:7s} {1:2s} {2:2s} {3:4s} {6:10s} {5:37s} {4:83s}'.format(ID, Region,State,Code,Name,Type,Visitors), file=f)
        else:
            print('Sorry that is not an option!')
def creatDB(filename):
    rec_total = 0
    blank = 0
    if not os.path.isfile(filename):                                            #checks to see if the filename that the user typed in is real or not
        print(filename,"not found")
        exit()                                                                  #exits the program if the file doesn't exist
    else:
        parksCsv = open(filename, 'r')                                          #opens the parks.csv file in read mode
        datafile = open('Parks.data', 'w+')                                     #opens/creates a new file called parks.data in append/read mode
        configfile = open('Parks.config','w')                                   #opens/creates a new file called parks.config in writing/read mode
        reader = csv.reader(parksCsv,delimiter=',')                             #reads in the parks.csv file to
        fields = next(reader)                                                   #skips the first line and set that line as the fields
        for fields in reader:                                                   #loop through the csv file
        #sets the fields to their corresponding row
            ID = fields[0]
            Region = fields[1]
            State = fields[2]
            Code = fields[3]
            Name = fields[4]
            Type = fields[5]
            Visitors = fields[6]
            Name = Name.replace(" ","_")
            Type = Type.replace(" ", "_")

            #This prints the fields in fixed lengths
            print('{0:7s} {1:2s} {2:2s} {3:4s} {6:10s} {5:37} {4:83s}'.format(ID, Region,State,Code,Name,Type,Visitors),file=datafile)

            #prints the blank line inbetween every row in the data file
            print('xxxxxxx xx xx xxxx xxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' ,file=datafile)
            blank = blank + 1
            rec_total = rec_total + 1                                           #keeping track of the total number of records in the file
        total = rec_total + blank
        config = configparser.ConfigParser()                                    #sets Config to the config parser library
        config.add_section('Records')                                           #adds a section to the config file called Records
        config.set('Records','num_records',str(total))                          #adds to the settings Records the variable num_records and sets that to the total which is converted to string
        config.set('Records','record_size','152')                               #adds to the settings Records the variable record_size and sets that to 152
        config.write(configfile)  #sys.stdout                                   #opens the configfile in write mode so that it can write the config settings
        configfile.close()                                                      #closes the config file

def openCloseDB(file,command):
    global dataf
    global num_records
    dataf = open(file,'r')                                                      #opening the file in read mode and saving it to dataf
    openClose = command
    if command == 'open':                                                       #if the command equals open
        files = 'opened'                                                        #sets the file as opened so it can be returned once the function is completed
        if file == 'Parks.config':                                              #if the file is Parks.config
            readConfig = configparser.ConfigParser()                            #sets readConfig to the config parser library
            readConfig.read_file(dataf)                                         #reads the park.config file
            num_records = readConfig.getint("Records","num_records")            #sets num_records to the int thats in section Records which is storing the num_records
            record_size = readConfig.getint("Records","record_size")            #sets record_size to the int thats in section Records which is storing the record_size
            dataf.close()                                                       # closed the config file
            files = 'closed'                                                    #sets the file as closed so it can be returned once the function is completed
        else:
            files = 'opened'                                                    #sets the file as opened so it can be returned once the function is completed
    elif command == 'close':
        dataf.close()                                                           #Close the file
        files = 'closed'                                                        #sets the file as closed so it can be returned once the function is completed
    return files                                                                #return the variable files

def insert():
    global State
    global Region
    global Type
    global Name
    global Code
    global Visitors
    newRecordID = input('What is the ID number: ')

    f = open("Parks.data", 'r+')
    Record, Middle = binarySearch(f, newRecordID)
    if Record != -1:
        print("ID",newRecord,"Already exists\n")
    else:
        newRegion = input('What is the Region ')
        regionTotal = len(newRegion)
        if regionTotal > 2:
            newRegion = newRegion[0:2]

        newState = input('What is the State ')
        stateTotal = len(newState)
        if stateTotal > 2:
            newState = newState[0:2]

        newCode = input('What is the Code ')
        codeTotal = len(newCode)
        if codeTotal > 4:
            newCode = newCode[0:4]

        newVisitors = input('What is the Visitors ')
        stateTotal = len(newVisitors)
        if stateTotal > 10:
            newVisitors = newVisitors[0:10]

        newType = input('What is the Type ')
        typeTotal = len(newType)
        if typeTotal > 37:
            newType = newType[0:37]

        newName = input('What is the Name ')
        nameTotal = len(newName)
        if nameTotal > 83:
            newName = newName[0:83]

        newRecord = newRecordID +' ' + newRegion +' ' + newState + ' ' + newCode +' ' + newVisitors +' ' + newType +' ' + newName
        field = newRecord.split()
        ID = field[0]
        Region = field[1]
        State = field[2]
        Code = field[3]
        Visitors = field[4]
        Type = field[5]
        Name = field[6]
        print("Record Inserted")
        f.seek(record_size* (middle-1))
        Region = Region.replace(Region,newRegion)
        State = State.replace(State,newState)
        Code = Code.replace(Code,newCode)
        Visitors = Visitors.replace(Visitors,newVisitors)
        Type = Type.replace(Type,newType)
        Name = Name.replace(Name,newName)
        print('{0:7s} {1:2s} {2:2s} {3:4s} {6:10s} {5:37s} {4:83s}'.format(ID, Region,State,Code,Name,Type,Visitors), file=f)

def delete():
    ID = input('What is the ID of the record you would like to delete? ')
    f = open("Parks.data", 'r+')
    Record, Middle = binarySearch(f, ID)
    if Record != -1:
        print("Deleted Record")
        f.seek(record_size* middle)
        f.write('xxxxxxx xx xx xxxx xxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        f.close()
    else:
        print("ID",ID,"not found in our records\n")

# Get record number n (Records numbered from 0 to NUM_RECORDS-1)
def getRecord(f, recordNum):
    record = ""
    global num_records
    global record_size
    num_records = 748
    Success = False
    if recordNum >= 0 and recordNum < num_records:
        f.seek(0,0)
        f.seek(record_size * recordNum)                                         #offset from the beginning of the file
        record = f.readline()
        Success = True
    return " ".join(record.split()), Success

def binarySearch(f, name):
    global middle
    global record_size,num_records
    count = 0
    low = 0
    num_records = 748
    high=num_records-1
    Found = False
    Success = False

    while not Found and high >= low and count != 12:
        middle = (low+high) // 2
        record, Success = getRecord(f, middle)
        middleid = record.split()
        if(middleid[0] == 'xxxxxxx' and  num_records == middle+2):
            return -1, middle
        middleidnum = middleid[0]
        while middleidnum == 'xxxxxxx':
            middle += 1
            count += 1
            record, Success = getRecord(f, middle)
            middleid = record.split()
            middleidnum = middleid[0]
            if count == 12:
                return -1, middle
        if middleidnum == name:
            Found = True
            print("Found")
        if int(middleidnum) < int(name):
            low = middle+1
        if int(middleidnum) > int(name):
            high = middle-1

    if(Found == True):
        return record, middle                                                   # the record number of the record
    else:
        return -1, middle
main()                                                                          #runs the program all together

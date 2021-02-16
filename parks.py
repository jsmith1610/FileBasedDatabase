#Python database project
#AnElizabeth Henry and Jacob Smith
import csv
import os.path
import sys
num_records = 748
record_size = 152

def main():
    loop = True
    while loop:
        rec_total = 0
        blank = 0
        #menu of operations
        print("Please pick on of the following to continue: ")
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
        choice = input("\nYour response here: ")

        if choice == '1':                                                   #if the user chooses the 1 menu option
            filename = input ("\nEnter in the database name you would like to create: ") #Prompt the user to say what file they are looking for
            print("You are looking for " + filename)

            if not os.path.isfile(filename):                                #checks to see if the filename that the user typed in is real or not
                print(filename,"not found")
                exit()                                                      #exits the program if the file doesn't exist
            else:
                parksCsv = open(filename, 'r')                      #opens the parks.csv file in read mode
                datafile = open('Parks.data', 'w+')             #opens/creates a new file called parks.data in append/read mode
                configfile = open('Parks.config','w+')       #opens/creates a new file called parks.config in writing/read mode
                reader = csv.reader(parksCsv,delimiter=',')    #reads in the parks.csv file to
                fields = next(reader)                           #skips the first line and set that line as the fields
                for fields in reader:                           #loop through the csv file
                #sets the fields to their corresponding row
                    ID = fields[0]
                    Region = fields[1]
                    State = fields[2]
                    Code = fields[3]
                    Visitors = fields[4]
                    Type = fields[5]
                    Name = fields[6]

                    #This prints the fields in fixed lengths
                    print('{0:7s} {1:2s} {2:2s} {3:4s} {6:10s} {5:37} {4:83s}'.format(ID, Region,State,Code,Visitors,Type,Name),file=datafile)

                    #prints the blank line inbetween every row in the data file
                    print('                                                                                                                                                       ',file=datafile)
                    blank = blank + 1
                    rec_total = rec_total + 1                           #keeping track of the total number of records in the file
                writeConfig = configfile.write("Number of Records: " + str(rec_total+blank) +'\n')          #prints out the total of record numbers to the config file
                writeConfig = configfile.write("Record Size: 152")
                # datafile.close()
                # if datafile.close():
                #     print('closed')

        elif choice == '2':         #if the user chooses the 2 menu option
            print("Option 2")
        elif choice == '3':         #if the user chooses the 3 menu option
            print("Option 3")
        elif choice == '4':         #if the user chooses the 4 menu option
            print("Option 4")
            ID = input ("\n Enter the ID for the Record you would like to pull up: ")
            f = open("Parks.data", 'r')
            #record_num = int(ID)
            # Success = False
            # Record, Success  = getRecord(f, (record_num - 1))
            # if Success:
            #     print("Record ",record_num,": ",Record,"\n")
            # else:
            #     print("Could not get the record")
            Record, Middle = binarySearch(f, ID)
            binarySearch(f, ID)
            if Record is not -1:
                print("ID ",ID,"found at Record",Middle)
                print("Record", middle,":", Record,"\n")
            else:
                print("ID",ID,"not found in our records\n")
        elif choice == '5':         #if the user chooses the 5 menu option
            print("Option 5")
        elif choice == '6':         #if the user chooses the 6 menu option
            print("Option 6")
            with open('Parks.data', 'r') as parkData:
                count = 0
                for line in parkData:
                    count +=1
                    if count %2 == 1:
                        print(line)
                    if count == 20:
                        break
        elif choice == '7':         #if the user chooses the 7 menu option
            print("Option 7")
        elif choice == '8':         #if the user chooses the 8 menu option
            print("Option 8")
        elif choice == '9':
            print('You are exiting the program.. GoodBye!')
            loop = False
        else:                                                                       #if the user chooses a number that isn't a menu option
            print("sorry that wasn't an option.. GoodBye!")
            loop = False
    exit()

# Get record number n (Records numbered from 0 to NUM_RECORDS-1)
def getRecord(f, recordNum):
    with open("Parks.config") as readConfig:
        recordStr = readConfig.readline()
    num_records = int(recordStr)
    record = ""
    global record_size
    Success = False
    if recordNum >= 0 and recordNum < num_records:
        f.seek(0,0)
        f.seek(record_size * recordNum) #offset from the beginning of the file
        record = f.readline()
        Success = True
	#f.close()
    return " ".join(record.split()), Success

def binarySearch(f, name):
    # with open("Parks.config") as readConfig:
    #     recordStr = readConfig.readline()
    # num_records = int(recordStr)
    # recordID = int(name)
    global middle
    global num_records, record_size
    low=0
    high=num_records-1
    Found = False
    Success = False
    while not Found and high >= low:
        middle = (low+high) // 2
        #middle = low + (high-low) // 2
        record, Success = getRecord(f, (middle - 1))
        middleid = record.split()
        middleidnum = middleid[0]
        if middleidnum == name:
            Found = True
        # if middleidnum < name:
        #     print("Low: ", low)
        #     low = middle+1
        # elif middleidnum > name:
        #     print("High: ", high)
        #     high = middle-1

    if(Found == True):
        return record, middle # the record number of the record
    else:
        return -1, middle
#runs the program all together
main()

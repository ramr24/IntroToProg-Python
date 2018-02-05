#Assignment_04
'''
Create a new program that asks the user for the name of a household item, and then asks for its
estimated value. Store, both pieces of data in a text file called, HomeInventory.txt. Ask the user
for new entries and stores them in the 2-dimensional Tuple. Ask the user, when the program exits,
if they would like to save/add the data to a text file called, HomeInventory.txt.
'''

#Opens file to read & reads already written text from text file
objFile = open("C:\_PythonClass\Assignment_04\HomeInventory.txt", "r")
read = objFile.readline()
tRow = (read.split(",")[0].strip(), read.split(",")[1].strip())
tTable = tRow,

#For loop adds new rows to the table
for l in objFile:
    read = l
    tRow = (read.split(",")[0].strip(), read.split(",")[1].strip())
    tTable += tRow,
print(tTable)
#Closes file
objFile.close()

#While loop to gather user input
while(True):
    item = input("Enter the name of a household item: ")
    value = float(input("Enter the value of the household item: $"))
    tRow = (item, value)
    tTable += tRow,
    #User continues or exits the program
    ex = input("To continue (press 'y') or to exit (press 'n'): ")
    if(ex.lower() == "n"):
        break
    else:
        continue

#User saves the data
save = input("Would you like to the save your data? (y/n): ")
if (save.lower() == "y"):
    #Opens file to write
    objFile = open("C:\_PythonClass\Assignment_04\HomeInventory.txt", "w")
    #For loop to write in text file
    for row in tTable:
        objFile.write(str(row[0]) + ", " + str(row[1]) + "\n")
    #Closes file
    objFile.close()
    print("The data was saved!")
else:
    print("The data was not saved!")
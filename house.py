#Assignment_03
'''
Create a new program that asks the user for the 
name of a household item, and then asks for its 
estimated value. Store, both pieces of data in a 
text file called, HomeInventory.txt.
'''

#Opens file
objFile = open("C:\_PythonClass\Assignment_03\HomeInventory.txt", "w")

#While loop
while(True):
    item = input("Enter the name of a household item: ")
    value = float(input("Enter the value of the household item: $"))

    #Writes item and value into the HomeInventory.txt file
    objFile.write(item + ": $" + str(value) + "\n")

    #User continues or exits the program
    ex = input("Press 'Enter' to continue or type 'Exit' to quit this program: ")
    if(ex.lower() == "exit"):
        break
    else:
        continue

#Closes file
objFile.close()

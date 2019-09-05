#Task 18
#Compulsory Task

#This program reads the data from the text file called DOB.txt and prints it out in two different sections i.e "Names" and "Birth date"
File = open('DOB.txt','r+')
#AllContents = File.read()   #read everyting in File DOB
Names = []       #This is a list that will store all the names read from the DOB text file
DOB = []         #This is a list that will store all the DOB's read from the DOB text file
n=1
m=1
for line in File:
    Line = line.strip()   # strip any white spaces
    Line = line.split()     #split the line into pieces
    #each line is split into 5 pieces - the first two pieces will be the name and surname while the 3rd,4th and 5th pieces will be the Birth Date
    Names.append(Line[0] + " " + Line[1])  #Add the first 2 pieces into the Names list.
    DOB.append(Line[2] + " " + Line[3] + " " + Line[4])  #Add the last 3 pieces into the DOB list.

print("Names:")
for i in Names:     #print each name in the list  on a seperate line
   print("\t" + str(n) + ".   " + i)   #i is the same as Names[i] in an array.
   n+=1


print("\nBirth Date:\n")
#m=1
for j in DOB:
    print("\t" + str(m) + ".   " + j)
    m+=1

    

File.close()

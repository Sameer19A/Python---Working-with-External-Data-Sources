#Task 20
#Compulsory Task
#This program reads each line in a text file and computes the answer to some operation on a list of numbers.
#We assume that the only operations given in the input file are min, max and avg, and that the operation is always followed by a list of comma separated integers.

InputFile = open('input.txt','r')
OutputFile = open('output.txt','w')
NumberList = []  #empty list to store the numbers given in the input file
Operation = []   # list that will keep the operations that are given in the input file - use to compare and complete the operation 
NumberString = ""  #empty string/tuple used to store the converted list so it can be printed
for line in InputFile:
    Line = line.strip()     #strip white spaces
    LineColon = Line.replace(':',',')  #line has colon, therefore Replace the colon in the line with a comma
    LineComma = LineColon.split(',')   #line has only commas now, so split the line into pieces using the comma ',' as a delimeter
    #print(LineComma)
    
    #Now add the operation part to a list . The operation part of the line is given in the first index of the list, index 0. 
    Operation.append(LineComma[0])   #add the operation part of the line to a list.
    #print(len(LineComma))
    #Now add the numbers in the line to the NumbersList
    for i in range(1,len(LineComma)):  #loop starts at index 1 of linecomma because at index 0 is the operation type
        NumberList.append(LineComma[i])        #add the numbers in all lines to NumberList
 
    #"Now we have to calculate the min, max and average for all the numbers in the LineCol"
    #"Determining the Operation to perform: Min,Max,Avg"
    if LineComma[0].lower() == "min":
        NumberList = sorted(NumberList)
        MinNum = NumberList[0]   # after sorting the min of the integers will be at index 0 in the list
        MinNum = str(MinNum)
        MinNum = MinNum.strip()
       # print("The min of [",NumberString,"] is ",str(MinNum)+ ".")

    elif LineComma[0].lower() == "max":
        NumberList = sorted(NumberList)
        MaxNum = NumberList[-1]   # after sorting the max of the integers will be at the last integer, thus at index [-1]
       # print("The max of [",NumberString,"] is ",str(MaxNum)+ ".")
        
    elif LineComma[0].lower() == "avg":
        NumberList = sorted(NumberList)
        Sum = 0
        AvgNum = 0
        for i in range(1,len(LineComma)):
            Sum = Sum + int(LineComma[i])
        AvgNum = Sum/(len(LineComma)-1) #subtract one from the length of LineComma because the len function will count the operation type at index 0 as 1 and thus include it 
       # print("The avg of [",NumberString,"] is ",str(AvgNum)+ ".")

###converting the list to string one list item/index at a time.
for i in range(1,len(LineComma)):
    NumberString = NumberString + "," + LineComma[i]

NumberString = NumberString[1:len(NumberList)]  #use len(NumberList to include the whole list including any spaces or commas between integers)
NumberString = NumberString.strip()

WriteMin = "The min of [" + NumberString + "] is " + str(MinNum)+ "."
WriteMax = "The max of [" + NumberString + "] is " + str(MaxNum)+ "."
WriteAvg = "The avg of [" + NumberString + "] is " + str(AvgNum)+ "."
OutputFile.write(str(WriteMin) + "\n")
OutputFile.write(str(WriteMax) + "\n")
OutputFile.write(str(WriteAvg) + "\n")


InputFile.close()
OutputFile.close()

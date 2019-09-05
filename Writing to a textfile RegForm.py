#Task 19
#Compulsory Task
#This program enters the ID numbers of students entered by the user and writes it to a textfile
NumStudents = int(input("How many students are registering?\t"))

AttendanceReg = open('RegForm.txt','w')   #open the RegForm textfile to store the ID numbers
for i in range(0,NumStudents):
    IDnum = input("Please enter your ID number:\t")
    AttendanceReg.write(IDnum+"\n") 
    
    
AttendanceReg.close()    #close the file


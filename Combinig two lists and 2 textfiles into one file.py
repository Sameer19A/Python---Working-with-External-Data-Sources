#Task 19
#Optional Task
#This programs takes the numbers from two texfiles and then combines them into one file and sorts them

Numbers1 = open('numbers1.txt','w')
Numbers2 = open('numbers2.txt','w')
allNumbers=open('allNumbers.txt','w')
list1 = []  #list to temporarily store numbers1 integers
list2 = []  #list to temporarily store numbers2 integers
Listall = [] #list that holds both list values
NumInt = int(input("How many integers would you like to enter into list 1?\t"))
for i in range(0,NumInt):
    n = int(input("Please enter an integer?\t"))  # not casting to int because we not doing calculations with the integer
    list1.append(n)
    Listall.append(n)
list1 = sorted(list1)
for i in list1:
    Numbers1.write(str(i) + "\n")  #write the sorted integers in list1 to the text file called Numbers1
    

print(sorted(list1))
    
NumInt2 = int(input("\nHow many integers would you like to enter into list 2?\t"))
for j in range(0,NumInt2):
    m = int(input("Please enter an integer?\t"))
    list2.append(m)
    Listall.append(m)
list2 = sorted(list2)
for i in list2:
    Numbers2.write(str(i) + "\n")  #write the sorted integers in list1 to the text file called Numbers2

print(sorted(list2))

Listall = sorted(Listall)   # sort the third list
print("")
print(Listall)
for k in Listall:
    allNumbers.write(str(k) + "\n")  #write the sorted integers in list1 to the text file called Numbers2

Numbers1.close()
Numbers2.close()
allNumbers.close()

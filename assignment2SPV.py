def isSubsetOf( setA, setB ):
	for e in setB :
		if e not in setA :
			return False
	return True 

size = int(input("Enter size of set 1: ")) 
size1 = int(input("Enter size of set 2: ")) 
print("\nFor set 1:") 
list1 = []
for i in range(size): 
	element = int(input("Enter unique element: ")) 
	list1.append(element)
print("set 1 =", list1) 

print("\nFor set 2:") 
list2=[] 
for i in range(size1): 
	element = int(input("Enter unique element: ")) 
	list2.append(element) 
print("set 2 =", list2) 

choice = 0 
while choice != 10: 
	print("\n") 
	print("******* Menu *******") 
	print(" I.Add") 
	print(" 2.Remove") 
	print(" 3.Contains") 
	print(" 4.Size") 
	print(" 5.Intersection") 
	print(" 6.Union") 
	print(" 7.Difference") 
	print(" 8.Subset") 
	print(" 9.Proper Subset") 
	print(" 10.Exit") 
	print("\n")
 
	choice = int(input("Enter Choice: ")) 
	print() 
	if choice == 1: 
		e = int(input("Enter unique number to add in set 1: ")) 
		if e not in list1 :
			list1.append(e)
			print("set 1 =", list1) 
		else:
			print("Enter unique element.")

	elif choice == 2: 
		e = int(input("Enter Number to remove: "))
		if e in list1: 
			list1.remove(e) 
			print("set 1 =", list1) 
		else: 
			print(e, "is not in set 1") 

	elif choice == 3: 
		e = int(input("Enter Number to Search in set 1: "))
		if e in list1: 
			print("Number Present in Set 1 !!") 
		else:
			print("Number not Present in Set 1 !!") 

		print("set 1 =", list1) 
	
	elif choice == 4:
		print("Set 1 Contains {} elements!!".format(len(list1)))
	
	elif choice == 5:
		list3 = [e for e in list1 if e in list2]
		print("set 1 =", list1)
		print("set 2 =", list2)
		print("Intersection =", list3)

	elif choice == 6:
		list3 = list1.copy()
		for e in list2:
			if e not in list1:
				list3.append(e)

		print("set 1 =", list1)
		print("set 2 =", list2)
		print("Union =", list3)

	elif choice == 7:
		list3 = [e for e in list1 if e not in list2]
		print("set 1 =", list1)
		print("set 2 =", list2)
		print("Difference =", list3)

	elif choice == 8:
		print("set 1 =", list1)
		print("set 2 =", list2)
		
		if isSubsetOf(list1,list2):
			print("Set 2 is a subset of set 1")
		else:
			print("Set 2 is not a subset of set 1")

	elif choice == 9:
		print("set 1 =", list1)
		print("set 2 =", list2)

		if isSubsetOf(list1, list2) and not isSubsetOf(list2, list1):
			print("Set 2 is proper subset of set 1")
		else:
			print("Set 2 is not proper subset of set 1")

	
	elif choice == 10:
		print("Exit")
		break
	
	elif choice<1 or choice>10:
		print("Invalid choice")
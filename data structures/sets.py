#initialize sets using the set() function or by placing all elements within curly braces
Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
Months = {"Jan", "Feb", "Mar"} 
Dates = {21, 22, 17}

print(Days)
print(Months)
print(Dates)

for d in Days:
	print(d)

#add item to set
Days.add("Sun") 
print(Days)

#remove item from set
Days.discard("Sun")
print(Days) 

DaysA = set(["Mon", "Tue", "Wed", "Thu"])
DaysB = set(["Thu", "Fri", "Sat", "Sun"])

#union of sets
AllDays = DaysA|DaysB
print(AllDays)

#intersection of sets
IntersectDays = DaysA & DaysB
print(IntersectDays)

#difference of sets
DifferenceDays = DaysA - DaysB
print(DifferenceDays)

#compare sets
DaysC = set(["Mon", "Tue", "Wed"])
DaysD = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

SubsetRes = DaysC <= DaysD
SupersetRes = DaysD >= DaysC

print(SubsetRes)
print(SupersetRes)

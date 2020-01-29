# th#is file calculates how many
# tiles i need to tile floor (in m2)
length = float(input("enter room length: "))
width = float(input("enter room width: "))
# length = 3.5
# width = 2.3
area = length * width
needed = area * 1.05
print("you need", needed, "tiles on metres squared,")

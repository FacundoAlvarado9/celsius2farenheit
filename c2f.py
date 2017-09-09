def ctof(x1):
	return (x1*1.8) +32
def ftoc(x1):
	return (x1-32) /1.8

#Main
print("Welcome to Pepa's Temperature converter.")
print("1. From Celsius to Farenheit [C to F]")
print("2. From Farenheit to Celsius [F to C]")

choice = int(input("Enter your option: "))

#Asking for a number
x1 = float(input("Now enter the number you want to convert: "))

#Conversion itself
if choice == 1:
	c = ctof(x1)
	print("{0}C converted is equal to {1}F" .format(x1, c))
	raw_input("Press any key to exit")
	exit()
elif choice == 2:
	f = ftoc(x1)
	print("{0}F converted is equal to {1}C" .format(x1, c))
	raw_input("Press any key to exit")
	exit()

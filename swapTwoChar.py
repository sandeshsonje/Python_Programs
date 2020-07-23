#WAP to accept two strings from user and swap their first two characters.
first=input("Enter first string")
second=input("Enter second string")
tempf=first[:2]
temps=second[:2]
first=temps+first[2:]
second=tempf+second[2:]
print("First:",first)
print("second",second)

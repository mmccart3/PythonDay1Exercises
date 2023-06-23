age = 17
country = "UK"

if age>17 and country == "UK":
    print ("What would you like to drink?")
elif age<21 and country == "USA":
    print ("sorry we cant't serve you")
elif age<18 and country == "UK":
    print ("sorry we cant't serve you")
elif age>20 and country == "USA":
    print ("What would you like to drink?")

print ("next customer please")
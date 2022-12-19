print("Enter your name: ")
name = input()
print("Enter your age: ")
age = int(input())

if (name != "" and age != "") and ( 18 <= age <= 31 ):
    print("Welcome to your holiday, {}".format(name))
else:
    print("Go away")

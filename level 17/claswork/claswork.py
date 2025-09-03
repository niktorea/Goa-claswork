age = int(input("Enter your age: "))

if age >= 64:
    print("elderly discount")
elif age >= 10:
    print("Child discount")
else:
    print("regular price")











age = 20

if age >= 18:
    # აქ უკვე ასაკი >= 18 არის სწორი,
    # ახლა შიგნით შეგვიძლია სხვა პირობა შევამოწმოთ
    if age >= 65:
        print("Pensioner")
    else:
        print("Adult")





age = int(input("Enter your age: "))
name = input("Enter your name: ")

# შემოწმება nested if-ით
if age < 18:
    print("Denied")
else:
    if name == "deme":
        print("Denied")
    else:
        print("Accepted")




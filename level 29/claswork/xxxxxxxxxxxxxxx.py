
def to_celsius(temp):
    
    celsius = (temp - 32) * 5 / 9
    return celsius


print(to_celsius(100))  



def check_number(num):
    if num % 2 == 0:
        print("ლუწი")
    else:
        print("კენტი")

check_number(10)  
check_number(7)















# 0) Default value გამოიყენება მაშინ, როცა არგუმენტი არ გადაეცემა ფუნქციას.
# მაგალითად, თუ ფუნქციას არგუმენტი არ მივაწოდეთ, ის გამოიყენებს default მნიშვნელობას.

# 1) ფუნქცია Student — რომელიც იღებს სახელს, გვარს და ნიშანს (default value = 6)
def Student(name, surname, grade=6):
    return f"You are {name} {surname}, and your grade is {grade}"

# ფუნქციის გამოძახება სხვადასხვა გზით:
print(Student("Nika", "Kesh", 9))   # გადაცემული ნიშანით
print(Student("Luka", "Giorgadze")) # default ნიშანით (6)
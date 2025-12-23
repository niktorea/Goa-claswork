# 0) ფუნქცია, რომელიც აბრუნებს ორ რიცხვიდან უფრო დიდს
def bigger_number(a, b):
    if a > b:
        return a
    else:
        return b


print(bigger_number(5, 9))  # გამოიტანს 9


# 1) ფუნქცია, რომელიც ამოწმებს კენტია თუ ლუწი
def even_or_odd(num):
    if num % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"


print(even_or_odd(7))  # გამოიტანს "კენტია"
print(even_or_odd(12)) # გამოიტანს "ლუწია"


# 2) ფუნქცია, რომელიც გამოიტანს 3 რიცხვს ზრდადობით
def sort_numbers(a, b, c):
    numbers = [a, b, c]     # ვქმნით სიას ამ 3 რიცხვით
    numbers.sort()           # ვალაგებთ ზრდადობით
    print(numbers)           # ვბეჭდავთ შედეგს




# 3) ფუნქცია, რომელიც მიიღებს ლისთს და გამოიტანს ყველაზე პატარა რიცხვს
def find_min(lst):
    print(min(lst))     # min() აბრუნებს სიაში ყველაზე პატარა ელემენტს

# მაგალითი:
find_min([4, 1, 7, 2, 9])   # გამოიტანს: 1











# 4) შექმენით dictionary, რომელსაც დაარქმევთ თქვენს სახელს და შეიტანეთ იქ თქვენი ინფორმაცია
nika = {
    "name": "Nika",
    "age": 9,
    "city": "Tbilisi",
    "hobby": "coding"
}

# 5) შექმენით dictionary, სახელად family სადაც შეიტანთ თქვენი ოჯახის წევრების ინფორმაციას
family = {
    "father": {"name": "Giorgi", "age": 42, "job": "engineer"},
    "mother": {"name": "tako", "age": 40, "job": "teacher"},
    "sister": {"name": "vika", "age": 11, "school": "public school "}
}


print(nika)
print(family)

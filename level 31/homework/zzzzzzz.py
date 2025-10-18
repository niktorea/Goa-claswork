# 0) ფუნქცია, რომელიც რიცხვს ამატებს 5-ს
def add_five(num):
    return num + 5


# 1) ფუნქცია, რომელიც აბრუნებს სიტყვის ბოლო ასოს
def last_char(text):
    return text[-1]


# 2) ფუნქცია, რომელიც ამოწმებს არის თუ არა რიცხვი ლუწი
def is_even(num):
    return num % 2 == 0


# 3) ფუნქცია, რომელიც აბრუნებს ორი რიცხვის ჯამს
def sum_two(a, b):
    return a + b


# 4) ფუნქცია, რომელიც აბრუნებს ორიდან უფრო დიდ რიცხვს
def bigger(a, b):
    return a if a > b else b

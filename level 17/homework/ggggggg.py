age = int(input("შეიყვანე ასაკი: "))

if 0 <= age <= 12:
    print("ბავშვი")
elif 13 <= age <= 19:
    print("თინეიჯერი")
elif 20 <= age <= 59:
    print("ზრდასრული")
else:
    print("პენსიონერი")




num = int(input("შეიყვანე რიცხვი: "))

if num < 0:
    print("უარყოფითი")
elif num == 0:
    print("ნული")
elif num > 0 and num < 100:
    print("პატარა რიცხვი")
else:
    print("დიდი რიცხვი")








score = int(input("შეიყვანე გამოცდის ქულა (0–100): "))

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")






day = int(input("შეიყვანე კვირის დღე (1–7): "))

if day == 1:
    print("ორშაბათი")
elif day == 2:
    print("სამშაბათი")
elif day == 3:
    print("ოთხშაბათი")
elif day == 4:
    print("ხუთშაბათი")
elif day == 5:
    print("პარასკევი")
elif day == 6:
    print("შაბათი")
elif day == 7:
    print("კვირა")
else:
    print("არასწორი დღეა!")








temp = int(input("შეიყვანე ტემპერატურა (°C): "))

if temp < 0:
    print("ძალიან ცივა")
elif 0 <= temp <= 15:
    print("გრილია")
elif 16 <= temp <= 30:
    print("თბილია")
elif 31 <= temp <= 40:
    print("ცხელა")
else:
    print("უაღრესად ცხელა")





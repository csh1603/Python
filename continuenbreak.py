absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("That's it for today's class. {0}, come to teacher's office.".format(student))
        break
    print("{0}, read the book".format(student))
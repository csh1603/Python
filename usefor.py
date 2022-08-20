# for waiting_n in [0,1,2,3,4]:
for waiting_n in range(1, 6):
    print("waiting number: {0}".format(waiting_n))

starbucks = ["Ironman", "Spiderman", "Groot"]
for customer in starbucks:
    print("{0}, your coffee is ready".format(customer))

customer = "Spiderman"
index = 5
while index >= 1:
    print("{0}, your coffee is ready. {1} time left.".format(customer, index))
    index -= 1
    if index == 0:
        print("coffee has been discarded")

# customer = "Ironman"
# index = 1
# while True:
#     print("{0}, your coffee is ready. {1} times".format(customer, index))
#     index += 1

customer = "Ironman"
person = "Unknown"

while person != customer:
    print("{0}, your coffee is ready".format(customer))
    person = input("What is your name?")
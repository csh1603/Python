# weather = input("How is the weather today?")
# if weather == "rain" or "snow" :
#    print("bring umbrella")
# elif weather == "fine dust":
#     print("bring mask")
# else:
#     print("don't need anthing")

temp = int(input("How's the temperature?"))
if 30 <= temp:
    print("So hot. Don't go outside")
elif 10 <= temp and temp < 30:
    print("Nice weather")
elif 0 <= temp < 10:
    print("Take a coat")
else:
    print("So cold. Don't go outside")
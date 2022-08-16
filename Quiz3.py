pw = "http://naver.com"
my_str = pw.replace("http://", "")
index = my_str.index(".")
my_str = my_str[:index]
passw = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0}'s password is {1}" .format(pw, passw))
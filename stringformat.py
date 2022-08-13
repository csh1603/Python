#print("a" + "b") ab
#print("a", "b") a b

# 방법 1
print("I am %d." %20)
print("I like %s." % "python")
print("The word apple starts with %c" % "A")

print("I like %s and %s" % ("red", "blue"))

# 방법 2
print("I am {}." .format(20))

print("I like {} and {}" .format ("red", "blue"))
print("I like {1} and {0}" .format ("red", "blue"))

# 방법 3
print("I am {age}, and like {color}." .format(age = 20, color = "red"))

# 방법 4
age = 20
color = "red"
print(f"I am {age}, and like {color}.")
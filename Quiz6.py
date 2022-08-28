def std_weight(height, gender):
    if gender == "man":
        return height*height*22
    else :
        return height*height*21

height = 175
gender = "man"
weight = round(std_weight(height/100, gender), 2)
print("A {0}cm tall {1} weighs {2}kg.".format(height, gender, weight))
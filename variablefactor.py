# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("name : {0} \t age : {1} \t".format(name, age), end =" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("name : {0} \t age : {1} \t".format(name, age), end =" ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("Ariana", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("Amy", 25, "Kotlin", "Swift")
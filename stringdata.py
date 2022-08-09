sentence = 'I am a boy'
print(sentence)
sentence2 = "Python is easy"
print(sentence2)

sentence3 = """
I am a boy, and Python is easy
"""
print(sentence3)

ID = "021114-1234567"

print("sex : " + ID[7])
print("year : " + ID[0:2]) # 0 부터 2 직전까지 (0, 1)
print("month : " + ID[2:4])
print("day : " + ID[4:6])

print("BDAY : " + ID[:6]) # 처음부터 6 직전까지
print("last 7 number : " + ID[7:])
print("last 7 number (reverse) : " + ID[-7:])
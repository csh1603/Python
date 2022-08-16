cabinet = {3:"Ariana", 100:"Selena"}
print(cabinet[3])
print(cabinet[100]) # key값에 없는 것을 입력하면 오류 발생 -> 프로그램 종료

print(cabinet.get(3)) # key값에 없는 것을 입력하면 None 출력
print(cabinet.get(5, "Available"))

# __이라는 키가 있나요?
print(3 in cabinet)


cabinet2 = {"A-3":"Ariana", "B-100":"Selena"}

# 새 손님
print(cabinet2)
cabinet2["A-3"] = "Justin"
cabinet2["C-20"] = "Harry"
print(cabinet2)

# 간 손님
del cabinet2["A-3"]
print(cabinet2)

# key들만 출력
print(cabinet2.keys())

# value들만 출력
print(cabinet2.values())

# key, value 쌍으로 출력
print(cabinet2.items())

# 목욕탕 매점
cabinet2.clear()
print(cabinet2)
# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"Amy", "Ariana", "Selena"}
python = set(["Amy", "Justin"])

# 교집합 (java와 파이썬을 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python을 할 수 있는 사람) -> 순서 보장 x
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있으나 python을 할 줄 모르는 사람)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("Ariana")
print(python)

# java를 까먹었어요
java.remove("Ariana")
print(java)
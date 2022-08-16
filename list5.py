subway = [10, 20, 30]
print(subway)

subway = ["Ariana", "Harry", "Charile"]
print(subway)

# Harry의 위치 찾기
print(subway.index("Harry"))

# Selena가 다음 정류장에서 다음 칸에 탐
subway.append("Selena")
print(subway)

# Justin을 Harry랑 Charile 사이에 태우면
subway.insert(2, "Justin")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # Selena 빠짐
print(subway)

print(subway.pop()) # Charlie 내림
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("Ariana")
print(subway.count("Ariana"))

# 정렬도 가능
num_list = [5, 4, 3, 2, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
#num_list.clear()
#print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["Justin", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)
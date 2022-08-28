gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[inside function] left guns : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[inside function] left guns : {0}".format(gun))
    return gun

print("total number of guns : {0}".format(gun))
# checkpoint(2) # 2명이 경게 근무 나감
gun = checkpoint_ret(gun, 2)
print("left guns : {0}".format(gun))
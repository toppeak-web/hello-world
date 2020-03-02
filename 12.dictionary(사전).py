# cabinet = {3:"박민재", 100:"엄태진"}
# print(cabinet[100]) # 값이 없으면 에러

# print(cabinet.get(3)) #값이없으면 none라고 뜸
# print(cabinet.get(4,"사용가능"))

# print(3 in cabinet) #T
# print(5 in cabinet) #F
cabinet = {"A-3":"박민재", "B-100":"엄태진"}
print(cabinet["A-3"])
print(cabinet.get("B-100"))

#새 손님
cabinet["C-20"] = "최진영"
cabinet["C-20"] = "엄준식"

#간 손님
del cabinet["A-3"]

print(cabinet)

# key 출력
print(cabinet.keys())

#벨류값
print(cabinet.values())

#키와 벨류 쌍으로 출력
print(cabinet.items())

# 페점
cabinet.clear()
print(cabinet)
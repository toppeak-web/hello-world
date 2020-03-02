# 중복 안됌, 순서 없음
my_set = {1,2,3,3,3,4}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 자바 파이썬 모두 사용가능한 사람
print(java & python)
print(python.intersection(java))

# 합집합 (자바나 파이썬 가능한 사람)
print(java | python)
print(java.union(python))

# 차집합 (자바 할 수 있지만 파이썬은 할줄 모르는)
print(java - python)
print(java.difference(python))

# 파이썬 할 줄 아는 사람이 증가
python.add("김태호")
print(python)

# 자바를 까먹
java.remove("김태호")
print(java)
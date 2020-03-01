subway = [10, 20, 30]
print(subway)
subway = ["박민재", "라이온", "이상용"]
print(subway)

#이상용씨가 몇 번쨰 칸에 타고 있는가?
print(subway.index("이상용")) #2

#다음 정류장에 오사용씨 탑승
subway.append("오상용")
print(subway)

# 오형훈씨를 박민재 / 라이온 사이에print(subway)
subway.insert(1, "오형훈")
print(subway)

#지하철 뒤에서부터 하차
print(subway.pop())
print(subway)

subway.append("박민재")
print(subway.count("박민재"))

# 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

#다양한 자료형 하껨 사용
mix_list = ["박민재", 50, True]
print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)
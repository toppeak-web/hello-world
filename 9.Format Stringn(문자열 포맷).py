# print("a" + "b")
# print("a","b")

# 방법 1
print("나는 %d살입니다." %20) #d는 정수
print("나는 %s을 쓰고 있어요" %"Python") 
print("나는 %cpple를 좋아해요" %"a") 

print("%s*%s=%s"%("1","0","0"))


# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {name}이며 {age}살이고, {color}색을 좋아해요.".format(name = "김현기", age = 21, color="black"))

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

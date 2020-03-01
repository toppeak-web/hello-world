# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com 
# 규칙1 : http:// 부분은 제외 => naver.com 
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver 
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                     (nav)             (5)           (1)        (!)
# 예) 생성된 비밀번호 : nav51

# site = "http://naver.com"
site = "https://www.youtube.com/watch?v=kWiCuklohdY&list=LLEIKy0pZjUsDJE4L1ob3d1w&index=3&t=1230s"
my_str = site.replace("http://","") 
my_str = site.replace("https://","") 
print(my_str)
my_str = my_str[:my_str.index(".")] #my_str[0:5] 0 ~ 5 직전까지. (0)
print(my_str)

pw = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(site, pw))
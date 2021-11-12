# 11.숫자의 갯수가 몇개인지 카운팅
# ex) 93728499321에서 9의 갯수 구하기(문자열 사용하지 않고)
number = 93728499321

count = 0

while number >0:
    # 각 자리의 마지막 숫자를 쪼갬(number % 10)
    if number % 10 == 9:
        count += 1
    number = number // 10


# 비효율적인 방법
# a = str(number)
# for x in a:
#     if x == 9:
#         count += 1
# print(count)

# num = "93728499321"
# print(num.count('9'))
# 아래코드를 이용하여 각 list1의 값을
# [2,3,4,5,6]으로 바꾸시오(python코드로)

# list1 = [10, 20, 30, 40, 50]
#
# for i in range(0, len(list1)):
#     list[i] += 1


# price : 원가, grade : 회원등급
def solution(price, grade):
    sale_price = 0
    if grade == "S":
        sale_price = price * 0.05
        # return price - price*0.05 이렇게도 계산 가능
    elif grade == "G":
        sale_price = price * 0.1
        # return price - price * 0.1 이렇게도계산 가능
    elif grade == "V":
        sale_price = price * 0.15
    return price - sale_price
    # return price - price*0.15 이렇게도 계산 가능

# testcase를 위한 output
result = solution(2500, "V")
print(result) # 2125
result = solution(96900, "S")
print(result) # 92055

def 보조함수(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0;
    for i in range(month-1):
        total += month_list[i]
    # tatal += @@@
    # return tatal -1

def solution(start_month, start_day, end_month, end_day):
    start_total = 보조함수(start_month, start_day)
    end_total = 보조함수(end_month, end_day)
    return end_total - start_total

arr = [1,2,3,3,1,3,3,2,3,2]
count = [0,0,0,0]

for x in arr:
     count[x] += 1

print(f"1의갯수 : {count[1]}")
print(f"2의갯수 : {count[2]}")
print(f"3의갯수 : {count[3]}")

# 문제 03_-2 최대값
counter = [0,2,3,5]

def 최대값(arr):
    large = 0
    for x in arr:
        if x > large :
            large = x
    return large

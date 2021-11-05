# 문자열에 해당단어가 몇개 있는지 카운팅

string = "ILOVKEFLOVEE"
find = "LOV"
count = 0

print(string.count("LOV"))

#Q1. 왜 일반화된 코드가 아닐까? -> find 문자열의 길이에 따라 코드가 달라짐
#Q2. 결함을 찾아라 -> string의 index범위를 넘어설 수 있다.

# i는 0부터 len(string)-1 만큼 반복:
for i in range(len(string)):
    # 만약에 string[i]가 'L' 이라면:
    # if string[i] == "L":  #Q2결함
    if string[i] == "L" and i+len(find) <= len(string):
        if string[i+1] == "O":
            if string[i+2] == "V":
                count += 1

print(count)
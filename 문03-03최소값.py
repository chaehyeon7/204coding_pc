# 문제 03-03 최소값
counter = [0,2,3,5]

def 최소값(arr):
    기존값 = 1001
    for x in arr:
        if x > 기존값 and x != 0 :
            기존값 = x
    최소 = 기존값
    return 최소

a = 최소값(counter)
print(a)
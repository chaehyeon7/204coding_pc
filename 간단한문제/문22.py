def pickup_even(arr):
    answer = list()
    for x in arr:
        if x%2 == 0:
            answer.append(x)
    return answer

a = pickup_even([3, 4, 5, 6, 7, 8])
print(a)

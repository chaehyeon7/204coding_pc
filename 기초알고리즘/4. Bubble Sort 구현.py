# 4. Bubble Sort 구형(버블소트가 무엇인지 말할수 있어야 함)

arr = [4, 3, 2, 7]

for i in range(0, len(arr)-1):
    for j in range(0, len(arr)-1-i):
        if(arr[j] < arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]




# if arr[0] > arr[1]:
#     arr[0], arr[1] = arr[1], arr[0]
# if arr[1] > arr[2]:
#     arr[1], arr[2] = arr[2], arr[1]
# if arr[2] > arr[3]:
#     arr[2], arr[3] = arr[3], arr[2]
#
# if arr[0] > arr[1]:
#     arr[0], arr[1] = arr[1], arr[0]
# if arr[1] > arr[2]:
#     arr[0], arr[2] = arr[2], arr[1]
#
# if arr[0] > arr[1]:
#     arr[0], arr[1] = arr[1], arr[0]
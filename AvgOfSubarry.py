# Problem Name: Average of All Contiguous Subarrays of Size K (Fixed Sliding Window)

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
total = 0  # this contains sum of first k numbers
avg = []

for i in range (k):
    total = (total + arr[i])

totalOne = total/k
avg.append(totalOne)

print('New Avg' , avg)
print('total', total)
for i in range(0,len(arr)-k ):
    print(arr[k+i])
    sum = total - arr[i] + arr[k+i]
    newAvg = sum/k 
    avg.append(newAvg)

print('New Avg' , avg)
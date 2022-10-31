n = int(input())
k = int(input())-1
arr = []
for i in range(1, n):
    if i%2==1:
        arr.append(i)
for i in range(2,n+1):
    if i%2==0:
        arr.append(i)
print(arr[k])

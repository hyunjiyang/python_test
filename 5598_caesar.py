arr = list(input())
answer = []

for i in range(len(arr)):
	n= ord(arr[i])-3
	if n < ord('A'):
		n+=26
	arr[i]=chr(n)

print("".join(arr))

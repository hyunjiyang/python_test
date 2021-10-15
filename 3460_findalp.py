#try1) index()
arr = list(input())
answer = []

for i in range(97,123):
	if chr(i) in arr:
		answer.append(str(arr.index(chr(i))))
	else:
		answer.append("-1")
    
print(" ".join(answer))


#try2) find() = 값 없을시 -1출력 . str만 가능
s=input()
for i in range(97,123): 
  print(s.find(chr(i)),end=' ')

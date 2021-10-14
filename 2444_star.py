/*
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
*/

N = int(input())

for i in range(-N+1,N):
    print(' '*(abs(i))+'*'*(2*N-1-2*abs(i)))

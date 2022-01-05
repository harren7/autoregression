### Binary coefficient of polynomial is represented in a descending order 
### ex. [1,0,0,0,0,0,0,0,0,1] stands for x^9+1

import numpy
import itertools
from operator import add

####### All combination of the binary polynomial
### Determine x^8~x^1's binary coefficient
n=8 
all_list = list(map(list, itertools.product([0, 1], repeat=n)))
### x^9 and x^0's coefficient is 1
for i in range(256):
  all_list[i].insert(0,1) 
  all_list[i].insert(9,1)

# Blank list to save current Polynomial
x=[];
# value of s(t) is saved in list S
S=[]
for x in range (256): #Make 256 lists inside list S
  S.append([])
#S which qualifies the condition
remainS=[];
fb = 0; #result of z-transform equation
func = []; #value of tau function
answer=[]; #answer polynomials for the first question
val = 0;
wantval = [1,-1,511]

for p in range(256):
  # Save the pth polynomial to a new list x
  x = all_list[p][0:9]
  S[p]=[x[8]];
  for l in range(510):
    for n in range(9):
      if all_list[p][n] == 0 :
        continue
      if all_list[p][n] == 1 :
          fb = fb + x[n];
    fb_ = fb%2;

    #Shift everything one place to the left
    x = x[1:] + x[:1]
    x[8] = fb_
    if x != all_list[p][0:9]:
      #Add the value of the first column in P1 to S1
      S[p].append(x[8])
    fb = 0;
  #Autocorrelation
  if len(S[p]) == 511:
    for l in range(0,511):
      for i in range (0,511):
        if int(l+i) < 511:
          val = val + (1-2*S[p][i])*(1-2*(S[p][i+l]))
        else :
          val = val + (1-2*S[p][i])*(1-2*(S[p][(i+l)%511]))
      func.append(val)
      val = 0;

    #check whether the autocorrelation values are equal to 511,1,-1
    b = numpy.in1d(func, wantval)
    result = all(element == True for element in b)
    if (result) : 
      answer.append(all_list[p])
      remainS.append(S[p])

    func = [];

#print("Answer Polynomial: ", answer)
#print(len(answer))

###Print Polynomial MSB-LSB
Show_answer = [];
for l in range(len(answer)):
  Show_answer.append([])

for p in range(len(answer)):
  for i in range(3):
    Show_answer[p].append(answer[p][3*i]*4 + answer[p][3*i+1]*2 + answer[p][3*i+2])
  Show_answer[p].append(answer[p][9]*4)

print("Answer Polynomial : " , Show_answer)
print(len(Show_answer))

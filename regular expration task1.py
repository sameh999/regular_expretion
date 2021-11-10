import re 
s = "heeellooo"
words = ["hello","helo" , "hi", "seee"]
#counter to count number off stretchy word repeated 
count =0
# the list of pattern in the word 
reg =''
reg_list=[]
# forloop to build the battern for eavry word in list of words 
for x in words:
  for ch in x :
    reg += "(" + ch +"|"+ ch +"{3,})"
  reg_list.append(reg)
  reg =''
# the function to fetch how many  time  the streatchy word are apperead
for w in range(0 ,len(reg_list)):
  if re.match(reg_list[w], s):
    count +=1
    print(reg_list[w])
    print("Match!")
  else:
    print(reg_list[w])
    print("Not a match!")
# print the number of appearing time 
print ("numer of match word = ",count)

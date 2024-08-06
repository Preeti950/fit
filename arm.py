# p=1
# for i in range(6):
#      for j in range(1,i+1):
#           print(p,end=" ")
#           p+=1
#      print()
""""
p=65
for i in range(65,70):
     for j in range(65,i+1):
          print(chr(p),end=" ")
          p+=1
     print()
"""
# p=65
# for i in range(65,70):
#      for j in range(70,i+1,-1):
#         print(" ",end="")
#      for k in range(65,i+1):
#         print(chr(p),end= "")
#         p+=1
#      print()

# fact=1
# for i in range(1,4):
#      fact=fact*i
# print(fact)

for i in range(5):
     for j in range(1,i-1,-1):
          print(" ",end="")
     for k in range(0,i+1):
          print("*",end="")
     print()
Rs=int(input("enter number of shirts:"))
Bs=int(input("enter number of shirts:"))
Ws=int(input("enter number of shirts:"))

total=Rs+Bs+Ws

prob_1=Bs/total
prob_2=Rs/total

prob_a_and_b=prob_1*prob_2
print("probablity of the second shirt is red given that the first shirt is blue:")
print(round((prob_2),3))

print("probablity that the second shirt is red and thefirst shirt is blue:")
print(round((prob_a_and_b),3))

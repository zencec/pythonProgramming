num_list=[]
n=int(input("Enterthenumberofvaluesinlist:"))
print("Enter the elements to the list:")
for i in range(n):
    val = int(input())
    num_list.append(val)
total=0
for item in num_list:
    total= total+item
print("Thesumofallitemsinthelist is:",total)
result=[]
start=int(input("Enterthestartingrange(four-digitnumber):"))
end = int(input("Enter the ending range(four-digit number): "))
if start<1000 or end>9999 or start>end:
    print("Invalidrange.Pleaseenteravalidfour-digitrange.")
else:
    for num in range(start,end+1):
         if num % 2 == 0:
            root =int(num**0.5)#takingthesquareroot
            if root * root==num:#checkingifitisaperfectsquare 
                result.append(num)# adding it to the list
    print("Four-digit even perfect square numbers in the given range:")
    print(result)
s1=int(input("enter a mark1:"))
s2=int(input("enter a mark2:"))
s3=int(input("enter a mark3:"))
s4=int(input("enter a mark4:"))
total=s1+s2+s3+s4
agg=(total/4)
print(total)
print(agg)
if(agg>75):
    print("Distinction")
elif(60<=agg>75):
    print("First Division")
elif(50<=agg>60):
    print("Second Division")
elif(40<=agg>50):
    print("Third Division")
else:
    print("Fail")
       
    

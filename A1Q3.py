numbers = [1,2,3,4,5,6,7,8,9]
even , odd = 0,0
for i in numbers :
    if i%2==0:
        even+=1
        print("Number of even number", even)
    else :
       if i%2==1:
        odd+=1
        print("Number of odd number", odd)

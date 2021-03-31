#calculator with basic trignometric function like sin and cos.

import math
  
def sin(a):
  return math.sin(a)
  
def cos(a):
    return math.cos(a)   

def tan(a):
    return math.tan(a)  
    
def degrees(a):
    return math.degrees(a)  
    
def radians(r):
    return math.radians(r)
    
def hypotenuse(x,y):
    return math.hypot(x,y)    
    
  
a = math.pi/6

print("Select operator : ")
print("1.Sin")
print("2.Cos")
print("3.Tan")
print("4.Degrees")
print("5.Radians")
print("6.Hypotenuse")   

while True:
    choice=input("Enter your choice : [1,2,3,4,5,6] \n")
    if choice in ('1','2','3','4','5','6'):
        if choice=='1':
            print ("The value of sine of pi/6 is : ", sin(a))

        elif choice=='2':
            print ("The value of cosine of pi/6 is : ", sin(a))   
            
        elif choice=='3':
            print ("The value of tangent of pi/6 is : ", tan(a))
            
        elif choice=='4':
            print ("The value in degrees of pi/6 is : ", degrees(a))    
            
        elif choice=='5':
            r=int(input("Enter value : "))
            print ("The value in radians of pi/6 is : ", radians(r))   
            
        elif choice=='6':
           x=int(input("Enter value_1 : "))
           y=int(input("Enter value_2 : "))
           print ("The value of hypotenuse is : ", hypotenuse(x,y))
        break
    
    else:
        print("Invalid input!!")

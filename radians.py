#Convert radians into degrees.

import math 
any_number = int(input())

radians = any_number * (math.pi/180)
print(math.sin(radians)) 


#another way of doing the same 
import math 

radian = int(input())
math = math.sin(math.radians(radian))
if -0.01 < math < 0.01:
    print(0)
else:
    print(round(math))

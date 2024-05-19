import math
def circle_stats(r):
    area = round((math.pi*r**2),2)
    circumference = 2*math.pi*r
    return area,circumference
a,c = circle_stats(3)
print("area:",a,"Circumference:",c)
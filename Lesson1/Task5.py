import math

x_a = int(input("Enter x for A: "))
y_a = int(input("Enter y for A: "))
x_b = int(input("Enter x for B: "))
y_b = int(input("Enter y for B: "))
res = math.sqrt((x_b - x_a)**2+(y_b-y_a)**2)
print('A ({}, {}); B ({}, {}) -> {:.2f}'.format(x_a,y_a,x_b,y_b,res))
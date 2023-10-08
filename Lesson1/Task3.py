x = int(input('Enter x coordinate: '))
y = int(input('Enter y coordonate: '))
if x > 0 and y > 0:
    print('x={}, y={} -> 1'.format(x, y))
elif x > 0 and y < 0:
    print('x={}, y={} -> 4'.format(x, y))
elif x < 0 and y < 0:
    print('x={}, y={} -> 3'.format(x, y))
elif x < 0 and y > 0:
    print('x={}, y={} -> 2'.format(x, y))

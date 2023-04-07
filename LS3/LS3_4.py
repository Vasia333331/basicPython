def my_func(x,y):
    v2 = 1
    i = 1
    while i <= abs(y):
        v2 *= x
        i += 1

    return  1 / v2

print(
    my_func(
        int(input("v1: ")),
        int(input("v2: "))
    )
)

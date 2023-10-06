# def add_one():
#     for x in range(1, 11):
#         print(x)
#
#
# add_one()

def add_one(num):
    if (num >= 9):
        return num + 1
    total = num + 1
    print(total)

    return add_one(total)

mynewvalue = add_one(0)
print(mynewvalue)


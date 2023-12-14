def keyValuArgs(name, **additions):
    for key, value in additions.items():
        print(key,'-->', value)
    # return f"{name} {additions}"


text = keyValuArgs(name='Al Amin', uni = 'NSu', dectric = 'Jhenidha', village = 'Fatepur')
print(text)


def find_sum(*values):
    sum = 0 
    for num in values:
        sum += num
    print(sum)


find_sum(1,1,1,1,1,1,4)

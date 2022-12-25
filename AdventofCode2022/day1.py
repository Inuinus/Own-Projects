f = open("input1.txt", "r")
numbers = f.read()
total = sum([int(num) for num in numbers.split(',')])
print(total)

for number in numbers:
    if number.strip():
        if value_max <= prev_max:
            value_max = prev_max
        else:
            prev_max = prev_max

    else:
        print("line is empty", number)
f.close()
length = int(input("how many level do you want: "))
space = 1 + (length - 1)*(2)

for h in range(length + 1):
    if h == 0:
        inst_level = 0
        level_length = length
        element = "^"
        part = 1 + (inst_level)*(2)
    elif h == length:
        inst_level = length // 2
        level_length = inst_level
        element = "|"
        part = inst_level
        inst_level = length // 4
    else:
        inst_level = length // 2
        level_length = inst_level
        element = "^"
        part = 1 + (inst_level)*(2)

    for i in range(level_length):
        j = 0
        while j < space:
            if j == (space // 2) - inst_level:
                for k in range(part):
                    print(element, end="")
            else:
                print(" ", end="")
            j += 1
        if h != length:
            inst_level += 1
            part += 2
        print("")
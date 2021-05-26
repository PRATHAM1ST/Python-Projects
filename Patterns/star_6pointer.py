size = int(input("how much size: "))
for a in [1, 0, size - 1, 2]:
    for i in range(size):
        if a == 0 or a == 1:
            b = i
            c = size - i - 1
            d = 0 
        elif a == 2 or a == size - 1:
            b = size - i - 1
            c = i
            d = size - i - 1
        if a == 1 or a == 2:
            for l in range(size):
                print("  ", end="")
            for j in range(size):
                if c == j:
                    # print(j,c)
                    print("*", end="")
                else:
                    print(" ", end="")
            if i != d:
                for k in range(size):
                    if b == k:
                        print("*", end="")
                    else:
                        print(" ", end="")
        else:
            if i == a:
                for h in ["* ", "  ", "* "]:
                    for j in range(size):
                        print(h, end="")
            else:
                for k in range(size):
                    if b == k:
                        print("*", end="")
                    else:
                        print("  ", end= "")
                for k in range(size):
                    print("  ", end="")             
                print(" ", end="")
                for k in range(size):
                    if c== k:
                        print("*", end="")
                    else:
                        print("  ", end= "")
        print("")

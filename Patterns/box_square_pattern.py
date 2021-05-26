total = int(input("how many lines or stars: "))
for a in [total, 1]:
    initial = a
    while initial and initial <= total:
        for i in range(total*2):
            if i < total:
                if i < initial:
                    print("*", end= "")
                else:
                    print(" ", end="")
            elif i >= total:
                if i - total < total - initial:
                    print(" ", end='')
                else:
                    print("*", end="")
        print("")
        if a == total:
            initial -= 1
        elif a == 1:
            initial += 1
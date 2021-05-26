def add(a, b, x = None):
    x  = b - a
    print('')
    print('                          =>  x = {} - {}'.format(b, a))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def mult(a, b, x = None):
    x = b / a
    print('')
    print('                          =>  x = {} / {}'.format(b, a))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def div1(a, b, x = None):
    x = b * a
    print('')
    print('                          =>  x = {} * {}'.format(b, a))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def div2(a, b, x = None):
    x = a / b
    print('')
    print('                          =>  x = {} / {}'.format(a, b))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def sub1(a, b, x = None):
    x = a - b
    print('')
    print('                          =>  x = {} - {}'.format(a, b))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def sub2(a, b, x = None):
    x = b + a
    print('')
    print('                          =>  x = {} + {}'.format(b, a))
    print('')
    print('                          =>  x = {}'.format(x))
def pow_add1(a, b, n, x = None):
    x  = b - (a**n)
    print('')
    print('                          =>  x = {} - {}**{}'.format(b, a, n))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def pow_add2(a, b, n, x = None):
    x  = (b**n) - a
    print('')
    print('                          =>  x = {}**{} - {}'.format(b, n, a))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def pow_add3(a, b, n, x = None):
    x = ((b - a)**(1/n))
    print('')
    print('                          =>  x = ({} - {})**(1/{})'.format(b, a, n))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def pow_mult1(a, b, n, x = None):
    x = b / (a**n)
    print('')
    print('                          =>  x = {} / {}**{}'.format(b, a, n))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def pow_mult2(a, b, n, x = None):
    x = (b**n) / a
    print('')
    print('                          =>  x = {}**{} / {}'.format(b, n, a))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def pow_mult3(a, b, n, x =None):
    x = ((b/a)**(1/n))
    print('')
    print('                          =>  x = ({}/{})**(1/{})'.format(b, a, n))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def pow_div1(a, b, n, x = None):
    x = b * (a**n)
    print('')
    print('                          =>  x = {} * {}**{}'.format(b, a, n))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def pow_div2(a, b, n, x = None):
    x = (b**n) * a
    print('')
    print('                          =>  x = {}**{} * {}'.format(b, n, a))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def pow_div3(a, b, n, x = None):
    x = a / (b**n)
    print('')
    print('                          =>  x = {} / {}**{}'.format(a, b, n))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def pow_div4(a, b, n, x = None):
    x = (a**n) / b
    print('')
    print('                          =>  x = {}**{} / {}'.format(a, n, b))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def pow_div5(a, b, n, x = None):
    x = ((a * b)**(1/n))
    print('')
    print('                          =>  x = ({}*{})**(1/{})'.format(a, b, n))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def pow_div6(a, b, n, x = None):
    x = ((a / b)**(1/n))
    print('')
    print('                          =>  x = ({}/{})**(1/{})'.format(a, b, n))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def pow_sub1(a, b, n, x = None):
    x = a - (b**n)
    print('')
    print('                          =>  x = {} - {}**{}'.format(a, b, n))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def pow_sub2(a, b, n, x = None):
    x = (a**n) - b
    print('')
    print('                          =>  x = {}**{} - {}'.format(a, n, b))
    print('')
    print('                          =>  x = {}'.format(x))
    print('')
def pow_sub3(a, b, n, x = None):
    x = (b**n) + a
    print('')
    print('                          =>  x = {}**{} + {}'.format(b, n, a))
    print('')
    print('                          =>  x = {}'.format(x))
def pow_sub4(a, b, n, x = None):
    x = (a**n) - b
    print('')
    print('                          =>  x = {}**{} - {}'.format(a, n, b))
    print('')
    print('                          =>  x = {}'.format(x))
def pow_sub5(a, b, n, x = None):
    x = ((a + b)**(1/n))
    print('')
    print('                          =>  x = ({} + {})**(1/{})'.format(a, b, n))
    print('')
    print('                          =>  x = {}'.format(x))
def pow_sub6(a, b, n, x = None):
    x = ((a - b)**(1/n))
    print('')
    print('                          =>  x = ({} - {})**(1/{})'.format(b, a, n))
    print('')
    print('                          =>  x = {}'.format(x))
def deg_add(a, b, n, x = None):
    x = b**(1/n) - a
    print('')
    print('                          =>  x = {}**(1/{}) - {}'.format(b, n, a))
    print('')
    print('                          =>  x = {}'.format(x))
def deg_mult(a, b, n, x = None):
    x = b**(1/n) / a
    print('')
    print('                          =>  x = {}**(1/{}) / {}'.format(b, n, a))
    print('')
    print('                          =>  x = {}'.format(x))
def deg_sub1(a, b, n, x = None):
    x = b**(1/n) + a
    print('')
    print('                          =>  x = {}**(1/{}) + {}'.format(b, n, a))
    print('')
    print('                          =>  x = {}'.format(x))
def deg_sub2(a, b, n, x = None):
    x = a - b**(1/n)
    print('')
    print('                          =>  x = {} - {}**(1/{})'.format(a, b, n))
    print('')
    print('                          =>  x = {}'.format(x))
def deg_div1(a, b, n, x = None):
    x = b**(1/n) * a
    print('')
    print('                          =>  x = {}**(1/{}) * {}'.format(b, n, a))
    print('')
    print('                          =>  x = {}'.format(x))
def deg_div2(a, b, n, x = None):
    x = a / b**(1/n)
    print('')
    print('                          =>  x = {} / {}**(1/{})'.format(a, b, n))
    print('')
    print('                          =>  x = {}'.format(x))


print('  you can write the expression in any of given formt, kindly do not change the format or else it will not give the ans.')
print('                   a + x = b        or   a - x = b       or   a * x = b        or   a / x = b       ')
print('                   x + a = b        or   x - a = b       or   x * a = b        or   x / a = b       ')
print('                   a**n + x = b     or   a**n - x = b    or   a**n * x = b     or   a**n / x = b    ')
print('                   x + a**n = b**n  or   x - a**n = b    or   x * a**n = b     or   x / a**n = b    ')
print('                   a + x = b**n     or   a - x = b**n    or   a * x  = b**n    or   a / x = b**n    ')
print('                   x + a = b**n     or   x - a = b**n    or   x * a = b**n     or   x / a = b**n    ')
print('                   a + x**n = b     or   a - x**n = b    or   a * x**n = b     or   a / x**n = b    ')
print('                   x**n + a = b     or   x**n - a = b    or   x**n * a = b     or   x**n / a = b    ')
print('                   (a + x)**n = b   or   (a - x)**n = b  or   (a * x)**n = b   or   (a / x)**n = b    ')
print('                   (x + a)**n = b   or   (x - a)**n = b  or   (x * a)**n = b   or   (x / a)**n = b    ')
print('')
print('')
print('                                 where a & b & n will be your given values!')
print('                                    a & b & n should be within 5 digits!')
print('')
print('')

x = []
n = []
s = []
o = []
t = []
y = input('            write expression: ')
for i in  range(len(y)):
    if y[i] !='(' and y[i] != ')' and y[i] != '+' and y[i] != '/' and y[i] != '*' and y[i] != '-' and y[i] != ' ' and y[i] != 'x' and y[i] != '=':
        if y[i] !='(' and y[i] != ')' and y[i] != '+' and y[i] != '/' and y[i] != '*' and y[i] != '-' and y[i] != ' ' and y[i] != 'x' and y[i] != '=':
            if i != (len(y) - 1):
                if y[i + 1] =='(' or y[i + 1] == ')' or y[i + 1] == '+' or y[i + 1] == '/' or y[i + 1] == '*' or y[i + 1] == '-' or y[i + 1] == ' ' or y[i + 1] == 'x' or y[i + 1] == '=':
                        if i == 0:
                            x.append(int(y[i]))
                            x.append(int(i))

                        elif y[i - 1] =='(' or y[i - 1] == ')' or y[i - 1] == '+' or y[i - 1] == '/' or y[i - 1] == '*' or y[i - 1] == '-' or y[i - 1] == ' ' or y[i - 1] == 'x' or y[i - 1] == '=':
                            if y[i - 2] != '*':
                                x.append(int(y[i]))
                                x.append(int(i))
                            if y[i - 2] == '*' and y[i - 1] != '*':
                                x.append(int(y[i]))
                                x.append(int(i))
                            if y[i - 2] == '*' and y[i - 1] == '*':
                                n.append(int(y[i]))
                                n.append(int(i))

            if i == (len(y) - 1):
                if y[i - 1] =='(' or y[i - 1] == ')' or y[i - 1] == '+' or y[i - 1] == '/' or y[i - 1] == '*' or y[i - 1] == '-' or y[i - 1] == ' ' or y[i - 1] == 'x' or y[i - 1] == '=':
                    if y[i - 2] != '*':
                        x.append(int(y[i]))
                        x.append(int(i))
                    if y[i - 2] == '*' and y[i - 1] == '*':
                        n.append(int(y[i]))
                        n.append(int(i))

    if y[i] == '+' or y[i] == '/' or y[i] == '-' or y[i] == '=':
        s.append(y[i])
        s.append(int(i))
    if y[i] == '*' and y[i - 1] != '*' and y[i + 1] != '*':
        s.append(y[i])
        s.append(int(i))
    if y[i] == 'x':
        t.append(y[i])
        t.append(int(i))

    if y[i] !='(' and y[i] != ')' and y[i] != '+' and y[i] != '/' and y[i] != '*' and y[i] != '-' and y[i] != ' ' and y[i] != 'x' and y[i] != '=':
        if i + 1 <= (len(y) - 1) and i <= (len(y) - 2):
            if y[i + 1] !='(' and y[i + 1] != ')' and y[i + 1] != '+' and y[i + 1] != '/' and y[i + 1] != '*' and y[i + 1] != '-' and y[i + 1] != ' ' and y[i + 1] != 'x' and y[i + 1] != '=':
                if i != (len(y) - 2):
                    if y[i + 2] =='(' or y[i + 2] == ')' or y[i + 2] == '+' or y[i + 2] == '/' or y[i + 2] == '*' or y[i + 2] == '-' or y[i + 2] == ' ' or y[i + 2] == 'x' or y[i + 2] == '=':
                        if i == 0:
                            x.append(int(y[i])*10 + int(y[i + 1]))
                            x.append(int(i))
                        if y[i - 1] =='(' or y[i - 1] == ')' or y[i - 1] == '+' or y[i - 1] == '/' or y[i - 1] == '-' or y[i - 1] == ' ' or y[i - 1] == 'x' or y[i - 1] == '=':
                            x.append(int(y[i])*10 + int(y[i + 1]))
                            x.append(int(i))
                        if y[i - 1] == '*' and y[i - 2] != '*':
                             x.append(int(y[i])*10 + int(y[i + 1]))
                             x.append(int(i))
                        if y[i - 1] == '*' and y[i - 2] == '*':
                             n.append(int(y[i])*10 + int(y[i + 1]))
                             n.append(int(i))

                if i == (len(y) - 2):
                    if y[i - 1] =='(' or y[i - 1] == ')' or y[i - 1] == '+' or y[i - 1] == '/' or y[i - 1] == '*' or y[i - 1] == '-' or y[i - 1] == ' ' or y[i - 1] == 'x' or y[i - 1] == '=':
                        if y[i - 1] == '*' and y[i - 2]!= '*':
                            x.append(int(y[i])*10 + int(y[i + 1]))
                            x.append(int(i))
                        if y[i - 1] == '*' and y[i - 2]== '*':
                            n.append(int(y[i])*10 + int(y[i + 1]))
                            n.append(int(i))
                        if y[i - 1] =='(' or y[i - 1] == ')' or y[i - 1] == '+' or y[i - 1] == '/' or y[i - 1] == '-' or y[i - 1] == ' ' or y[i - 1] == 'x' or y[i - 1] == '=':
                            x.append(int(y[i])*10 + int(y[i + 1]))
                            x.append(int(i))

        if i <= (len(y) - 3) and (i + 2) <= (len(y) - 1) and (i + 1) <= (len(y) - 2):
            if y[i + 2] !='(' and y[i + 2] != ')' and y[i + 2] != '+' and y[i + 2] != '/' and y[i + 2] != '*' and y[i + 2] != '-' and y[i + 2] != ' ' and y[i + 2] != 'x' and y[i + 2] != '='and y[i + 1] != '*':
                if i != (len(y) - 3):
                    if y[i + 3] =='(' or y[i + 3] == ')' or y[i + 3] == '+' or y[i + 3] == '/' or y[i + 3] == '*' or y[i + 3] == '-' or y[i + 3] == ' ' or y[i + 3] == 'x' or y[i + 3] == '=':
                        if i == 0:
                            x.append(int(y[i])*100 + int(y[i + 1])*10 + int(y[i + 2]))
                            x.append(int(i))
                        if y[i - 1] == '(' or y[i - 1] == ')' or y[i - 1] == '+' or y[i - 1] == '/' or y[i - 1] == '-' or y[i - 1] == ' ' or y[i - 1] == 'x' or y[i - 1] == '=':
                            print(i ,'what')
                            x.append(int(y[i])*100 + int(y[i + 1])*10 + int(y[i + 2]))
                            x.append(int(i))
                        if y[i - 1] == '*' and y[i - 2] == '*':
                            n.append(int(y[i])*100 + int(y[i + 1])*10 + int(y[i + 2]))
                            n.append(int(i))
                if i == (len(y) - 3) and (i + 1) < (len(y) - 1) and (i + 2) < (len(y)):
                    if y[i - 1] =='(' or y[i - 1] == ')' or y[i - 1] == '+' or y[i - 1] == '/' or y[i - 1] == '*' or y[i - 1] == '-' or y[i - 1] == ' ' or y[i - 1] == 'x' or y[i - 1] == '=':
                        if y[i - 1] == '*' and y[i - 2] != '*':
                            x.append(int(y[i])*100 + int(y[i + 1])*10 + int(y[i + 2]))
                            x.append(int(i))
                        if y[i - 1] == '*' and y[i - 2] == '*':
                            n.append(int(y[i])*100 + int(y[i + 1])*10 + int(y[i + 2]))
                            n.append(int(i))
                        if y[i - 1] =='(' or y[i - 1] == ')' or y[i - 1] == '+' or y[i - 1] == '/' or y[i - 1] == '-' or y[i - 1] == ' ' or y[i - 1] == 'x' or y[i - 1] == '=':
                            x.append(int(y[i])*100 + int(y[i + 1])*10 + int(y[i + 2]))
                            x.append(int(i))

        if i <= (len(y) - 4) and (i + 3) <= (len(y) - 1) and (i + 2) <= (len(y) - 2):
            if y[i + 3] !='(' and y[i + 3] != ')' and y[i + 3] != '+' and y[i + 3] != '/' and y[i + 3] != '*' and y[i + 3] != '-' and y[i + 3] != ' ' and y[i + 3] != 'x' and y[i + 3] != '=' and y[i + 2] != '*':
                if i != (len(y) - 4):
                    if y[i + 4] =='(' or y[i + 4] == ')' or y[i + 4] == '+' or y[i + 4] == '/' or y[i + 4] == '*' or y[i + 4] == '-' or y[i + 4] == ' ' or y[i + 4] == 'x' or y[i + 4] == '=':
                        if i == 0:
                            x.append(int(y[i])*1000 + int(y[i + 1])*100 + int(y[i + 2])*10 + int(y[i + 3]))
                            x.append(int(i))
                        if y[i - 1] =='(' or y[i - 1] == ')' or y[i - 1] == '+' or y[i - 1] == '/' or y[i - 1] == '-' or y[i - 1] == ' ' or y[i - 1] == 'x' or y[i - 1] == '=':
                            x.append(int(y[i])*1000 + int(y[i + 1])*100 + int(y[i + 2])*10 + int(y[i + 3]))
                            x.append(int(i))
                        if y[i - 1] == '*' and y[i - 2] == '*':
                            n.append(int(y[i])*1000 + int(y[i + 1])*100 + int(y[i + 2])*10 + int(y[i + 3]))
                            n.append(int(i))
                if i == (len(y) - 4) and (i + 2) < (len(y) - 1) and (i + 3) < (len(y)):
                    if y[i - 1] =='(' or y[i - 1] == ')' or y[i - 1] == '+' or y[i - 1] == '/' or y[i - 1] == '*' or y[i - 1] == '-' or y[i - 1] == ' ' or y[i - 1] == 'x' or y[i - 1] == '=':
                        if y[i - 1] == '*' and y[i - 2]!= '*':
                            x.append(int(y[i])*1000 + int(y[i + 1])*100 + int(y[i + 2])*10 + int(y[i + 3]))
                            x.append(int(i))
                        if y[i - 1] == '*' and y[i - 2]== '*':
                            n.append(int(y[i])*1000 + int(y[i + 1])*100 + int(y[i + 2])*10 + int(y[i + 3]))
                            n.append(int(i))
                        if y[i - 1] =='(' or y[i - 1] == ')' or y[i - 1] == '+' or y[i - 1] == '/' or y[i - 1] == '-' or y[i - 1] == ' ' or y[i - 1] == 'x' or y[i - 1] == '=':
                            x.append(int(y[i])*1000 + int(y[i + 1])*100 + int(y[i + 2])*10 + int(y[i + 3]))
                            x.append(int(i))

        if i <= (len(y) - 5) and (i + 4) <= (len(y) - 1) and (i + 3) <= (len(y) - 2):
            if y[i + 4] !='(' and y[i + 4] != ')' and y[i + 4] != '+' and y[i + 4] != '/' and y[i + 4] != '*' and y[i + 4] != '-' and y[i + 4] != ' ' and y[i + 4] != 'x' and y[i + 4] != '='and y[i + 3] != '+' and y[i + 3] != '/' and y[i + 3] != '*' and y[i + 3] != '-' and y[i + 3] != ' ' and y[i + 3] != 'x' and y[i + 3] != '=':
                if i != (len(y) - 5):
                    if y[i + 5] =='(' or y[i + 5] == ')' or y[i + 5] == '+' or y[i + 5] == '/' or y[i + 5] == '*' or y[i + 5] == '-' or y[i + 5] == ' ' or y[i + 5] == 'x' or y[i + 5] == '=':
                        if i == 0:
                            x.append(int(y[i])*10000 + int(y[i + 1])*1000 + int(y[i + 2])*100 + int(y[i + 3])*10 + int(y[i + 4]))
                            x.append(int(i))
                        if y[i - 1] == '+' or y[i - 1] == '/' or y[i - 1] == '-' or y[i - 1] == ' ' or y[i - 1] == 'x' or y[i - 1] == '=':
                            x.append(int(y[i])*10000 + int(y[i + 1])*1000 + int(y[i + 2])*100 + int(y[i + 3])*10 + int(y[i + 4]))
                            x.append(int(i))
                        if y[i - 1] == '*' and y[i - 2] == '*':
                            n.append(int(y[i])*10000 + int(y[i + 1])*1000 + int(y[i + 2])*100 + int(y[i + 3])*10 + int(y[i + 4]))
                            n.append(int(i))
                if i == (len(y) - 5) and (i + 3) < (len(y) - 1) and (i + 4) < (len(y)):
                    if y[i - 1] =='(' or y[i - 1] == ')' or  y[i - 1] == '+' or y[i - 1] == '/' or y[i - 1] == '*' or y[i - 1] == '-' or y[i - 1] == ' ' or y[i - 1] == 'x' or y[i - 1] == '=':
                        if y[i - 1] == '*' and y[i - 2]!= '*':
                            x.append(int(y[i])*10000 + int(y[i + 1])*1000 + int(y[i + 2])*100 + int(y[i + 3])*10 + int(y[i + 4]))
                            x.append(int(i))
                        if y[i - 1] == '*' and y[i - 2]== '*':
                            n.append(int(y[i])*10000 + int(y[i + 1])*1000 + int(y[i + 2])*100 + int(y[i + 3])*10 + int(y[i + 4]))
                            n.append(int(i))
                        if y[i - 1] =='(' or y[i - 1] == ')' or y[i - 1] == '+' or y[i - 1] == '/' or y[i - 1] == '-' or y[i - 1] == ' ' or y[i - 1] == 'x' or y[i - 1] == '=':
                            x.append(int(y[i])*10000 + int(y[i + 1])*1000 + int(y[i + 2])*100 + int(y[i + 3])*10 + int(y[i + 4]))
                            x.append(int(i))
try:
    try:
        o = x + n + s + t
        a = x[0]
        b = x[2]
        n = n[0]
        if y[0] != '(':
            if o[5] != o[11] + 3:
                if o[5] < o[9]:    #1**6 + x = 3
                    if s[0] == '+':
                        pow_add1(a, b, n)
                    if s[0] == '*':
                        pow_mult1(a, b, n)
                    if s[0] == '-':
                        if o[7] == o[1] + 1 or o[7] == o[1] + 2 or o[7] == o[1] + 3 or o[7] == o[1] + 4 or o[7] == o[1] + 5 or o[7] == o[1] + 6 or o[7] == o[1] + 7 or o[7] == o[1] + 8 or o[7] == o[1] + 9 or o[7] == o[1] + 10 or o[7] == o[1] + 11 or o[7] == o[1] + 12:
                            pow_sub2(a, b, n)
                        if o[7] == o[1] - 4 or o[7] == o[1] - 3 or o[7] == o[1] - 2 or o[7] == o[1] - 1 or o[7] == o[1] - 5:
                            pow_sub4(a, b, n)
                    if s[0] == '/':
                        if o[7] == o[1] - 1 or o[7] == o[1] - 2 or o[7] == o[1] - 3 or o[7] == o[1] - 4 or o[7] == o[1] - 5 or o[7] == o[1] - 6 or o[7] == o[1] - 7 or o[7] == o[1] - 8 or o[7] == o[1] - 9 or o[7] == o[1] - 10 or o[7] == o[1] - 11 or o[7] == o[1] - 12:
                            pow_div1(a, b, n)
                        if o[7] == o[1] + 1 or o[7] == o[1] + 2 or o[7] == o[1] + 3 or o[7] == o[1] + 4 or o[7] == o[1] + 5 or o[7] == o[1] + 6 or o[7] == o[1] + 7 or o[7] == o[1] + 8 or o[7] == o[1] + 9 or o[7] == o[1] + 10 or o[7] == o[1] + 11 or o[7] == o[1] + 12:
                            pow_div4(a, b, n)

                if o[5] > o[9]:    #1 + x = 3**6
                    if s [0] == '+':
                        pow_add2(a, b, n)
                    if s[0] == '*':
                        pow_mult2(a, b, n)
                    if s[0] == '-':
                        if o[7] == o[1] + 1 or o[7] == o[1] + 2 or o[7] == o[1] + 3 or o[7] == o[1] + 4 or o[7] == o[1] + 5 or o[7] == o[1] + 6 or o[7] == o[1] + 7:
                            pow_sub1(a, b, n)
                        if o[7] == o[1] - 1 or o[7] == o[1] - 2 or o[7] == o[1] - 3 or o[7] == o[1] - 4 or o[7] == o[1] - 5 or o[7] == o[1] - 6 or o[7] == o[1] - 7:
                            pow_sub3(a, b, n)
                    if s[0] == '/':
                        if o[7] == o[1] + 1 or o[7] == o[1] + 2 or o[7] == o[1] + 3 or o[7] == o[1] + 4 or o[7] == o[1] + 5 or o[7] == o[1] + 6 or o[7] == o[1] + 7:
                            pow_div3(a, b, n)
                        if o[7] == o[1] - 1 or o[7] == o[1] - 2 or o[7] == o[1] - 3 or o[7] == o[1] - 4 or o[7] == o[1] - 5 or o[7] == o[1] - 6 or o[7] == o[1] - 7:
                            pow_div2(a, b, n)


            if o[5] == o[11] + 3:
                if o[5] < o[9]:    #1**6 + x = 3
                    if s[0] == '+':
                        pow_add3(a, b, n)
                    if s[0] == '*':
                        pow_mult3(a, b, n)
                    if s[0] == '-':
                        pow_sub5(a, b, n)
                    if s[0] == '/':
                        pow_div5(a, b, n)
                if o[5] > o[9]:
                    if s[0] == '+':
                        pow_add3(a, b, n)
                    if s[0] == '*':
                        pow_mult3(a, b, n)
                    if s[0] == '-':
                        pow_sub6(a, b, n)
                    if s[0] == '/':
                        pow_div6(a, b, n)


        if  y[0] == '(' or y[1] == '(' or y[2] == '(':
            if s [0] == '+':
                deg_add(a, b, n)
            if s[0] == '*':
                deg_mult(a, b, n)
            if s[0] == '-':
                if o[7] == o[1] + 1 or o[7] == o[1] + 2 or o[7] == o[1] + 3 or o[7] == o[1] + 4 or o[7] == o[1] + 5:
                    deg_sub2(a, b, n)
                if o[7] == o[1] - 1 or o[7] == o[1] - 2 or o[7] == o[1] - 3:
                    deg_sub1(a, b, n)
            if s[0] == '/':
                if o[7] == o[1] + 1 or o[7] == o[1] + 2 or o[7] == o[1] + 3 or o[7] == o[1] + 4 or o[7] == o[1] + 5:
                    deg_div2(a, b, n)
                if  o[7] == o[1] - 1 or o[7] == o[1] - 2 or o[7] == o[1] - 3:
                    deg_div1(a, b, n)


    except IndexError or TypeError as e:
        a = x[0]
        b = x[2]
        for i in range(len(y)):
            if i > 0 and i < (len(y) - 1):
                if y[i - 1] != '*' and y[i + 1] != '*':
                    if y[i] == '{}'.format('+'):
                        add(a, b)
                    if y[i] == '{}'.format('*'):
                        mult(a, b)
                    if y[i] == '{}'.format('-'):
                        if y[i + 2] == 'x':
                            sub1(a, b)
                        if y[i - 2] == 'x':
                            sub2(a, b)
                    if y[i] == '{}'.format('/'):
                        if y[i + 2] == 'x':
                            div2(a, b)
                        if y[i - 1] == 'x' or y[i - 2] == 'x':
                            div1(a, b)

except OverflowError as e:
    print('')
    print('                          =>  sorry it is not a super computer!')
    print('')
    print('                          =>  Integer division is too large for float')
    print('')
    print('')

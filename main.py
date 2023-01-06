i = 1
z = ''
def x_vin(arr):
    if (arr[0][0] == 'x' and arr[0][1] == 'x' and arr[0][2] == 'x') or \
            (arr[0][0] == 'x' and arr[1][0] == 'x' and arr[2][0] == 'x') or \
            (arr[0][0] == 'x' and arr[1][1] == 'x' and arr[2][2] == 'x') or \
            (arr[0][2] == 'x' and arr[1][1] == 'x' and arr[2][0] == 'x') or \
            (arr[2][0] == 'x' and arr[2][1] == 'x' and arr[2][2] == 'x') or \
            (arr[1][0] == 'x' and arr[1][1] == 'x' and arr[1][2] == 'x') or \
            (arr[0][1] == 'x' and arr[1][1] == 'x' and arr[2][1] == 'x') or \
            (arr[0][2] == 'x' and arr[1][2] == 'x' and arr[2][2] == 'x'):
        print("Tic win")
        return True

def o_vin(arr):
    if (arr[0][0] == 'o' and arr[0][1] == 'o' and arr[0][2] == 'o') or \
            (arr[0][0] == 'o' and arr[1][0] == 'o' and arr[2][0] == 'o') or \
            (arr[0][0] == 'o' and arr[1][1] == 'o' and arr[2][2] == 'o') or \
            (arr[0][2] == 'o' and arr[1][1] == 'o' and arr[2][0] == 'o') or \
            (arr[2][0] == 'o' and arr[2][1] == 'o' and arr[2][2] == 'o') or \
            (arr[1][0] == 'o' and arr[1][1] == 'o' and arr[1][2] == 'o') or \
            (arr[0][1] == 'o' and arr[1][1] == 'o' and arr[2][1] == 'o') or \
            (arr[0][2] == 'o' and arr[1][2] == 'o' and arr[2][2] == 'o'):
        print("Tac win")
        return True

def draw(arr):
    for x in arr:
        for y in x:
            if y != "":
                continue
            else:
                return False
    print('Draw')
    return True


a = [['', '', ''], ['', '', ''], ['', '', '']]
while True:
    for x in a:
        print(x)
    if i == 1:
        z = 'x'
        print('Turn Tic')
    elif i == -1:
        z = 'o'
        print('Turn Tac')
    n = input('enter num square: ')
    if n == '1':
        if a[0][0] == '':
            a[0][0] = z
            i *= -1
    elif n == '2':
        if a[0][1] == '':
            a[0][1] = z
            i *= -1
    elif n == '3':
        if a[0][2] == '':
            a[0][2] = z
            i *= -1
    elif n == '4':
        if a[1][0] == '':
            a[1][0] = z
            i *= -1
    elif n == '5':
        if a[1][1] == '':
            a[1][1] = z
            i *= -1
    elif n == '6':
        if a[1][2] == '':
            a[1][2] = z
            i *= -1
    elif n == '7':
        if a[2][0] == '':
            a[2][0] = z
            i *= -1
    elif n == '8':
        if a[2][1] == '':
            a[2][1] = z
            i *= -1
    elif n == '9':
        if a[2][2] == '':
            a[2][2] = z
            i *= -1
    else:
        print('Incorrect. Try again')
        continue
    if x_vin(a) or o_vin(a) or draw(a):
        for x in a:
            print(x)
        ag = input('Try again?\n1:Yes\n2:No\n')
        if ag == '1':
            a = [['', '', ''], ['', '', ''], ['', '', '']]
            continue
        else:
            break

print("End game")

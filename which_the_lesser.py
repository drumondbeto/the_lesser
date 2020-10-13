# This function compares the numbers and informs which is the lesser.
def the_lesser(x, y, z):
    if x < y and x < z:
        return print(x, ' is the lesser.')
    if y < x and y < z:
        return print(y, ' is the lesser.')
    if z < x and z < y:
        return print(z, ' is the lesser.')
    if x == y and x < z:
        return print(x, ' is the lesser.')
    if y == z and y < x:
        return print(y, ' is the lesser.')
    if z == x and z < y:
        return print(z, ' is the lesser.')


# The program receives three numbers and returns the lesser.
print('Lets find out which is the lesser between three numbers.')
f_num = float(input('Insert the first one.\n'))
s_num = float(input('Now, insert the second number.\n'))
t_num = float(input('And the third number.\n'))

# If the numbers are the same, it informs at the terminal.
if f_num == s_num == t_num:
    print('They are the same number. ')

# If they are different, it calls the function to compare and return with the answer.
else:
    the_lesser(f_num, s_num, t_num)

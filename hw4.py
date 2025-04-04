def draw_line_string(name):
    msg1 = " Hello " + name
    msg2 = " Welcome to Seoul."
    return msg1, msg2

def rep_char(c, n):
    print(c * n)

name = input("Input his/her name : ")

msg1, msg2 = draw_line_string(name)
nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2) 
rep_char("-", nstr)
print(msg1)
print(msg2)
rep_char("-", nstr)
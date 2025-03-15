def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(r):
    extent_num = r*r*3.14
    print("반지름 ",r,"인 원의 넓이 = 3.14 x",r,"x",r,"=",extent_num)

get_circle_area(get_radius("넓이를 구하고자 하는 원의 반지름은?"))

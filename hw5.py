#개념확인 과제 (연습문제 7.6)

def read_single_digit(num):
    if num == 1:
        return "일"
    elif num == 2:
        return "이"
    elif num == 3:
        return "삼"
    elif num == 4:
        return "사"
    elif num == 5:
        return "오"
    elif num == 6:
        return "육"
    elif num == 7:
        return "칠"
    elif num == 8:
        return "팔"
    elif num == 9:
        return "구"
    elif num == 0:
        return "영"

def read_number(lang):
    hangle = []
    for i in range(len(lang)):
        hangle.append(read_single_digit(int(lang[i])))
        i=i+1
    return hangle


num = input("세 자리 정수 입력 : ")
result = read_number(num)
print(" ".join(result)) #join활용해 " "로 연결함
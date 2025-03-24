#개념 확인 과제 연습문제 4.7
#사용자로부터 입력된 금액을 동전으로 교환하고자 할 때 동전별 교환 갯수 확인

def exchange(mony):
    mony1 = mony
    m500 = mony // 500
    m100 = (mony%500)//100
    m50 = ((mony%500)%100)//50
    m10 = (((mony%500)%100)%50)//10
    print("500원 동전의 개수:",m500,"\n100원 동전의 개수:",m100,"\n50원 동전의 개수:",m50,"\n10원 동전의 개수:",m10)


def get_integer(prompt):
    mony = int(input(prompt))
    return mony


exchange(get_integer("동전으로 교환하고자 하는 금액은?"))
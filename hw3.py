#연습문제5.5 과제

def get_fixed_price(persent, price):
    real_price = int((price/(100-persent))*persent + price)
    print("상품의 정가는 ",real_price,"원")

persent = int(input("할인율은?"))
price1 = int(input("A 상품의 할인된 가격은?"))
price2 = int(input("B 상품의 할인된 가격은?"))

get_fixed_price(persent, price1)
get_fixed_price(persent, price2)

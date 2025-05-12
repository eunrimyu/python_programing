#연습문제 9.4
#상품명에 엔터 치면 구입 종료

shopping_bag = {}

#구입
while True:
    item = input('상품명?')
    if item == "" or item == '\n':
        break
    count = int(input('수량은?'))
    print(f'장바구니에 {item} {count}개가 담겼습니다.')
    shopping_bag[item] = count

#장바구니 보기
print(f' >>> 장바구니 보기 : {shopping_bag}')

#검색
print('[검색]')
it = input('장바구니에서 확인하고자 하는 상품은?')
if it in shopping_bag:
    print(f'{it}(는) {shopping_bag[it]}개 담겨있습니다.')
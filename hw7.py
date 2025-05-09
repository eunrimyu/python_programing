#쇼핑몰 장바구니 시뮬레이션 프로그램 작성
shopping_bag = {}  # 장바구니

# [구입] 단계
while True:
    item = input("상품명? ")
    if item == "":
        break
    count = int(input("수량은? "))  # 수량은 숫자로 저장
    print(f"장바구니에 {item} {count}개가 담겼습니다.")
    shopping_bag[item] = count

# 장바구니 출력
print(f">>> 장바구니 보기 : {shopping_bag}")

# [검색] 단계
print("[검색]")
it = input("장바구니에서 확인하고자 하는 상품은? ")
if it in shopping_bag:
    print(f"{it}은(는) {shopping_bag[it]}개 담겨 있습니다.")
else:
    print(f"{it}은(는) 장바구니에 없습니다.")

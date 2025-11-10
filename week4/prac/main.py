import os
from prac import Menu, Order, Manage

cafe_menu = Menu()
cafe_order = Order(cafe_menu)
cafe_manage = Manage(cafe_menu)

# 2. 메인 루프 실행
while True:
    print("\n** 원하는 작업을 선택하세요: [1. 주문 | 2. 재고 관리 | 3. 종료] **")
    choice = input("> ")
    
    if choice == '1':
        cafe_order.orderMenu()
        
    elif choice == '2':
        cafe_manage.Management()
        
    elif choice == '3':
        # 종료 시 총 매출액을 출력하고 종료
        print("---")
        cafe_manage.totalSale()
        print("프로그램을 종료합니다.")
        break
        
    else:
        print("잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")
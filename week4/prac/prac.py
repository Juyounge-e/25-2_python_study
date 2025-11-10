import os

file_path = "./week4/cafe.txt"
if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("커피:3000:10\n")
        f.write("라떼:4000:5\n")
        f.write("스무디:4500:3\n")


# 🚀 미션 1: 메뉴판 만들기 (Menu 클래스)
class Menu:
    
    def __init__(self):
        self.orderList = {}  
        self.total = 0       
        
        # 생성자 호출 시 파일에서 메뉴를 읽어옴
        with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        name, price, stock = line.split(":")
                        self.orderList[name] = {'가격': int(price), '재고': int(stock)}

    def printMenu(self):
        print("--- Menu ---")
        # 딕셔너리를 리스트로 변환하여 인덱싱 
        menu_items = list(self.orderList.items())
        for i in range(len(menu_items)):
            name, details = menu_items[i]
            print(f"{i+1}. {name}: {details['가격']}원, 재고: {details['재고']}")
        print("---")

    def addMenu(self):
        name = input("추가할 메뉴 이름: ")

        if name in self.orderList:
            print("이미 존재하는 메뉴입니다.")
            return

        try:
            price = int(input("메뉴 가격: "))
            stock = int(input("초기 재고: "))
            
            self.orderList[name] = {'가격': price, '재고': stock}

            with open(file_path, "a", encoding="utf-8") as f:
                f.write(f"\n{name}:{price}:{stock}")
            
            print(f"'{name}' 메뉴가 성공적으로 추가되었습니다.")
            
        except ValueError:
            print("가격과 재고는 숫자로 입력해야 합니다.")


# 🚀 미션 2: 주문 시스템 만들기 (Order 클래스)
class Order:

    def __init__(self, menu_instance):
        self.menu = menu_instance  
        self.orderResult = []     

    def orderMenu(self):
        # self.menu.orderList.items()는 딕셔너리 뷰 객체이므로 리스트로 변환
        menu_items = list(self.menu.orderList.items())
        
        while True:
            self.menu.printMenu()
            
            user_input = input("주문할 메뉴 번호를 입력하세요 (종료: end): ")

            if user_input.lower() == 'end':
                break
            
            try:
                menu_num = int(user_input)
                
                if 1 <= menu_num <= len(menu_items):
                    name, details = menu_items[menu_num - 1]
                    
                    if details['재고'] == 0:
                        print(f"'{name}'은(는) 품절되었습니다.")
                    else:
                        print(f"'{name}' 1개가 주문되었습니다.")
                        details['재고'] -= 1  
                        price = details['가격']# Menu 클래스의 총 매출 증가
                        self.orderResult.append((name, price))
                
                else:
                    print("존재하지 않는 메뉴입니다.")
                    
            except ValueError:
                print("유효한 숫자를 입력하거나 'end'를 입력하세요.")

        if self.orderResult:
            total_quantity = len(self.orderResult)
            total_price = sum([price for name, price in self.orderResult])
            
            print("---")
            print(f"총 주문 수량: {total_quantity}개")
            print(f"총 주문 금액: {total_price}원")
        
        self.orderResult = []


# 🚀 미션 3: 재고 및 매출 관리 시스템 완성하기
class Manage:
    def __init__(self, menu_instance):
        self.menu = menu_instance 

    def Management(self):
        print("--- 재고 관리 ---")
        print("현재 재고 상태입니다.")
        self.menu.printMenu()
        
        menu_items = list(self.menu.orderList.items())
        
        while True:
            user_input = input("재고를 추가할 메뉴 번호를 입력하세요 (종료: end): ")
            
            if user_input.lower() == 'end':
                print("재고 관리를 종료하고 메인 메뉴로 돌아갑니다.")
                break
                
            try:
                menu_num = int(user_input)
                
                if 1 <= menu_num <= len(menu_items):
                    name, details = menu_items[menu_num - 1]
                    
                    try:
                        stock_to_add = int(input("추가할 수량을 입력하세요: "))
                        if stock_to_add < 0:
                            print("0 이상의 수량을 입력하세요.")
                            continue
                            
                        details['재고'] += stock_to_add
                        print(f"'{name}'의 재고가 {stock_to_add}개 추가되었습니다.")
                        
                        self.menu.printMenu()

                    except ValueError:
                        print("수량은 숫자로 입력해야 합니다.")
                else:
                    print("존재하지 않는 메뉴입니다.")
            
            except ValueError:
                print("유효한 숫자를 입력하거나 'end'를 입력하세요.")

    def totalSale(self):
        print(f"현재까지의 총 매출액은 {self.menu.total}원입니다.")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # 메서드: 책 정보를 형식에 맞게 출력
    def display_info(self):
        print(f"제목: {self.title}, 저자: {self.author}")


book1 = Book("일반수학2", "김인덕")
book2 = Book("의사소통 영어", "박비룡")

book1.display_info()
book2.display_info()

def greet(name, msg="안녕하세요!"):
    print(f"{name}님, {msg}")

# 1. msg 매개변수를 전달하지 않는 경우
greet("김인덕")

# 2. msg 매개변수를 전달하는 경우
greet("이비룡", "반갑습니다!")
import random

answer = random.sample(range(10), 3)

attempts = 0
print("컴퓨터가 숫자를 생성했습니다. 답을 맞춰보세요!")
print(answer) # 정답 출력용

# 2. 게임 루프 시작
while True:
    attempts += 1

    user_input = input(f"{attempts}번째 시도: ")
    guess = [int(digit) for digit in user_input]

    strike_count = 0
    ball_count = 0
    out_count = 0

    for i in range(3):
        if guess[i] == answer[i]:
            # Strike: 숫자와 위치가 모두 맞을 경우
            strike_count += 1
        elif guess[i] in answer:
            # Ball: 숫자는 맞지만 위치가 틀릴 경우
            ball_count += 1
        else:
            # Out: 숫자와 위치 모두 틀린 경우
            out_count += 1

    print(f"{strike_count} Strike, {ball_count} Ball, {out_count} Out")

    if strike_count == 3:
        print(f"축하합니다! {attempts}번 만에 정답을 맞추셨습니다!")
        break
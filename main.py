def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    print("더하기/빼기 프로그램입니다.")

    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    operation = input("연산을 선택하세요 (+ 또는 -): ")

    if operation == "+":
        result = add(num1, num2)
        print(f"결과: {num1} + {num2} = {result}")
    elif operation == "-":
        result = subtract(num1, num2)
        print(f"결과: {num1} - {num2} = {result}")
    else:
        print("잘못된 연산을 선택하셨습니다.")


if __name__ == "__main__":
    main()

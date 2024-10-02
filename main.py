def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "0으로 나눌 수 없습니다."


def main():
    print("더하기/빼기/곱하기/나누기 프로그램입니다.")

    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    operation = input("연산을 선택하세요 (+, -, *, /): ")

    if operation == "+":
        result = add(num1, num2)
        print(f"결과: {num1} + {num2} = {result}")
    elif operation == "-":
        result = subtract(num1, num2)
        print(f"결과: {num1} - {num2} = {result}")
    elif operation == "*":
        result = multiply(num1, num2)
        print(f"결과: {num1} * {num2} = {result}")
    elif operation == "/":
        result = divide(num1, num2)
        print(f"결과: {num1} / {num2} = {result}")
    else:
        print("잘못된 연산을 선택하셨습니다.")


if __name__ == "__main__":
    main()

    print("이것은 branch1에서 수정된 내용입니다.")

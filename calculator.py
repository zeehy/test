def add(a, b):
    return a+b


def subtract(a, b):
	return a-b

def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


def pow(a, b):
    return a**b


def abs(a):
    return a if a>=0 else -a 


def mod(a, b):
    return a % b


if __name__ == "__main__":
    # 간단한 테스트 코드
    print("abs (-5): ", abs(-5))

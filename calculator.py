def add(a, b):
    c=a+b
    return c


def subtract(a, b):
	pass


def multiply(a, b):
    pass


def divide(a, b):
    if b!=0:
        return a/b
    else:
        return print("Error")


def pow(a, b):
    return a**b
    


def abs(a):
    return abs(a)


def mod(a, b):
    return a%b


if __name__ == "__main__":
    # 간단한 테스트 코드
    a=100
    b=77
    print(mod(a,b))

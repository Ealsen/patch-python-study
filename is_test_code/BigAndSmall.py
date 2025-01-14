import random

def VS_big_small():
    """ 可以用于大小比较 """
    a = 50
    b = 0
    b = random.randint(1,101)
    print(f"{a}比{b}")
    if a > b:
        print("big")
    elif a < b:
        print("small")
    else:
        print("re")

if __name__ == '__main__':
    VS_big_small()
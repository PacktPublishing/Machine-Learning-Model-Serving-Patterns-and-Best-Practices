def fun(x):
    import random
    y = round(10*random.random())
    return x + y


if __name__ == "__main__":
    print(fun(5)) # fun can return any number from 5 to 15 for the same input 5

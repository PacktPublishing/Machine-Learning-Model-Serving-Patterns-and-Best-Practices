class Counter:
    count = 0

    def __init__(self):
        pass

    def current_count(self):
        Counter.count += 1
        return Counter.count

if __name__=="__main__":
    counter = Counter()
    print(counter.current_count()) # This call prints 1
    print(counter.current_count()) # This call prints 2
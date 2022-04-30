class Counter:

    def __init__(self):
        pass

    def current_count(self, prev_count):
        return prev_count + 1

if __name__=="__main__":
    counter = Counter()
    print(counter.current_count(1)) # Now the call does not depend on any previous call
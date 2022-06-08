import threading
import random
import time

threadLock = threading.Lock()

def predict(data):
    size = len(data) // 2
    thread1 = Predictor("Predictor 1", data[:size], 0)
    thread2 = Predictor("Predictor 2", data[size:], size)
    global result
    result = []
    threads = [thread1, thread2]
    thread1.start()
    thread2.start()
    for thread in threads:
        thread.join()
    return result


def combine_result(response):
    result.append(response)


class Predictor(threading.Thread):

    def __init__(self, threadName, data, start_index):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.data = data
        self.labels = []
        self.start_index = start_index
        self.truth = [10, 11, 12, 13]

    def run(self) -> None:
        print("Predicting labels for ", self.data)
        sleepTime = random.randint(0, 10)
        print("Sleeping for ", sleepTime, " s\n")
        time.sleep(sleepTime)
        threadLock.acquire()
        self.labels = self.truth[self.start_index:self.start_index + 2]
        combine_result(self.labels)
        threadLock.release()
        print("Predicting done:", self.data, " are predicted as ", self.labels)


if __name__ == "__main__":
    data = [[1], [2], [3], [4]]
    pred = predict(data)
    print("Prediction is ", pred)

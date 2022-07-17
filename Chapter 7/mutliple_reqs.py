import queue

Q = queue.Queue()
class Request:
    def __init__(self, id, data):
        self.id = id
        self.data = data

def update_model(request):
    Q.put(request)
    if(Q.qsize() >= 3):
        print("Now the model is going to update")
        while Q.qsize() > 0:
            req = Q.get()
        print("After training the queue size now: ", Q.qsize())
    else:
        print("Not going to update yet")

request1 = Request("id1", [[1, 1]])
update_model(request1)
request2 = Request("id2", [[1, 1]])
update_model(request2)
request3 = Request("id3", [[2, 2]])
update_model(request3)

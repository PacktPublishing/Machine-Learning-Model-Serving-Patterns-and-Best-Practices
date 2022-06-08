truths = [10, 11, 12, 13]
import asyncio
import random


class Model:
    def __init__(self, name):
        self.name = name

    def predict(self, X, index):
        n = len(X)
        Y = truths[index: (index + n)]
        return Y

async def predict(modelName, data, model: Model, response):
    sleepTime = random.randint(0, 10)
    await asyncio.sleep(sleepTime)
    (x, i) = data
    print(f"Prediction by {modelName} for: {x}")
    y = model.predict(x, i)
    print(f"The response for {x} is {y}")
    await response.put(y)

async def server():
    X = [[1], [2], [3], [4]]
    responses = asyncio.Queue()
    model1 = Model("Model 1")
    model2 = Model("Model 2")
    model3 = Model("Model 3")
    model4 = Model("Model 4")
    await asyncio.gather(
        asyncio.create_task(predict("Model 1", (X[0], 0), model1, responses)),
        asyncio.create_task(predict("Model 2", (X[1], 1), model2, responses)),
        asyncio.create_task(predict("Model 3", (X[2], 2), model3, responses)),
        asyncio.create_task(predict("Model 4", (X[3], 3), model4, responses))
    )
    print(responses)

if __name__ == "__main__":
    asyncio.run(server())



import ray
from ray import serve
from ray.serve.dag import InputNode
from ray.serve.drivers import DAGDriver
@serve.deployment
def Step1(inp: str) -> str:
    print("I am inside step 1")
    return f"{inp}_step1"

@serve.deployment
def Step2(inp: str) -> str:
    print("I am inside step 2")
    return f"{inp}_step2"

@serve.deployment
def Step3(inp: str) -> str:
    print("I am inside step 3")
    return f"{inp}_step3"

@serve.deployment
def Step4(inp: str) -> str:
    print("I am inside step 4")
    return f"{inp}_step4"


@serve.deployment
class Model:
    def __init__(self):
        self.model = lambda x : f"{x}_predict"

    def predict(self, inp: str) -> str:
        print("I am inside predict method")
        return self.model(inp)


with InputNode() as input:
    model = Model.bind()
    step1 = Step1.bind(input)
    step2 = Step2.bind(step1)
    step3 = Step3.bind(step2)
    step4 = Step4.bind(step3)
    output = model.predict.bind(step4)
    serve_dag = DAGDriver.bind(output)

handle = serve.run(serve_dag)
print(ray.get(handle.predict.remote("hello")))

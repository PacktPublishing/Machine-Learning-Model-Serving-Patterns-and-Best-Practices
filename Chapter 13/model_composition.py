import ray
from ray import serve
from starlette import requests

@serve.deployment
class ModelA:
    def __init__(self):
        self.model = lambda x : x + 5

    async def __call__(self, request):
        data = await request.json()
        x = data['X']
        return self.model(x)

@serve.deployment
class ModelB:
    def __init__(self):
        self.model = lambda x : x * 2

    async def __call__(self, request):
        data = await request.json()
        x = data['X']
        return self.model(x)

@serve.deployment
class Driver:
    def __init__(self, model_a_handle, model_b_handle):
        self._model_a_handle = model_a_handle
        self._model_b_handle = model_b_handle

    async def __call__(self, request):
        ref_a = await self._model_a_handle.remote(request)
        ref_b = await self._model_b_handle.remote(request)
        return (await ref_a) + (await ref_b)


model_a = ModelA.bind()
model_b = ModelB.bind()

driver = Driver.bind(model_a, model_b)

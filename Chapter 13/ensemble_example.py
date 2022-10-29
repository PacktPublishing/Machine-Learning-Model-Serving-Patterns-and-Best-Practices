from ray import serve
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.datasets import make_regression

@serve.deployment
class RandomForestRegressorModel:
    def __init__(self):
        X, y = make_regression(n_features=4, n_informative=2,
                               random_state=0, shuffle=False)
        self.model = RandomForestRegressor(max_depth=2, random_state=0)
        self.model.fit(X, y)

    async def __call__(self, request):
        data = await request.json()
        x = data['X']
        pred = self.model.predict(x)
        print("Prediction from RandomForestRegressor is ", pred)
        return pred

@serve.deployment
class AdaBoostRegressorModel:
    def __init__(self):
        X, y = make_regression(n_features=4, n_informative=2,
                               random_state=0, shuffle=False)
        self.model = AdaBoostRegressor(random_state=0, n_estimators=100)
        self.model.fit(X, y)

    async def __call__(self, request):
        data = await request.json()
        x = data['X']
        pred = self.model.predict(x)
        print("Prediction from AdaBoostRegressor is ", pred)
        return pred

@serve.deployment
class EnsemblePattern:
    def __init__(self, model_a_handle, model_b_handle):
        self._model_a_handle = model_a_handle
        self._model_b_handle = model_b_handle

    async def __call__(self, request):
        ref_a = await self._model_a_handle.remote(request)
        ref_b = await self._model_b_handle.remote(request)
        return ((await ref_a) + (await ref_b))/2.0


model_a = RandomForestRegressorModel.bind()
model_b = AdaBoostRegressorModel.bind()

ensemble = EnsemblePattern.bind(model_a, model_b)

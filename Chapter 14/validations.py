import bentoml
import numpy as np
from bentoml.io import NumpyNdarray
regr_runner = bentoml.sklearn.get("dummyregressionmodel").to_runner()
print(regr_runner)
service = bentoml.Service("DummyRegressionService", runners=[regr_runner])

@service.api(
    input=NumpyNdarray(
        shape=(1, 4),
        enforce_shape=True
    ),
    output=NumpyNdarray(),
    route="/infer"
)
def predict(input: np.ndarray) -> np.ndarray:
    print("input is ", input)
    response = regr_runner.run(input)
    print("Response is ", response)
    return response
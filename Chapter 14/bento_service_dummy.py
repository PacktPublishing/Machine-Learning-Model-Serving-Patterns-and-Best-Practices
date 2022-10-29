import bentoml
import numpy as np
from bentoml.io import NumpyNdarray
regr_runner = bentoml.sklearn.get("dummyregressionmodel").to_runner()
bento_service = bentoml.Service("DummyRegressionService", runners=[regr_runner])

@bento_service.api(
    input=NumpyNdarray(),
    output=NumpyNdarray(),
    route="/bento-infer"
)
def predict(input: np.ndarray) -> np.ndarray:
    print("input is ", input)
    response = regr_runner.run(input)
    print("Response is ", response)
    return response
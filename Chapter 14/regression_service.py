import bentoml
import numpy as np
from bentoml.io import NumpyNdarray
rf_runner = bentoml.sklearn.get("rf").to_runner()
boost_runner = bentoml.sklearn.get("boost").to_runner()
reg_service = bentoml.Service("regression_service", runners=[rf_runner, boost_runner])

@reg_service.api(
    input=NumpyNdarray(),
    output=NumpyNdarray(),
    route="/infer"
)
def predict(input: np.ndarray) -> np.ndarray:
    print("input is ", input)
    rf_response = rf_runner.run(input)
    print("RF response ", rf_response)
    boost_response = boost_runner.run(input)
    print("Boost response ", boost_response)
    avg = (rf_response + boost_response) / 2
    print("Average is ", avg)
    return avg
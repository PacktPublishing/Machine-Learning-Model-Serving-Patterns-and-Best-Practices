import ray
from ray import serve
from ray.serve.dag import InputNode
from ray.serve.drivers import DAGDriver
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

@serve.deployment
def collect_data() -> pd.DataFrame:
    df = pd.DataFrame({"F1": [1, 2, 3, 4, 5, None], "F2": ["C1", "C1", "C2", "C2", "C3", "C4"], "Y": [0, 0, 0, 1, 1, 1]})
    print("DF in the data collection stage")
    print(df)
    return df

@serve.deployment
def data_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    print("DF after the data cleaning stage")
    print(df)
    return df

@serve.deployment
def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    df = pd.get_dummies(df)
    print("DF after the feature engineering stage")
    print(df)
    return df

@serve.deployment
def train(df: pd.DataFrame) -> RandomForestRegressor:
    X = df[["F1", "F2_C1"]]
    y = df["Y"]
    print("Inside training!")
    model = RandomForestRegressor(max_depth=2, random_state=0)
    model.fit(X, y)
    return model

@serve.deployment
def predict(model: RandomForestRegressor, x) -> float:
    print("Inside predict method")
    print("Input is", x)
    return model.predict(x)


with InputNode() as input:
    data_collection = collect_data.bind()
    clean_data = data_cleaning.bind(data_collection)
    feature_creation = feature_engineering.bind(clean_data)
    train_model = train.bind(feature_creation)
    output = predict.bind(train_model, input)
    serve_dag = DAGDriver.bind(output)

handle = serve.run(serve_dag)

print(ray.get(handle.predict.remote([[1 , 1]])))

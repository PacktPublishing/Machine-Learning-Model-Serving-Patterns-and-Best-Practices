from sklearn.cluster import MiniBatchKMeans
import numpy as np

X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 0], [4, 4],
              [4, 5], [0, 1], [2, 2],
              [3, 2], [5, 5], [1, -1]])

kmeans = MiniBatchKMeans(n_clusters=2,
                         random_state=0,
                         batch_size=6).fit(X)

def update_model(X):
    global kmeans
    kmeans = kmeans.partial_fit(X)
    print("New Cluster centers are")
    print(kmeans.cluster_centers_)


def predict(X):
    # Train the model first
    update_model(X)
    predictions = kmeans.predict(X)
    print(predictions)

if __name__ == "__main__":
    predict([[0, 0], [4, 4]])
    predict([[1, 0], [1, 4]])
    predict([[0, 1], [2, 4]])
    predict([[0, 3], [3, 4]])
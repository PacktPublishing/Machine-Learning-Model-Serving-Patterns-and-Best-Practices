from sklearn.cluster import MiniBatchKMeans
import numpy as np

X = np.array([[0, 0], [0, 1]])

kmeans = MiniBatchKMeans(n_clusters=2,
                         random_state=0,
                         batch_size=6).fit(X)
print("Initial cluster centers")
print(kmeans.cluster_centers_)

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
    predict([[0, 0], [0, 1]])
    predict([[10, 10], [10, 15]])
    predict([[10, 11], [11, 15]])
    predict([[11, 10], [11, 14]])
    predict([[0, 0], [0, 1]])

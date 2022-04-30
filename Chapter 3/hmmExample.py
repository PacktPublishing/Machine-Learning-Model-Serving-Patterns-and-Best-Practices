import numpy as np
from hmmlearn import hmm
# model = hmm.GaussianHMM(n_components=3, covariance_type="full")
# model.startprob_ = np.array([0.6, 0.3, 0.1])
# model.transmat_ = np.array([[0.7, 0.2, 0.1],
#                             [0.3, 0.5, 0.2],
#                             [0.3, 0.3, 0.4]])
# model.means_ = np.array([[0.0, 0.0], [3.0, -3.0], [5.0, 10.0]])
# model.covars_ = np.tile(np.identity(2), (3, 1, 1))
# X, Z = model.sample(100)
#
# remodel = hmm.GaussianHMM(n_components=3, covariance_type="full", n_iter=100)
# remodel.fit(X)
#
# print(X)
# print(Z)
#
# Z2 = remodel.predict(X)
# print(Z2)
X = np.array([
    [6.01337858e+00, 9.89064033e+00],
    [ 4.09530509e+00,  1.01998433e+01],
    [4.57725764e+00,  1.03085986e+01]
]
)
import pickle
# with open("filename.pkl", "wb") as file: pickle.dump(remodel, file)
with open("filename.pkl", "rb") as file:
    data: hmm.GaussianHMM = pickle.load(file)

    print(data.startprob_)
    print(data.predict(X))

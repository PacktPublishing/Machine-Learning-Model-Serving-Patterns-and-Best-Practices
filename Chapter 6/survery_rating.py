import numpy as np
users = ["A", "B", "C", "D", "E"]
w1 = np.array([5, 5, 5, 5, 5])
w2 = np.array([5, 4, 4, 5, 5])
w3 = np.array([4, 4, 4, 4, 4])
w4 = np.array([3, 3, 4, 4, 4])
w5 = np.array([3, 3, 3, 3, 3])

def check_any_less_than_3(rating):
    mappedArray = rating <= 3
    return mappedArray.any()

print("Checking when first rating <= 3 appears")
print(check_any_less_than_3(w1))
print(check_any_less_than_3(w2))
print(check_any_less_than_3(w3))
print(check_any_less_than_3(w4))
print(check_any_less_than_3(w5))

def check_average(rating):
    mean = np.mean(rating)
    return mean <= 4.0

print("Checking when average rating becomes <= 4.0")
print(check_average(w1))
print(check_average(w2))
print(check_average(w3))
print(check_average(w4))
print(check_average(w5))

def check_median(rating):
    median = np.median(rating)
    return median <= 3.0

print("Checking when the median becomes <= 3.0")
print(check_median(w1))
print(check_median(w2))
print(check_median(w3))
print(check_median(w4))
print(check_median(w5))

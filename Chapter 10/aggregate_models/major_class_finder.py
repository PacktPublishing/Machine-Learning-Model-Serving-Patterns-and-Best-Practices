from collections import Counter

x = ['C1', 'C1', 'C1', 'C2', 'C2', 'C3', 'C3']
counts = Counter(x)
print("Counts of different elements", counts)
major_element = counts.most_common(1)[0][0]
print("Major element", major_element)

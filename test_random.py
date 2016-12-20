import CorrCoef as c
import numpy as np
v = np.random.rand(5,9)

first = c.Pearson(v,4)[0]
for i in range(1000):
    assert first == c.Pearson(v,4,1)[0], "Found different value"

for i in range(1000):
    c.Pearson(v,4,.9)

print("Success!")

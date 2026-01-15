
# Perzeptron function
def hFunction(w, x):
    if not (isinstance(w, tuple) and isinstance(x, tuple)):
        raise TypeError("w und x müssen Tupel sein")
    if (len(w) + len(x)) != 5:
        raise ValueError("w und x müssen gleich lang sein")
    result = w[0] + w[1] * x[0] + w[2] * x[1]
    return sign(result)

# Sign function
def sign(result):
    if result < 0:
        return 0
    return 1

print(hFunction((1,1,1),(1,1)))
print(hFunction((-2,1,1),(0,0)))
print(hFunction((-2,1,1),(0,1)))
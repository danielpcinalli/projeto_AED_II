
def hashFunction(value):
    hashValue = hash(value)
    hashValue = abs(hashValue)//1000000000000000
    return hashValue

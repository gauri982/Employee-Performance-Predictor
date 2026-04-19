import numpy as np

def predict(model):
    sample = np.array([[30, 5, 50000, 40, 80]])
    return model.predict(sample)
import pickle
import warnings
import numpy as np

warnings.filterwarnings("ignore")


class MlModel:
    def __init__(self, P, G, BP, ST, I, BMI, DP, AGE):
        self.P = P
        self.G = G
        self.BP = BP
        self.ST = ST
        self.I = I
        self.BMI = BMI
        self.DP = DP
        self.AGE = AGE

    def predict(self):
        filename = 'model.pickle'
        model = pickle.load(open(filename, 'rb'))
        value = np.array([[self.P, self.G, self.BP, self.ST, self.I, self.BMI, self.DP, self.AGE]])
        predict = model.predict(value)

        return predict[0]



from flask import Flask , jsonify, request, render_template,json
import pickle
import numpy as np
import config
app = Flask(__name__)


class LinearModel:
    def __init__(self,total_bill,sex,day,time,smoker,size):
        self.total_bill = total_bill
        self.sex = sex
        self.day = day
        self.time = time
        self.smoker = smoker
        self.size = size

    def get_pickel(self):
        self.p = pickle.load(open(config.model_file_path    , 'rb'))
        self.j = json.load(open(config.json_path , 'r'))

    
    def get_details(self):
        self.get_pickel()
        test_array = np.zeros(len(self.j['column']))

        test_array[0] = self.total_bill
        test_array[1] = self.sex
        test_array[2] = self.day               
        test_array[3] = self.time
        test_array[4] = self.smoker
        test_array[5] = self.size

        
        result = np.around(self.p.predict([test_array]), 2)
        return result[0]

if __name__ ==  "__main__":
    waiter_tips = LinearModel(2000,1,2, 0,0,4)    
    waiter_tips.get_details()           
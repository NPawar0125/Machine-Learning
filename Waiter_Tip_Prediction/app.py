from flask import Flask, jsonify, request, render_template
from project_app.utils import LinearModel
import numpy as np
app = Flask(__name__)


@app.route('/', methods = ['GET','POST'])
def homepage():
    print('waiter tips prediction')
    if request.method == 'POST':
        print('We are in POST Method')
        # data = request.form
        total_bill=request.form.get('total_bill')     
        sex= request.form.get('gender')
        day = request.form.get('day')
        time =request.form.get('time')
        size = request.form.get('size')
        smoker = request.form.get('smoker')

        # print(data)
        print(f'total_bill >> {total_bill}, sex >>{sex} , day >> {day}, time >> {time}, smoker >> {smoker} , size >> {size} ')
        waiter_tips = LinearModel(total_bill, sex, day, time, smoker,size)    
        
        return render_template('waiter_tips.html',output=waiter_tips.get_details())
    else:
        return render_template('waiter_tips.html')


        
app.run()
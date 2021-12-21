import sys
import os
import requests
import time
import random
from flask import Flask
from markupsafe import escape
import subprocess
from flask import render_template
app = Flask(__name__)


@app.route('/lunch')
def index():
    data = jturn()
    return f"<p>{data[0]}</p><p>{data[1]}</p><p>{data[2]}</p>"



from flask import render_template
@app.route('/salam')
def salam():
    memory = subprocess.Popen(['date'], stdout=subprocess.PIPE)
    out,error = memory.communicate()
    return render_template('view.html', out=out, error=error)


from __future__ import print_function

@app.route('/button/')
def button_clicked():
   print('Hello world!', file = sys.stderr)
return redirect('/')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def jturn():
    Callcenter = ['Ali', 'Masomeh', 'Reza']
    rand_item = random.sample(Callcenter, 3)
    order_list = []
    for item in rand_item:
        order_list.append(item)
    return order_list


def firstfunc():
    mainfunc = input(
        f'{bcolors.OKBLUE}"Press"{bcolors.ENDC}{bcolors.WARNING}"1"{bcolors.ENDC}{bcolors.OKBLUE}For Using the Tshoot tool{bcolors.ENDC}\n{bcolors.OKBLUE}Press{bcolors.ENDC}{bcolors.WARNING}"2"{bcolors.OKBLUE}To See whose turn is it{bcolors.ENDC}\n\n{bcolors.OKCYAN}What do you wnant to do?{bcolors.ENDC}')
    if mainfunc == '1':
        jtshoot()
    elif mainfunc == '2':
        jturn()
    else:
        print(f'\n{bcolors.Red}You choose poorly! Try again{bcolors.ENDC}\n')


# firstfunc()

if __name__ == '__main__':
    app.run(debug=True)

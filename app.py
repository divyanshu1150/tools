from flask import Flask, render_template, request
from modules import sip, emi, fd, rd, lumpsum

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sip', methods=['GET', 'POST'])
def sip_calc():
    result = None
    if request.method == 'POST':
        p = float(request.form['monthly_investment'])
        r = float(request.form['annual_rate']) / 12 / 100
        n = int(request.form['years']) * 12
        result = round(p * (((1 + r)**n - 1) * (1 + r)) / r)
    return render_template('sip.html', result=result)

@app.route('/emi', methods=['GET', 'POST'])
def emi_calc():
    result = None
    if request.method == 'POST':
        p = float(request.form['loan_amount'])
        r = float(request.form['annual_rate']) / 12 / 100
        n = int(request.form['years']) * 12
        result = round((p * r * ((1 + r)**n)) / (((1 + r)**n) - 1))
    return render_template('emi.html', result=result)

@app.route('/fd', methods=['GET', 'POST'])
def fd_calc():
    result = None
    if request.method == 'POST':
        p = float(request.form['principal'])
        r = float(request.form['rate']) / 100
        n = int(request.form['years'])
        freq = int(request.form['frequency'])
        result = round(p * (1 + r / freq) ** (freq * n))
    return render_template('fd.html', result=result)

@app.route('/rd', methods=['GET', 'POST'])
def rd_calc():
    result = None
    if request.method == 'POST':
        p = float(request.form['monthly_investment'])
        r = float(request.form['annual_rate']) / 100
        n = int(request.form['years']) * 12
        result = round(p * n + p * n * (n + 1) * r / (2400))
    return render_template('rd.html', result=result)

@app.route('/lumpsum', methods=['GET', 'POST'])
def lumpsum_calc():
    result = None
    if request.method == 'POST':
        p = float(request.form['investment'])
        r = float(request.form['rate']) / 100
        n = int(request.form['years'])
        result = round(p * ((1 + r) ** n))
    return render_template('lumpsum.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

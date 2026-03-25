from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/triangle/<type>')
def triangle_page(type):
    return render_template('formula.html', triangle_type=type)

@app.route('/calculate', methods=['POST'])
def calculate():
    triangle_type = request.form.get('triangle_type')
    formula = request.form.get('formula')
    
    try:
        if formula == 'base_height':
            a = float(request.form.get('a'))
            h = float(request.form.get('h'))
            area = (a * h) / 2
        else:
            a = float(request.form.get('a'))
            b = float(request.form.get('b'))
            c = float(request.form.get('c'))
            p = (a + b + c) / 2
            area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        
        return render_template('result.html', area=f"{area:.2f}")
    except:
        return render_template('result.html', area="Ошибка! Проверьте введённые данные.")

if __name__ == '__main__':
    app.run(debug=True)
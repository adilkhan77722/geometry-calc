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
        # ПРЯМОУГОЛЬНЫЙ ТРЕУГОЛЬНИК
        if triangle_type == 'right':
            if formula == 'legs':
                a = float(request.form.get('a'))
                b = float(request.form.get('b'))
                area = (a * b) / 2
            else:  # hypotenuse
                c = float(request.form.get('c'))
                h = float(request.form.get('h'))
                area = (c * h) / 2
        
        # РАВНОБЕДРЕННЫЙ ТРЕУГОЛЬНИК
        elif triangle_type == 'isosceles':
            if formula == 'base_height':
                b = float(request.form.get('b'))
                h = float(request.form.get('h'))
                area = (b * h) / 2
            else:  # side_angle
                a = float(request.form.get('a'))
                angle = float(request.form.get('angle'))
                area = (a**2 * math.sin(math.radians(angle))) / 2
        
        # РАВНОСТОРОННИЙ ТРЕУГОЛЬНИК
        elif triangle_type == 'equilateral':
            a = float(request.form.get('a'))
            area = (a**2 * math.sqrt(3)) / 4
        
        # ПРОИЗВОЛЬНЫЙ ТРЕУГОЛЬНИК
        elif triangle_type == 'scalene':
            if formula == 'base_height':
                a = float(request.form.get('a'))
                h = float(request.form.get('h'))
                area = (a * h) / 2
            else:  # heron
                a = float(request.form.get('a'))
                b = float(request.form.get('b'))
                c = float(request.form.get('c'))
                p = (a + b + c) / 2
                area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        
        return render_template('result.html', area=f"{area:.2f}")
    
    except Exception as e:
        return render_template('result.html', area=f"Ошибка: {e}")

if __name__ == '__main__':
    app.run(debug=True)
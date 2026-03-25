from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Русские названия треугольников
names = {
    'right': 'прямоугольного',
    'isosceles': 'равнобедренного',
    'equilateral': 'равностороннего',
    'scalene': 'произвольного'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/triangle/<type>')
def triangle_page(type):
    return render_template('formula.html', triangle_type=type, triangle_name=names.get(type, type))

@app.route('/calculate', methods=['POST'])
def calculate():
    t = request.form.get('triangle_type')
    f = request.form.get('formula')

    try:
        # Прямоугольный
        if t == 'right':
            if f == 'legs':
                a = float(request.form.get('a'))
                b = float(request.form.get('b'))
                area = (a * b) / 2
            elif f == 'hypotenuse':
                c = float(request.form.get('c'))
                h = float(request.form.get('h'))
                area = (c * h) / 2
            else:
                area = "Неверная формула"

        # Равнобедренный
        elif t == 'isosceles':
            if f == 'base_height':
                b = float(request.form.get('b'))
                h = float(request.form.get('h'))
                area = (b * h) / 2
            elif f == 'side_angle':
                a = float(request.form.get('a'))
                angle = float(request.form.get('angle'))
                area = (a**2 * math.sin(math.radians(angle))) / 2
            else:
                area = "Неверная формула"

        # Равносторонний
        elif t == 'equilateral':
            a = float(request.form.get('a'))
            area = (a**2 * math.sqrt(3)) / 4

        # Произвольный
        elif t == 'scalene':
            if f == 'base_height_scalene':
                a = float(request.form.get('a'))
                h = float(request.form.get('h'))
                area = (a * h) / 2
            elif f == 'heron':
                a = float(request.form.get('a'))
                b = float(request.form.get('b'))
                c = float(request.form.get('c'))
                p = (a + b + c) / 2
                area = math.sqrt(p * (p - a) * (p - b) * (p - c))
            else:
                area = "Неверная формула"

        else:
            area = "Неизвестный тип треугольника"

        return render_template('result.html', area=f"{area:.2f}")

    except Exception as e:
        return render_template('result.html', area=f"Ошибка: {e}")

if __name__ == '__main__':
    app.run(debug=True)
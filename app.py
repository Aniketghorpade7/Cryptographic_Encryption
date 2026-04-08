
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def mandelbrot(width, height, max_iter):
    image = []
    for y in range(height):
        row = []
        for x in range(width):
            zx = 1.5*(x - width/2)/(0.5*width)
            zy = (y - height/2)/(0.5*height)
            c = complex(zx, zy)
            z = 0
            iter = 0
            while abs(z) < 2 and iter < max_iter:
                z = z*z + c
                iter += 1
            row.append(iter)
        image.append(row)
    return image

@app.route("/", methods=["GET","POST"])
def home():
    data = None
    if request.method == "POST":
        width = 200
        height = 200
        max_iter = int(request.form["iter"])
        data = mandelbrot(width, height, max_iter)
    return render_template("index.html", data=data)

app.run(debug=True)

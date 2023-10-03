import numpy as np
import matplotlib.pyplot as plt
import os
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)

app = Flask(__name__)

wsgi_app = app.wsgi_app

def get_plot(py1, py2, py3, py4, py5, px1, px2, px3, px4, px5):
	x1 = px1
	x2 = px2
	x3 = px3
	x4 = px4
	x5 = px5
		
	y1 = py1
	y2 = py2
	y3 = py3
	y4 = py4
	y5 = py5

	vx_min = x1 - 1
	vx_max = x5 + 5

	x = np.array([x1, x2, x3, x4, x5])
	y = np.array([y1, y2, y3, y4, y5])
		
	model.fit(x[:, np.newaxis], y)
	xfit = np.linspace(vx_min, vx_max, 1000)
	yfit = model.predict(xfit[:, np.newaxis])
	
	plt.scatter(x, y)
	plt.plot(xfit, yfit, '-r')
	plt.xlabel('Year')
	plt.ylabel('Emission')
	return plt

@app.route('/', methods = ['GET','POST'])

def index():
	the_form = request.form
	emi_1 = ''
	year_1 = ''
	emi_2 = ''
	year_2 = ''
	emi_3 = ''
	year_3 = ''
	emi_4 = ''
	year_4 = ''
	emi_5 = ''
	year_5 = ''

	if request.method == 'POST':
		emi_1 = the_form["emissions_1"]
		year_1 = the_form["year_1"]
		int_py1 = int (emi_1)
		int_px1 = int (year_1)
		emi_2 = the_form["emissions_2"]
		year_2 = the_form["year_2"]
		int_py2 = int (emi_2)
		int_px2 = int (year_2)
		emi_3 = the_form["emissions_3"]
		year_3 = the_form["year_3"]
		int_py3 = int (emi_3)
		int_px3 = int (year_3)
		emi_4 = the_form["emissions_4"]
		year_4 = the_form["year_4"]
		int_py4 = int (emi_4)
		int_px4 = int (year_4)
		emi_5 = the_form["emissions_5"]
		year_5 = the_form["year_5"]
		int_py5 = int (emi_5)
		int_px5 = int (year_5)
		plot = get_plot(int_py1, int_py2, int_py3, int_py4, int_py5, int_px1, int_px2, int_px3, int_px4, int_px5)
		plot.savefig(os.path.join('static', 'images', 'plot.png'))
		return render_template("/result.html", emi_1 = emi_1, emi_2 = emi_2, emi_3 = emi_3, emi_4 = emi_4, emi_5 = emi_5, year_1 = year_1, year_2 = year_2, year_3 = year_3, year_4 = year_4, year_5 = year_5)

	return render_template("/index.html", emi_1 = emi_1, emi_2 = emi_2, emi_3 = emi_3, emi_4 = emi_4, emi_5 = emi_5, year_1 = year_1, year_2 = year_2, year_3 = year_3, year_4 = year_4, year_5 = year_5)

if __name__ == '__main__':

	app.run(debug=True)
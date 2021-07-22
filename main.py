from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
	"""Burasi ana sayfadir"""
	# template'deki index.html sayfasina yonlendirebilirsiniz
	return render_template('index.html', **locals())
	# veya isterseniz basit sekilde asagidaki gibi girebilirsiniz
	# return 'Hello World!'


@app.route('/sayfa1')
def sayfa1():
	"""Ozel sayfalar duzenleyebilirsiniz."""
	# template'deki sayfa.html sayfasina yonlendirebilirsiniz
	return render_template('sayfa.html', **locals())
	# veya isterseniz basit sekilde asagidaki gibi girebilirsiniz
	# return "Sayfa1'e hos geldiniz."


@app.route('/sayfa2/<ozelSayfa>')
def sayfa2(ozelSayfa):
	"""Ozel sayfalar duzenleyebilirsiniz."""
	# template'deki sayfa.html sayfasina yonlendirebilirsiniz
	return render_template('sayfa.html', **locals())
	# veya isterseniz basit sekilde asagidaki gibi girebilirsiniz
	# return "Sayfa2/%s sayfasina hos geldiniz." % ozelSayfa


@app.errorhandler(404)
def page_not_found(e):
	"""404 sayfalari bu fonksiyona yonlenir"""
	# template'deki 404.html sayfasina yonlendirebilirsiniz
	return render_template('404.html', **locals()), 404
	# veya isterseniz basit sekilde asagidaki gibi girebilirsiniz
	# return 'Boyle bir sayfa bulunamadi!', 404


# sanal sunucu veya pc'de localhost ile calistirmak icin,
if __name__ == "__main__":
	app.run("0.0.0.0", port=80)
	
	
	
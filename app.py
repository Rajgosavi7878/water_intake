from flask import Flask,request,render_template
from pickle import load

with open("model_water","rb") as f:
	model = load(f)

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def water():
	msg = ""
	if request.method == "POST":
		bw = float(request.form["bw"])
		dwi = float(request.form["dwi"]) 
		

		gender = request.form["gender"]
		if gender == "female":
			d2 = [1,0]
		else:
			d2 = [0,1]

		country = request.form["country"]
		if country == "india":
			d3 = [1,0,0]
		elif country == "uk":
			d3 = [0,1,0]
		else:
			d3 = [0,0,1]

		d1 = [bw,dwi]
		d = [d1 + d2 + d3]
		ans = model.predict(d)
		msg = " Predicted Result = "+ str(ans[0])
		return render_template("home.html",msg=msg,bw=bw,dwi=dwi)
	else:
		return render_template("home.html")
		

if __name__ == "__main__":
	app.run(use_reloader=True,debug=True)
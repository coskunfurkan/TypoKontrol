from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main():
	input_data = request.args.get('jsdata')

	if request.method == 'POST':
		pass
	elif input_data != None:
		return input_data
	else:
		return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)
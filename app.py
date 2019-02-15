import os
from flask import Flask, render_template, request
from modules.breed import predict
from werkzeug.utils import secure_filename

app = Flask(__name__)
# searching for path to current directory assigning it to Global variable
UPLOAD_FOLDER =	os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = set(['jpg', 'png'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def breed():
	result = ''

	if request.method == 'POST':
		if 'dog_name' not in request.files:
			print('no file in request.files')

		#requesting data from html input name
		file = request.files['dog_name']
		# request.files[#name]
		# request.save
		if file:
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		

		result = predict(filename)
	return render_template('index.html', result=result)


if __name__ == "__main__":
	app.run(debug=True)
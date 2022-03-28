import pandas as pd
from flask import Flask, render_template, request
import random

# Initiate Flask App
app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

## Add data part
missfrance = pd.read_csv('../missfrance4flask/miss_france.csv')
# print(missfrance[missfrance['year'] == 2022].iloc[0].to_dict())
# {'year': 2022, 'name': 'Diane Leyre', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Miss_France_2022_Diane_Leyre_1.jpg/90px-Miss_France_2022_Diane_Leyre_1.jpg'}

## Make App working
@app.route("/")
def landing_page():
    return render_template('landing_page.html')

@app.route("/choose_miss")
def choose_year():
    return render_template('choose_miss.html')

@app.route('/go_to_miss', methods=['GET', 'POST'])
def go_to_miss():
  if request.method == 'POST':

    if request.form['year'] not in missfrance['year'].apply(str).unique():
        return render_template('wrong_miss.html')
        
    else:  
        miss = missfrance[missfrance['year'] == int(request.form['year'])].iloc[0].to_dict()

    # Send data to the next page
        return render_template('result_page.html', miss_data = miss)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)
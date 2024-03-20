from flask import Flask, render_template, request, redirect, url_for
from forms import DataCollectionForm  # Importing the form class
import uuid  # Importing the uuid module for generating random IDs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Setting up a secret key for the app

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for displaying information
@app.route('/information')
def information():
    return render_template('information.html')

# Route for data collection form
@app.route('/data-collection', methods=['GET', 'POST'])
def data_collection():
    form = DataCollectionForm()  # Creating an instance of the form
    if form.is_submitted():  # Checking if the form is submitted
        # Generating a random ID for the form submission
        submission_id = str(uuid.uuid4())
        # Here you can handle form submission and data storage
        with open('data.txt', 'a') as file:  # Opening a file to store form data
            file.write(f"Form Submission ID: {submission_id}\n")
            for field_name, field_value in form.data.items():  # Writing form data to the file
                file.write(f"{field_name.capitalize().replace('_', ' ')}: {field_value}\n")
            file.write('\n')  # Adding a new line for the next form submission
        return redirect(url_for('submitted'))  # Redirecting to the submitted page after successful form submission
    return render_template('data-collection.html', form=form)  # Rendering the data collection form template

# Route for displaying submitted page
@app.route('/submitted')
def submitted():
    return render_template('submitted.html')  # Rendering the submitted page template

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=0)  # Running the app in debug mode and assigning a random port
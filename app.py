# Import library and packages 
from flask import Flask, render_template

# Create our application
app = Flask(__name__)

# Create our routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template ('aboutpage.html')


#Start our application
if __name__ == "__main__":
    app.run(debug=True)  
    
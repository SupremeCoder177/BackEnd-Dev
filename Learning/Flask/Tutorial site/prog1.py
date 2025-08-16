# Trying Flask for the first time

# watched the Flask Tutorial by Corey Schafer on youtube

from flask import Flask, render_template

# the app variable is the object which handles the request routing
app = Flask(__name__)


posts = [
	{
		'author' : "John Doe",
		"title" : "Blog post 1",
		"content" : "First post content",
		'date_posted' : "April 20th 2018"
	},
	{
		'author' : "Mary Jane",
		"title" : "Blog post 2",
		"content" : "Second post content",
		'date_posted' : "April 21th 2018"
	}
]

# this means that all requests to / and /home will be routed to this function
@app.route("/")
@app.route("/home")
def hello():
	# return "<h1>Home Page</h1>"

	# render_template returns a html document
	return render_template('home.html', posts=posts)



@app.route("/about")
def about():
	# return "<h1>About Us</h1>"
	return render_template('about.html', title="About")



if __name__ == '__main__':
	# debug is set to true so that we can see changes 
	# without needing to turn off the server
	app.run(debug = True)
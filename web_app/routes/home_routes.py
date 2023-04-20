
from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
  #  return "Welcome Home, let's talk about your living situation here."
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
   # return "You ain't nothin at all"
    return render_template("about.html")

@home_routes.route("/hello")
def hello_world():
    print("Get off my lawn")

    url_params = dict(request.args)
    print("URL PARAMS:", url_params) #> can be empty like {} or full of params like {"name":"Harper"}

    # compile message using specified "name" url parameter or a default value:
    name = url_params.get("You a real POS") or "You a real POS"
    message = f"Sup, {name}!"

   # return message
    return render_template("hello.html", message=message, other="Jea")

# @app.route("/hello")
def hello():
    return "Hello, World!"


# @app.route("/hello/<name>")
def hello_name(name, lastname):
    return "Bonjour, %s!" % name + " " + lastname

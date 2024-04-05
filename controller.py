# @app.route("/hello")
def hello():
    return "Hello, World!"


# @app.route("/hello/<name>")
def hello_name(name):
    return "Hello, %s!" % name

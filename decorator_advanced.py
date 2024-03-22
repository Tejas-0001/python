class User:

    def __init__(self,name):
        self.name = name
        self.is_logged_in = False

def logging_decorator(function):
    def wrapper(*args):
        print(f"function name: {function.__name__}\nArguments passed : {args}")
        function(args[0])
    return wrapper

def is_authenticated(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in is True:
            function(args[0])
    return wrapper
"""here we see that argument of the function needs to be passed but wrapper function only takes function,
so to solve this we use *args and **kwargs"""
@is_authenticated
def create_blog(user):
    print(f"this is {user.name}'s blog post")

@logging_decorator
def login(user):
    user.is_logged_in = True

new_user = User("Tejas")
login(new_user)
create_blog(new_user)
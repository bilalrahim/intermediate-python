is_logged_in=True

def login_required(f):

    def wrapper():
        if not is_logged_in:
            return "False"
        else:
            return f()
    return wrapper

@login_required
def generate_view():
    return "Hello"

print(generate_view())

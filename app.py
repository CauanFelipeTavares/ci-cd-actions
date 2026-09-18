def greet(name):
    return f"Hello, {name or 'world'}!"


def farewell(name):
    return f"Bye, {name or 'world'}!"


if __name__ == "__main__":
    assert greet("cauan") == "Hello, cauan!"
    assert greet("") == "Hello, world!"
    assert farewell("cauan") == "Bye, cauan!"
    assert farewell("") == "Bye, world!"
    print(greet("cauan"), farewell("cauan"))

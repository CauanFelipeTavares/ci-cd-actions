def greet(name):
    return f"Hello, {name or 'world'}!"


if __name__ == "__main__":
    assert greet("cauan") == "Hello, cauan!"
    assert greet("") == "Hello, world!"
    print(greet("cauan"))

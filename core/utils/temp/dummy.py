from functools import wraps


def app(function) -> any:
    @wraps(function)
    def talk(*args, **kwargs) -> any:
        print('hi')
        return function(*args, **kwargs)
    return talk


@app
def main() -> any:
    return 1 + 1


if __name__ == "__main__":
    print(app)

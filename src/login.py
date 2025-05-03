import os


def token_for_my_silly_web(username: str, password: str) -> str:
    """Fake token generation for silly web."""
    return hash(f"{username}{password}")



def get_something_from_the_silly_web(token: str) -> str:
    header = {"Authorization": "token"}

    # make the request to the silly web
    # response = requests.get("https://sillyweb.com/api", headers=header)
    # do something with the response

    return "ok"


if __name__ == "__main__":
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(f"Getting important data from the silly web for {username=}")
    token = token_for_my_silly_web(username, password)
    result = get_something_from_the_silly_web(token)
    print(result)

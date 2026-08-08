import requests


def get_weather(location: str) -> str:
    # your API code here
    return f"Weather for {location}"


def main():
    print("Hello from mcp-aws!")
    print(get_weather("Delhi"))


if __name__ == "__main__":
    main()
    
    print("Hello from mcp-aws!")
    print(get_weather("Delhi"))
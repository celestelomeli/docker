import requests

def main():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    if response.status_code == 200:
        print("Request successful!")
        print("Response content:")
        print(response.text)
    else:
        print("Request failed with status code:", response.status_code)

if __name__ == "__main__":
    main()
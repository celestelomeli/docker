# Import the 'requests' library that allows making HTTP requests from Python code
import requests

# Define a function named 'main' that serves as the entry point of the program 
def main():
    # Use the 'requests.get' function to send an HTTP GET request to <url>
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    # Check if the HTTP response status code is 200 (OK)
    if response.status_code == 200:
        # Print a success message if the status code is 200
        print("Request successful!")
        # Print the content of the HTTP response (HTML content of the page)
        print("Response content:")
        #
        print(response.text)
    else:
        # Print an error message along with actual status code
        print("Request failed with status code:", response.status_code)
# Check if the script is being run as the main program             
if __name__== "__main__":
    # Call the main function to start the program
    main()
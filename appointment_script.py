import requests
from bs4 import BeautifulSoup
import time

def get_dropdown_options(url, target_element_id):
  # Make a request to the website
    response = requests.get(url)
    response.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the target dropdown element
    target_element = soup.find('select', {'name': target_element_id})

    # Return the text content of options if the dropdown is found, otherwise return an empty list
    return [option.text.strip() for option in target_element.find_all('option')] if target_element else []


def check_website(url, target_element_id):
    previous_options = ['More Info','Audit & Assurance','Financial Advisory','Analytics and M&A','Middle Marketing','Legal Consulting','Regulatory Risk','Other']

    while True:
        try:
            # Get the current options in the dropdown
            current_options = get_dropdown_options(url, target_element_id)
            print(previous_options)
            print(current_options)
            # Check if the options have changed
            if current_options != previous_options:
                print("Dropdown options have changed! You can book your appointment now.")
                break

            # Update the previous options for the next iteration
            previous_options = current_options

            # Wait for a certain period before checking again
            # Adjust the counter, howmuch time you want to wait before new request
            time.sleep(5)  

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            time.sleep(60)  # Wait for a while before trying again in case of an error

if __name__ == "__main__":
    # Specify the URL of the website 
    website_url = "https://www.logxgroup.me/"
    # Specify the field you want to detect the change from
    dropdown_id = "info"

    check_website(website_url, dropdown_id)

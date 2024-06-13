import argparse
import subprocess
import os
import pyfiglet
from colorama import init, Fore, Style

def print_title():
    """Print the script title and description."""
    title = pyfiglet.figlet_format("Wayback Sensitive Info Detector")
    description = """
    Wayback Sensitive Info Detector - A sophisticated tool for identifying sensitive information in archived URLs.
    This tool can check a single domain or a list of domains for indications of sensitive information.
    """
    print(title)
    print(description)

def read_domains(file_path):
    """Read domains from a file and return them as a list."""
    with open(file_path, 'r') as file:
        domains = [line.strip() for line in file.readlines()]
    return domains

def log_check(action, result=None):
    """Log the actions taken and the results."""
    if result is not None:
        color = Fore.GREEN if result == "Detected" else Fore.RED
        symbol = "+" if result == "Detected" else "-"
        print(f"{color}{symbol} {action}: {result}{Style.RESET_ALL}")
    else:
        print(f"Checking {action}...")

def save_result(domain, results):
    """Save the detected sensitive URLs to a file in a folder named after the domain."""
    folder_name = domain.replace(".", "_")
    os.makedirs(folder_name, exist_ok=True)
    output_file = os.path.join(folder_name, f"{folder_name}.txt")
    
    with open(output_file, 'w') as file:
        if results:
            file.write("Potential sensitive information found in the following URLs:\n")
            for url in results:
                file.write(url + '\n')
        else:
            file.write("No sensitive information found in the URLs.\n")
    
    print(f"Results saved in {output_file}")

def check_sensitive_info(url):
    """Check if the URL contains sensitive information."""
    sensitive_keywords = [
        'password', 'credential', 'admin', 'login', 'secret', 'key', 'config', 'confidential',
        'private', 'token', 'auth', 'session', 'account', 'database', 'root', 'backup',
        'user', 'username', 'access', 'secure','payment',
        'credit', 'card', 'billing', 'invoice', 'purchase', 'order', 'customer', 'client',
        'api', 'apikey', 'hidden', 'internal', 'sensitive', 'temp', 'tmp', 'test',
        'development', 'dev', 'stage', 'staging', 'uat', 'prod', 'production', 'debug', 'trace',
        'error', 'bug', 'logs', 'log', 'dump', 'import', 'export', 'upload', 'download'
    ]
    return any(keyword in url.lower() for keyword in sensitive_keywords)

def fetch_urls(domain):
    """Run getallurls tool and fetch URLs."""
    try:
        result = subprocess.run(['gau', domain ,'--fp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Error running getallurls: {result.stderr}")
            return []
        urls = result.stdout.splitlines()
        return urls
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return []

def process_domains(domains):
    """Process a list of domains to check for sensitive information."""
    for domain in domains:
        print(f"\nChecking {domain}...")
        urls = fetch_urls(domain)
        if not urls:
            print(f"{Fore.RED}- No URLs found for {domain}.{Style.RESET_ALL}")
            continue

        sensitive_urls = [url for url in urls if check_sensitive_info(url)]
        if sensitive_urls:
            print(f"{Fore.GREEN}+ Sensitive information found in URLs for {domain}.{Style.RESET_ALL}")
            save_result(domain, sensitive_urls)
        else:
            print(f"{Fore.RED}- No sensitive information found in URLs for {domain}.{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description="Check archived URLs for sensitive information.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--url', type=str, help="Check a single domain.")
    group.add_argument('-f', '--file', type=str, help="Path to the file containing the list of domains.")
    args = parser.parse_args()

    init(autoreset=True)
    print_title()

    if args.url:
        domains = [args.url]
    elif args.file:
        domains = read_domains(args.file)

    process_domains(domains)

if __name__ == "__main__":
    main()


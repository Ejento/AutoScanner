import argparse
import re, time
from web_scanner import WebScanner
from port_scanner import NetScanner
from ascii_art import display_art

# Static Variables
IPV4_PATTERN = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
DOMAIN_PATTERN = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}(?:\.[a-zA-Z]{2,})?'

def check_host_file(target_ip):
    try:
        with open('/etc/hosts',"r") as file:
            for line in file:
                if line.strip() and not line.strip().startswith("#"):
                    parts = line.split()
                    if len(parts) >= 2:
                        ip, host = parts[0],parts[1]
                        if ip == target_ip:
                            print(f"Found: {target_ip} ---> {host}!\nContinuing with domain name.")
                            domain = host
                            return domain
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

    return None

def extract_domain(input_string):
    domain_regex = re.compile(DOMAIN_PATTERN)
    match = re.search(domain_regex, input_string)
    if match:
        return match.group(0)
    
    return None

# Ascii art
display_art()
# Main logic
parser = argparse.ArgumentParser(description="Nmap Port Scanner")
parser.add_argument("target", help="Target IP address or hostname")
#parser.add_argument("-p", "--ports", default="1-1000", help="Port range to scan (default: 1-1000)")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

args = parser.parse_args()
ipv4_regex = re.compile(IPV4_PATTERN)

nmap_scanner = NetScanner(args.target)

[step1_ports,step1_tech] = nmap_scanner.scan_all_ports(args.target, args.verbose)
print("Still running, just wait a little more...")
services = nmap_scanner.scan_port_services(args.target, step1_ports, args.verbose)
print("Cool! Keep processing things...")
print("="*100+"\n")

gobuster_scanner = WebScanner(args.target)
http_ports = []
for ip, ports in services.items():
    for port, info in ports.items():
        if info['name'] == 'http' and 'scripts' in info:
            if 'http-title' in info['scripts']:
                http_ports.append(port)
                if ipv4_regex.match(args.target):
                    extracted_domain = extract_domain(" ".join({info['scripts']['http-title']}))
                    break
        elif info['name'] == 'ldap':
            extracted_domain = extract_domain(info['extraInfo'])
            break
        elif 'scripts' in info:
            info['scripts'].get('fingerprint-strings', '')

# Just a RegEx for the domain
domain_regex = re.compile(DOMAIN_PATTERN)
# If the user's argument was a domain instead of an IP address, then the domain is matched with the argument.
domain = domain_regex.match(args.target)
# If the user provided an IP, then we are checking the local host file (/etc/hosts) to see if there is a match.
while not domain:
    domain = check_host_file(args.target)
    # If there is a domain for that IP address, then we proceed with that.
    # In all the other cases, we prompt the user to add the extracted domain name to the hosts file.
    if domain:
        gobuster_scanner.change_target(domain)
    else:
        answer = input(f"You should go and add the {extracted_domain}, for the IP address {args.target}, in your /etc/hosts file.\nPress Y or N. ").lower()
        time.sleep(1)
        if answer == 'n':
            break

http_directories = gobuster_scanner.scanner(http_ports,"directories")
http_directories = gobuster_scanner.cleaner_gobuster(http_directories)
for port, results in http_directories.items():
    print(f"Results for port {port}:")
    for result in results:
        print(result)
print("-"*100)
http_files = gobuster_scanner.scanner(http_ports,"files")
http_files = gobuster_scanner.cleaner_gobuster(http_files)
for port, results in http_files.items():
    print(f"Resuls for files for {port}:")
    for result in results:
        if "Status: 403" not in result:
            print(result)
        else:
            with open("more_files.txt","a") as status403:
                status403.write(result)
print("-"*100)

print(f"Scanning for subdomains of the {domain} domain.")
subdomains_list = gobuster_scanner.vhost_scanner(domain)
subdomains_list = gobuster_scanner.clean_gobuster_vhosts(subdomains_list)

subs_200 = []
for result in subdomains_list:
    with open("subs.txt","w") as subs:
        subs.write(result)
    if "Status: 400" not in result:
        subs_200.append(result)
        
for i in subs_200:
    print(i)

print("Exiting...Bye bye!")
exit(0)
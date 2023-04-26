import subprocess
import csv

# Read in subnets from file
with open('file.txt', 'r') as f:
    subnets = f.read().splitlines()

# Initialize an empty list to hold active hosts
active_hosts = []

# Loop through each subnet and scan for open port 80
for subnet in subnets:
    # Use nmap to scan for open port 80
    nmap_cmd = f"nmap -p 80 {subnet}"
    nmap_output = subprocess.check_output(nmap_cmd, shell=True).decode()

    # Loop through each line of the nmap output
    for line in nmap_output.splitlines():
        # Check if the line contains an IP address
        if "Nmap scan report for" in line:
            ip = line.split()[-1].replace("(", "").replace(")", "")

            # Ping the IP to see if it is active and alive
            ping_cmd = f"ping -c 1 {ip}"
            ping_output = subprocess.call(ping_cmd, shell=True)

            if ping_output == 0:
                print(f"{ip} is active and alive.")
                active_hosts.append(ip)
            else:
                print(f"{ip} is not active.")

            # Add the IP to the active hosts list if it is open on port 80
            if "80/tcp open" in nmap_output:
                print(f"{ip} has port 80 open.")
                active_hosts.append(ip)

# Write the list of active hosts to a CSV file
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['IP Address', 'Port 80 Open'])
    for host in set(active_hosts):
        has_port_80_open = "Yes" if host in active_hosts and "80/tcp open" in nmap_output else "No"
        writer.writerow([host, has_port_80_open])


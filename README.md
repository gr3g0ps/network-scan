# network-scan
Python Network Scanner for Network administrators or System Admins.

This script reads in a list of subnets from a file called file.txt, uses nmap to scan for open port 80 on each subnet, pings each found host to see if it is active and alive, and saves the list of active hosts to an output.txt file. 

The list of active hosts is stored in the active_hosts list, which is written to the csv file at the end of the script. 

The script uses the set() function to remove duplicates from the list of active hosts, since a host may be both pingable and have port 80 open.


Repo must contains 2 files to run: file.txt & scan.py
<br>
File.txt should contain all networks subnet for scan: file.txt 

code:
touch file.txt 

e.g. 192.168.1.1/24


Python scan script. 

scan.py





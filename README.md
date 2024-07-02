# ketamine

Ketamine is a comprehensive network and penetration testing utility designed to streamline a wide range of tasks into a single suite, eliminating the need to switch between multiple tools.

Currently, Ketamine can perform numerous functions including:

Network interface configuration (ifconfig)
Connectivity tests (ping)
Network path tracing (traceroute)
Various port scans (SYN, TCP, UDP, ACK, and comprehensive scans)
Host discovery (identifying active devices on a local network)
MAC address detection (retrieving MAC addresses of host IPs on a local network)
Banner grabbing
DNS checks with geolocation information
WHOIS lookups
Subdomain enumeration
Vulnerability reconnaissance
Packet sniffing
MAC spoofing
IP spoofing
SYN flooding
Deauthentication attacks
Brute-force attacks (currently in beta)
Future enhancements planned for Ketamine include:

WAF detection
DNS enumeration
Traffic analysis
XSS vulnerability scanning
ARP cache poisoning
DNS cache poisoning
MAC flooding
Ping of death attacks
Network disassociation attacks (distinct from deauthentication attacks)
OSINT
Email spoofing
Exploits
Automation of various tasks
Ketamine aims to be an all-in-one solution for network and security professionals, offering a robust and versatile toolset for a wide range of applications.

![image](https://github.com/IlyaKosloF/ketamine/assets/174350287/3d55a34d-c44b-4faf-b0f9-2a5a1ac77d1a)

# Contents

. -- Networking --

ifconfig (beta)
ping
traceroute
Footprinting
Port scans
Host discovery (scan for devices on a local network)
MAC address detection (get MAC address of a host IP on a local network)
Application version detection (also known as banner grabbing)
DNS checks (with geolocation information)
WHOIS
Subdomain enumeration
Directory busting
Vulnerability reconnaissance
Offensive
Packet sniffing
MAC spoofing
IP spoofing
SYN flooding
Deauth attack
Brute-force attack (beta)
Others
Turn on monitor/managed mode on an interface
Automated reconnaissance (beta)

# Installation

Note that currently, this script only runs well on Linux. If you try it in on Windows or macOS, it may run, but numerous errors will appear.

This script was tested on:

Kali Linux
Ubuntu
Pop!_OS

# Linux
To install the necessary packages so that the script can run withouth any problems simply run the setup.sh script with root privileges. Currently, this installation script is only supported on Debian, Red Hat and Arch based distros that has the apt, dnf and pacman package manager respectively (Ubuntu, Kali Linux, Parrot OS, Debian, Pop!_OS, Linux Mint, Deepin, Zorin OS, MX Linux, Elementary OS, Fedora, CentOS, Red Hat Enterprise Linux, Rocky Linux, AlmaLinux, Oracle Linux, ClearOS, Arch, Black Arch, Manjaro, etc). On most systems, to install Hawk simply run the following commands:

git clone https://github.com/IlyaKosloF/ketamine.git

cd ketamine

sudo sh setup.sh

sudo python3 ketamine.py

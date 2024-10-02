# Network_Scanner_Tool
Creating a Python-based tool for scanning networks, detecting open ports, services, and vulnerabilities.
Project Overview
Objective:

To develop a Python-based network scanner that can discover devices on a local network, identify open ports, and provide basic information about the services running on these ports.
Features:

Device Discovery: Identify all devices connected to a given network.
Port Scanning: Scan open ports on discovered devices.
Service Detection: Identify services running on the open ports.
Reporting: Provide a summary report of the scanned network.

Tools and Libraries:

Python: The core programming language.
Scapy: A powerful Python library for network manipulation and packet analysis.
socket: A built-in Python module for network communications.
argparse: A module for handling command-line arguments.
threading: To handle multiple scanning tasks simultaneously.

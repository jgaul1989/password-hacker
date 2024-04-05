# Network Login Tester

This script is designed to automate the process of testing login mechanisms on network services. It attempts to log in to a server by generating and sending various username and password combinations. The script uses a timing attack to deduce the correct password based on the response delay from the server.

## Description

The Network Login Tester connects to a specified IP address and port using a socket connection. It then attempts to log in using a list of popular usernames, trying different case variations for each. The script intelligently guesses the password by observing the time taken by the server to respond, exploiting the timing vulnerability.

## How It Works
- The script reads from logins.txt and generates all possible case combinations of the usernames.
- It connects to the server using the provided IP address and port.
- It then attempts to log in with each username, incrementally constructing the password.
- The script sends the login request and measures the response time for each password attempt.
- A longer response time for a specific password attempt indicates a partially correct password, exploiting the timing vulnerability in the login process.
- The script continues this process, character by character, to deduce the correct password.
- Once the correct username and password are identified, the script prints them out.

### Disclaimer
This tool is for educational and ethical testing purposes only. 
Unauthorized testing on servers without explicit permission is illegal and unethical. 
Always ensure you have explicit authorization before testing a server or network with this script.
The idea for this project came from https://hyperskill.org/projects/80?track=2
#### Dependencies

- Python 3.x
- Access to a network service to test, which responds with specific JSON messages for login attempts

##### Setup

1. Ensure Python 3.x is installed on your system.
2. Clone this repository or download the script to your local machine.
3. Prepare a file named `logins.txt` containing usernames to try, with one username per line.

###### Usage

Run the script from the command line, providing the IP address and port number of the server you wish to test.

```bash
python network_login_tester.py <ip_address> <port_number>

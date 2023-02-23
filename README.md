
# Python Reverse Shell

This repository contains the code for a basic reverse shell in Python. A reverse shell is a type of shell in which the target machine communicates back to the attacking machine, allowing the attacker to execute commands on the target machine.

## Prerequisites
In order to use this reverse shell, you will need to have Python 3 installed on both the target and attacking machines.


## Usage

To use this reverse shell, follow these steps:

1. Clone this repository to both the target and attacking machines.
2. On the target machine, run the client.py script with the command python3 client.py.
3. On the attacking machine, run the server.py script with the command python3 server.py.
4. Once the connection is established, you can send commands from the attacking machine to be executed on the target machine. The results of the commands will be returned to the attacking machine.

    Note that while reverse shells can be a useful tool for system administration and network testing, they can also be used maliciously to gain unauthorized access to systems. As such, it's important to use them responsibly and with proper authorization.


## Contributing

Contributions to this repository are welcome. If you have any suggestions for improvements, please feel free to submit a pull request.


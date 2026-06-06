
# Python Reverse Shell

This repository contains a simple Python implementation of a reverse shell, allowing a remote client to connect to a server and execute commands on the server machine.



## Installation

To use this script, simply clone the repository using the following command:

```bash
  git clone https://github.com/sallar-ba/PythonReverseShell.git
```
    
## Usage
### Server Side
On the server side, run the server.py script to start listening for incoming connections:


```bash
python server.py

```
### Client Side
On the client side, run the client.py script with the IP address and port number of the server machine:

```bash
    python client.py <server_ip> <server_port>

```
After running the client script, you will be connected to the server and can execute commands on the server machine through the client terminal.




## Disclaimer
This script is intended for educational purposes only and should not be used for any malicious activities. The author of this script is not responsible for any damage caused by the misuse of this script.


## License
This project is licensed under the MIT License - see the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.


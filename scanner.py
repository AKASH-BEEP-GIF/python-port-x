import socket

GREEN = "\033[92m"
RESET = "\033[0m"

print(GREEN + r"""
██████╗  ██████╗ ██████╗ ████████╗██╗  ██╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝╚██╗██╔╝
██████╔╝██║   ██║██████╔╝   ██║    ╚███╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║    ██╔██╗
██║     ╚██████╔╝██║  ██║   ██║   ██╔╝ ██╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
""" + RESET)


target = input("Enter target IP: ")


port_input = input("Enter ports (example: 22,80,443,8080): ")


ports = [int(port.strip()) for port in port_input.split(",")]

print("\nScanning:", target)
print("-" * 30)


for port in ports:

    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    sock.settimeout(1)

    
    result = sock.connect_ex((target, port))

    
    if result == 0:
        print(f"Port {port} -> OPEN")
    else:
        print(f"Port {port} -> CLOSED")

    
    sock.close()

print("-" * 30)
print("Scan completed.")
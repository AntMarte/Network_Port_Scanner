import socket

def scan_port(target_host, target_port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout value (adjust as needed)
        sock.settimeout(2)
        
        # Attempt to connect to the target host and port
        result = sock.connect_ex((target_host, target_port))
        
        # Check the connection result
        if result == 0:
            print(f"Port {target_port}: Open")
        else:
            print(f"Port {target_port}: Closed")
        
        # Close the socket
        sock.close()
    
    except socket.error as e:
        print(f"Error: {e}")

def main():
    # Example usage: scan a single target host and a range of ports
    target_host = input("Enter the target host: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    
    # Scan the range of ports
    for port in range(start_port, end_port + 1):
        scan_port(target_host, port)

if __name__ == "__main__":
    main()

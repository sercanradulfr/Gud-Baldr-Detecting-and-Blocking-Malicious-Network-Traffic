import socket
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Gud Baldr")
print(ascii_banner)

def analyze_network_traffic():
    # Prompt the user to enter the IP address and port to monitor
    ip_address = input("Enter the IP address to monitor (e.g., 127.0.0.1): ")
    port = input("Enter the port to monitor (e.g., 8080): ")
    
    try:
        port = int(port)
    except ValueError:
        print("Invalid port number. Please enter a valid port number.")
        return
    
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Bind the socket to the IP address and port
        s.bind((ip_address, port))
        
        # Listen for incoming connections
        s.listen(1)
        print(f"Listening for incoming connections on {ip_address}:{port}...")
        
        while True:
            # Accept a client connection
            conn, addr = s.accept()
            print(f"Connection established from: {addr[0]}:{addr[1]}")
            
            # Receive data from the client
            data = conn.recv(1024)
            
            # Perform analysis on the received data
            if detect_malicious_traffic(data):
                print("Malicious traffic detected!")
                # Perform actions like blocking the IP or sending an alert
            
            # Close the connection
            conn.close()
    except socket.error as e:
        print(f"Error: {e}")
    finally:
        # Close the socket
        s.close()


def detect_malicious_traffic(data):
    # Implement your own logic to analyze the data
    # You can use various techniques like pattern matching, machine learning, etc.
    # For the sake of this example, let's assume any data starting with "XSS" is considered malicious
    if data.startswith(b"XSS"):
        return True
    else:
        return False


# Run the network traffic analysis tool
if __name__ == "__main__":
    analyze_network_traffic()

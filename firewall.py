print("Enter the Port number to scan: ")
port = int(input())
ports = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    21: "FTP"
}
if port in ports:
    print(f"Port is open: {ports[port]}")
else:
    print("port is closed")

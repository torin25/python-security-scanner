import socket
import datetime

# Ask user for target
user_input = input("Enter target host/IP (press Enter for default: scanme.nmap.org): ").strip()
TARGET = user_input if user_input else "scanme.nmap.org"

# Ports to scan
PORTS = [22, 80, 443, 8080]

def scan_port(port):
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((TARGET, port))
        try:
            banner = s.recv(1024).decode().strip()
        except:
            banner = "No banner"
        return True, banner
    except:
        return False, None
    finally:
        s.close()

def main():
    results = []
    print(f"\n[*] Scanning {TARGET}...\n")

    for port in PORTS:
        is_open, banner = scan_port(port)
        if is_open:
            result = f"[OPEN] Port {port} | Banner: {banner}"
            print(result)
            results.append(result)
        else:
            print(f"[CLOSED] Port {port}")

    # Save results
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"scan_report_{timestamp}.txt"

    with open(report_name, "w") as f:
        for line in results:
            f.write(line + "\n")

    print(f"\nReport saved as: {report_name}")

if __name__ == "__main__":
    main()

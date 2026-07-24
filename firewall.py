BLOCKED_IPS = {"192.168.1.66", "10.0.0.13", "203.0.113.99"}
BLOCKED_PORTS = {23, 445, 3389}         
ALLOWED_PROTOCOLS = {"TCP", "UDP"}


def check_packet(packet: dict)
    src_ip = packet.get("src_ip")
    dst_port = packet.get("dst_port")
    protocol = packet.get("protocol")

    if src_ip in BLOCKED_IPS:
        return False, f"Source IP {src_ip} is blacklisted"

    if dst_port in BLOCKED_PORTS:
        return False, f"Destination port {dst_port} is blocked"

    if protocol not in ALLOWED_PROTOCOLS:
        return False, f"Protocol {protocol} not permitted"

    return True, "Packet allowed"


def generate_fake_packet() -> dict:
    sample_ips = [
        "192.168.1.66", "192.168.1.10", "10.0.0.13",
        "10.0.0.5", "203.0.113.99", "8.8.8.8"
    ]
    sample_ports = [22, 23, 80, 443, 445, 3389, 8080]
    sample_protocols = ["TCP", "UDP", "ICMP"]

    return {
        "src_ip": random.choice(sample_ips),
        "dst_port": random.choice(sample_ports),
        "protocol": random.choice(sample_protocols),
    }


def run_simulation(num_packets: int = 10, delay: float = 0.5) -> None:
    print("=== Firewall Simulation Started ===\n")

    for i in range(1, num_packets + 1):
        packet = generate_fake_packet()
        allowed, reason = check_packet(packet)
        status = "ALLOWED " if allowed else "BLOCKED "

        print(f"[{i:02d}] {packet['src_ip']:>15} -> port {packet['dst_port']:<5} "
              f"({packet['protocol']:<4}) : {status}  | {reason}")

        time.sleep(delay)

    print("\n=== Simulation Complete ===")


if __name__ == "__main__":
    run_simulation(num_packets=15, delay=0.3)

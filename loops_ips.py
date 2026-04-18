# Week 4: Loops and Iteration
# Goal: Identify internal vs external IP addresses

ip_addresses = [
    "192.168.1.25",
    "10.0.0.8",
    "172.16.5.14",
    "8.8.8.8",
    "172.15.3.2"
]
for ip in ip_addresses:
    print(ip)

print("\n")

for ip in ip_addresses:
    if ip.startswith("192.168.") or ip.startswith("10."):
        print(f"{ip} is an internal address.")
    else:
        print(f"{ip} is an external address.")

print("\n")

for ip in ip_addresses:
    if ip.startswith("192.168."):
        zone = "Private (Class C)"
    elif ip.startswith("10."):
        zone = "Private (Class A)"
    elif ip.startswith("172.16.") or ip.startswith("172.17.") or ip.startswith("172.31."):
        zone = "Private (Class B)"
    else:
        zone = "Public"

    print(f"{ip} → {zone}")

print("\n")

index = 0
while index < len(ip_addresses):
    ip = ip_addresses[index]

    if ip.startswith(("192.168.", "10.")):
        print(f"{ip} is internal.")
    else:
        print(f"{ip} is external.")

    index += 1

internal_count = 0
external_count = 0
for ip in ip_addresses:
    if ip.startswith(("192.168.", "10.")):
        internal_count += 1
    else:
        external_count += 1

print(f"\nInternal IP addresses: {internal_count}")
print(f"External IP addresses: {external_count}")

print("\n")

internal_ips =[]
external_ips = []
for ip in ip_addresses:
    if ip.startswith(("192.168.", "10.")):
        internal_ips.append(ip)
    else:
        external_ips.append(ip)

print(f"\nInternal IP addresses: {internal_ips}")
print(f"External IP addresses: {external_ips}")

print("\n")

while True:
    ip = input("Enter an IP address (or 'done' to quit): ")
    if ip.lower() == "done":
        break
    elif ip.startswith(("192.168.", "10.")):
        print(f"{ip} is internal.")
    else:
        print(f"{ip} is external.")
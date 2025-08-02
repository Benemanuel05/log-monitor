from collections import defaultdict

# File to read
log_file = "sample_log.txt"

# Dictionary to count failed logins per IP
failed_logins = defaultdict(int)

# Threshold for alerts
THRESHOLD = 3

with open(log_file, "r") as file:
    for line in file:
        if "ERROR Failed login" in line:
            ip_start = line.find("ip: ") + 4
            ip = line[ip_start:].strip()
            failed_logins[ip] += 1

# Print results
for ip, count in failed_logins.items():
    if count >= THRESHOLD:
        print(f"[ALERT] {count} failed logins from IP: {ip}")
    else:
        print(f"[INFO] {count} failed logins from IP: {ip}")

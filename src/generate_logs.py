import csv
import random
from datetime import datetime, timedelta

# Number of log records to generate
NUM_RECORDS = 1000

# Output file
OUTPUT_FILE = "data/raw/infrastructure_logs.csv"

# Sample infrastructure values
hosts = [
    "WEB-SERVER-01",
    "WEB-SERVER-02",
    "APP-SERVER-01",
    "APP-SERVER-02",
    "DB-SERVER-01",
    "DB-SERVER-02",
    "ROUTER-01",
    "SWITCH-01"
]

device_types = {
    "WEB-SERVER-01": "Windows Server",
    "WEB-SERVER-02": "Windows Server",
    "APP-SERVER-01": "Linux Server",
    "APP-SERVER-02": "Linux Server",
    "DB-SERVER-01": "Database Server",
    "DB-SERVER-02": "Database Server",
    "ROUTER-01": "Network Device",
    "SWITCH-01": "Network Device"
}

event_types = [
    "Authentication",
    "CPU Monitoring",
    "Memory Monitoring",
    "Network",
    "Application",
    "System"
]

severity_levels = [
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL"
]

messages = {
    "Authentication": [
        "Successful user login",
        "Failed login attempt",
        "User account locked",
        "Password authentication failed"
    ],
    "CPU Monitoring": [
        "CPU utilization normal",
        "High CPU utilization detected",
        "CPU utilization exceeded threshold"
    ],
    "Memory Monitoring": [
        "Memory utilization normal",
        "High memory utilization detected",
        "Memory utilization exceeded threshold"
    ],
    "Network": [
        "Network connection established",
        "Packet loss detected",
        "Network interface is down",
        "Network connectivity restored"
    ],
    "Application": [
        "Application started successfully",
        "Application error occurred",
        "Database connection timeout",
        "Service response time exceeded threshold"
    ],
    "System": [
        "System startup completed",
        "System service restarted",
        "Disk space running low",
        "System configuration changed"
    ]
}

# Starting timestamp
start_time = datetime(2026, 1, 1, 0, 0, 0)

# Create the CSV file
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

    fieldnames = [
        "event_id",
        "event_timestamp",
        "host_name",
        "device_type",
        "event_type",
        "severity",
        "source_ip",
        "message"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for event_id in range(1, NUM_RECORDS + 1):

        host = random.choice(hosts)
        event_type = random.choice(event_types)
        severity = random.choices(
            severity_levels,
            weights=[60, 25, 12, 3]
        )[0]

        timestamp = start_time + timedelta(
    minutes=random.randint(0, 349919)
)

        source_ip = (
            f"192.168."
            f"{random.randint(1, 10)}."
            f"{random.randint(1, 254)}"
        )

        message = random.choice(messages[event_type])

        writer.writerow({
            "event_id": event_id,
            "event_timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "host_name": host,
            "device_type": device_types[host],
            "event_type": event_type,
            "severity": severity,
            "source_ip": source_ip,
            "message": message
        })

print(f"Successfully generated {NUM_RECORDS} infrastructure log records.")
print(f"Output file: {OUTPUT_FILE}")

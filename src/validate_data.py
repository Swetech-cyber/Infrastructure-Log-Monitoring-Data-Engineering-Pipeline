import pandas as pd

FILE_PATH = "data/raw/infrastructure_logs.csv"

df = pd.read_csv(FILE_PATH)

validation_passed = True

print(f"Loaded {len(df)} records for validation.")

# Check for missing values
missing_values = df.isnull().sum()

if missing_values.sum() == 0:
    print("PASS: No missing values found.")
else:
    print("FAIL: Missing values found:")
    print(missing_values[missing_values > 0])
    validation_passed = False


# Check for duplicate event IDs
duplicate_ids = df["event_id"].duplicated().sum()

if duplicate_ids == 0:
    print("PASS: No duplicate event IDs found.")
else:
    print(f"FAIL: Found {duplicate_ids} duplicate event IDs.")
    validation_passed = False


# Check for valid severity values
expected_severities = {"INFO", "WARNING", "ERROR", "CRITICAL"}

actual_severities = set(df["severity"].dropna().unique())

invalid_severities = actual_severities - expected_severities

if not invalid_severities:
    print("PASS: Severity values are valid.")
else:
    print(f"FAIL: Invalid severity values found: {invalid_severities}")
    validation_passed = False


# Check for valid device types
expected_device_types = {
    "Windows Server",
    "Linux Server",
    "Database Server",
    "Network Device"
}

actual_device_types = set(df["device_type"].dropna().unique())

invalid_device_types = actual_device_types - expected_device_types

if not invalid_device_types:
    print("PASS: Device types are valid.")
else:
    print(f"FAIL: Invalid device types found: {invalid_device_types}")
    validation_passed = False


# Check for valid event types
expected_event_types = {
    "Authentication",
    "CPU Monitoring",
    "Memory Monitoring",
    "Network",
    "Application",
    "System"
}

actual_event_types = set(df["event_type"].dropna().unique())

invalid_event_types = actual_event_types - expected_event_types

if not invalid_event_types:
    print("PASS: Event types are valid.")
else:
    print(f"FAIL: Invalid event types found: {invalid_event_types}")
    validation_passed = False


# Overall validation result
if validation_passed:
    print("Validation PASSED.")
else:
    print("Validation FAILED.")
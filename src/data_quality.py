import pandas as pd

FILE_PATH = "data/processed/infrastructure_logs_processed.csv"

df = pd.read_csv(FILE_PATH)

print("===== DATA QUALITY MONITORING =====")
print(f"Total records: {len(df)}")

# 1. Missing values
missing_values = df.isnull().sum().sum()

print(f"Missing values: {missing_values}")

# 2. Duplicate event IDs
duplicate_ids = df["event_id"].duplicated().sum()

print(f"Duplicate event IDs: {duplicate_ids}")

# 3. High-severity events
high_severity_count = df["is_high_severity"].sum()

print(f"High-severity events: {high_severity_count}")

# 4. Severity distribution
print("\nSeverity Distribution:")
print(df["severity"].value_counts())

# 5. Data quality status
if missing_values == 0 and duplicate_ids == 0:
    print("\nData Quality Status: PASSED")
else:
    print("\nData Quality Status: FAILED")
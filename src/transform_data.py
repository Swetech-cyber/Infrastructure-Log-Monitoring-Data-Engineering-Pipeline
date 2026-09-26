import pandas as pd

FILE_PATH = "data/raw/infrastructure_logs.csv"

df = pd.read_csv(FILE_PATH)

print(f"Loaded {len(df)} records for transformation.")
# Create event_date from event_timestamp
df["event_timestamp"] = pd.to_datetime(df["event_timestamp"])
df["event_date"] = df["event_timestamp"].dt.date

print("Transformation 1 completed: event_date created.")
# Create event_hour from event_timestamp
df["event_hour"] = df["event_timestamp"].dt.hour

print("Transformation 2 completed: event_hour created.")
# Create high-severity indicator
df["is_high_severity"] = df["severity"].isin(["ERROR", "CRITICAL"])

print("Transformation 3 completed: is_high_severity created.")
# Display transformed data
print(df[[
    "event_timestamp",
    "event_date",
    "event_hour",
    "severity",
    "is_high_severity"
]].head())
# Save transformed data
OUTPUT_PATH = "data/processed/infrastructure_logs_processed.csv"

df.to_csv(OUTPUT_PATH, index=False)

print(f"Transformed data saved to: {OUTPUT_PATH}")
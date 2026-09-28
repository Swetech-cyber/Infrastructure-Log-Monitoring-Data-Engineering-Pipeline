-- Database indexes for infrastructure log analytics

CREATE INDEX idx_logs_processed_event_timestamp
ON infrastructure_logs_processed (event_timestamp);

CREATE INDEX idx_logs_processed_high_severity
ON infrastructure_logs_processed (is_high_severity);

CREATE INDEX idx_logs_processed_host_name
ON infrastructure_logs_processed (host_name);

CREATE INDEX idx_logs_processed_event_type
ON infrastructure_logs_processed (event_type);
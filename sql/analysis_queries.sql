-- Query 1: High-Severity Events by Host

SELECT
    host_name,
    COUNT(*) AS high_severity_events
FROM infrastructure_logs_processed
WHERE is_high_severity = TRUE
GROUP BY host_name
ORDER BY high_severity_events DESC;
-- Query 2: High-Severity Events by Event Type

SELECT
    event_type,
    COUNT(*) AS high_severity_events
FROM infrastructure_logs_processed
WHERE is_high_severity = TRUE
GROUP BY event_type
ORDER BY high_severity_events DESC;
-- Query 3: Monthly High-Severity Event Trend

SELECT
    DATE_TRUNC('month', event_timestamp) AS month,
    COUNT(*) AS high_severity_events
FROM infrastructure_logs_processed
WHERE is_high_severity = TRUE
GROUP BY DATE_TRUNC('month', event_timestamp)
ORDER BY month;
-- Query 4: Overall Severity Distribution

SELECT
    severity,
    COUNT(*) AS event_count
FROM infrastructure_logs_processed
GROUP BY severity
ORDER BY event_count DESC;
-- Query 5: Top Hosts by Total Events

SELECT
    host_name,
    COUNT(*) AS total_events
FROM infrastructure_logs_processed
GROUP BY host_name
ORDER BY total_events DESC;
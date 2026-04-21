-- stream-analytics-query.sql
-- Real-time aggregation of IoT telemetry for Jacob Davis's predictive maintenance solution
SELECT
    deviceId,
    System.Timestamp AS windowEnd,
    AVG(vibration) AS avg_vibration,
    MAX(temperature) AS max_temperature,
    AVG(current_draw) AS avg_current_draw,
    COUNT(*) AS reading_count,
    MAX(CASE WHEN error_log != 'none' THEN 1 ELSE 0 END) AS error_flag
INTO [outputDataLake]
FROM [inputIotHub]
GROUP BY deviceId, TumblingWindow(second, 300)

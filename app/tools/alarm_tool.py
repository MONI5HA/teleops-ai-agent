import logging

logging.basicConfig(level=logging.INFO)

mock_alarm_data = {
    "NR-4402": [
        {
            "alarm": "High Interference",
            "severity": "critical"
        },
        {
            "alarm": "Sector Congestion",
            "severity": "major"
        }
    ],

    "NR-7781": []
}

def get_alarms(cell_id):
    logging.info(f"[Alarm Agent] Checking alarms for {cell_id}")
    return mock_alarm_data.get(cell_id, [])
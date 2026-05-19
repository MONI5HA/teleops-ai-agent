import logging

logging.basicConfig(level=logging.INFO)

mock_kpi_data = {
    "NR-4402": {
        "sinr": 4.2,
        "rsrp": -112,
        "throughput": 11,
        "connected_users": 230
    },

    "NR-7781": {
        "sinr": 18,
        "rsrp": -85,
        "throughput": 95,
        "connected_users": 80
    }
}

def get_kpi(cell_id):
    logging.info(f"[KPI Agent] Fetching data for {cell_id}")
    return mock_kpi_data.get(cell_id,"cell not found")

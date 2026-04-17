
import json
from modules.db_handler import fetch_data, delete_data
from modules.mqtt_client import publish
from config.config import BATCH_SIZE

def sync_cached_data():
    rows = fetch_data(BATCH_SIZE)
    if not rows:
        return
    success_ids = []
    for row in rows:
        row_id, data = row
        if publish(json.loads(data)):
            success_ids.append(row_id)
        else:
            break
    if success_ids:
        delete_data(success_ids)


import time, json
from modules.sensor import get_data
from modules.network import is_online
from modules.mqtt_client import connect, publish
from modules.db_handler import init_db, insert_data
from modules.sync_manager import sync_cached_data
from config.config import CHECK_INTERVAL

def main():
    init_db()
    connect()
    while True:
        data = get_data()
        if is_online():
            if not publish(data):
                insert_data(json.dumps(data))
        else:
            insert_data(json.dumps(data))
        sync_cached_data()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()

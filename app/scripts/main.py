import time, json

from modules.sensor import get_data
from modules.network import is_online
from modules.mqtt_client import connect, publish
from modules.db_handler import init_db, insert_data
from modules.sync_manager import sync_cached_data
from config.config import CHECK_INTERVAL

def main():
    print("🚀 Edge Gateway Started...", flush=True)

    init_db()
    print("✅ Database Initialized", flush=True)

    connect()
    print("✅ MQTT Connected", flush=True)

    while True:
        data = get_data()
        print("📊 Generated Data:", data, flush=True)

        if is_online():
            print("🌐 Internet Available", flush=True)

            if publish(data):
                print("📡 Published to MQTT", flush=True)
            else:
                print("⚠️ Publish failed → caching", flush=True)
                insert_data(json.dumps(data))
        else:
            print("❌ No Internet → caching", flush=True)
            insert_data(json.dumps(data))

        sync_cached_data()
        print("🔁 Sync check done", flush=True)

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()

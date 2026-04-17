
import time, random

def get_data():
    return {
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 80), 2),
        "timestamp": int(time.time())
    }

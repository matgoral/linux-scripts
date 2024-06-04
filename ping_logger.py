import subprocess
import time
from datetime import datetime

# Function to ping an IP address and return the response time in milliseconds
def ping(host):
    try:
        output = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True)
        if output.returncode == 0:
            response_time = float(output.stdout.split("time=")[-1].split(" ms")[0])
            return response_time
        else:
            return None
    except Exception as e:
        print(f"An error occurred while pinging {host}: {e}")
        return None

# Function to log the timestamp and host if the response time is greater than the threshold
def log_if_slow(host, response_time, log_file, threshold=30):
    if response_time > threshold:
        with open("log_file", "a") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{timestamp} - {host} - {response_time}ms\n")
        print(f"{timestamp} - ping {host} - {response_time}ms")

def main():
    hosts = ["8.8.8.8", "1.1.1.1"]
    threshold = 30
    start_time = datetime.now()
    log_filename = start_time.strftime("ping_log_%Y-%m-%d.txt")

    while True:
        for host in hosts:
            response_time = ping(host)
            if response_time is not None:
                log_if_slow(host, response_time, log_filename, threshold)
        time.sleep(1)

if __name__ == "__main__":
    main()


import psutil
import time

def cpu_monitor(threshold=80):
    print("Monitoring CPU use...")

    try:
        while True:
            cpu_use = psutil.cpu_percent(interval=1)

            if cpu_use > threshold:
                print(f"CPU use exceeds the threshold: {cpu_use}%")
            else:
                print(f"CPU use is normal: {cpu_use}%")

            time.sleep(60)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    cpu_monitor(threshold=80)

"""
Day 07 - Reading tags from an Allen-Bradley PLC using pycomm3.
Requires a real PLC reachable on the network - update PLC_IP and TAG_NAMES.
"""

from pycomm3 import LogixDriver

PLC_IP = "192.168.1.10"       # tomar PLC-r actual IP diye replace koro
TAG_NAMES = ["Tank_Level", "Pump_Status", "Flow_Rate"]


def read_tags(ip, tag_names):
    """Connect to the PLC and read a list of tags. Returns a dict of tag -> value."""
    results = {}

    try:
        with LogixDriver(ip) as plc:
            for tag in tag_names:
                reading = plc.read(tag)
                if reading.error:
                    print(f"Error reading {tag}: {reading.error}")
                else:
                    results[tag] = reading.value
    except Exception as e:
        print(f"Could not connect to PLC at {ip}: {e}")

    return results


def main():
    values = read_tags(PLC_IP, TAG_NAMES)

    if not values:
        print("No tags read - check the PLC IP address and network connection.")
        return

    print("--- PLC tag values ---")
    for tag, value in values.items():
        print(f"{tag:<15} {value}")


if __name__ == "__main__":
    main()
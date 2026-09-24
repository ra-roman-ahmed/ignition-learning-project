"""
Day 04 - OOP: Class, Object, Inheritance
A tiny "device library" for a SCADA system.
"""


class Device:
    """Base blueprint - every SCADA device has these basics."""

    def __init__(self, tag, area):
        self.tag = tag
        self.area = area
        self.status = "OFFLINE"   # shuru te shob device offline dhorlam

    def turn_on(self):
        self.status = "ONLINE"
        print(f"{self.tag}: turned ON")

    def turn_off(self):
        self.status = "OFFLINE"
        print(f"{self.tag}: turned OFF")

    def report(self):
        # eta base version - Pump/Sensor eta "override" korbe (niche dekho)
        print(f"[{self.area}] {self.tag} -> {self.status}")


class Sensor(Device):
    """A sensor: extra info = unit + last reading."""

    def __init__(self, tag, area, unit):
        super().__init__(tag, area)     # Device-er kaj Device-ke korte dilam
        self.unit = unit
        self.last_reading = 0.0

    def read(self, value):
        self.last_reading = value
        print(f"{self.tag}: reading = {value} {self.unit}")

    def report(self):
        # ei method Device-er report()-ke "override" korche - notun behavior
        print(f"[{self.area}] {self.tag} -> {self.status}, "
              f"last reading: {self.last_reading} {self.unit}")


class Pump(Device):
    """A pump: extra info = run hours + start/stop tracking."""

    def __init__(self, tag, area):
        super().__init__(tag, area)
        self.run_hours = 0.0

    def turn_on(self):
        # ei pump-er nijer turn_on, kintu Device-er turn_on-o use korche
        super().turn_on()
        print(f"{self.tag}: pump motor starting...")

    def add_run_time(self, hours):
        self.run_hours += hours

    def report(self):
        print(f"[{self.area}] {self.tag} -> {self.status}, "
              f"run hours: {self.run_hours:.1f}")


def main():
    # --- objects toiri korlam (blueprint theke real device banalam) ---
    fit101 = Sensor("WWTP_FIT_101", "WWTP", "GPM")
    pmp03 = Pump("WWTP_PMP_A03", "WWTP")

    print("--- Starting up ---")
    fit101.turn_on()
    pmp03.turn_on()          # Device-er turn_on() + Pump-er extra line, dutoi cholbe

    print("\n--- Working ---")
    fit101.read(452.7)
    pmp03.add_run_time(3.5)

    print("\n--- Status report ---")
    devices = [fit101, pmp03]   # duita alada type, kintu ekshathe list e rakha jay
    for d in devices:
        d.report()              # protita nijer report() call hobe (Sensor-er alada, Pump-er alada)


if __name__ == "__main__":
    main()
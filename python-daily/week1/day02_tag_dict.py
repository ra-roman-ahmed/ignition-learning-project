"""
Day 02 - Tag validator rewritten with a dictionary + list comprehension
Same job as Day 01, cleaner code.
"""

# Dictionary: prefix -> full meaning. Also acts as the "valid list".
TAG_TYPES = {
    "FIT": "Flow Indicating Transmitter",
    "LIT": "Level Indicating Transmitter",
    "PIT": "Pressure Indicating Transmitter",
    "TIT": "Temperature Indicating Transmitter",
    "PMP": "Pump",
    "VLV": "Valve",
}


def validate_tag(tag):
    parts = tag.split("_")

    if len(parts) != 3:
        return False, "Expected 3 parts: AREA_TYPE_NUMBER"

    area, tag_type, number = parts

    if not area.isalpha():
        return False, f"Area '{area}' should be letters only"

    if tag_type not in TAG_TYPES:
        return False, f"Unknown type '{tag_type}'"

    if not number.isdigit():
        return False, f"Number '{number}' should be digits"

    return True, TAG_TYPES[tag_type]   # ekhon message e full name o dekhabe


def main():
    tags = [
        "WWTP_FIT_101",
        "WWTP_XYZ_102",
        "WWTP_PMP_A03",
        "CLEARWELL_LIT_201",
        "BADTAG",
    ]

    # --- list comprehension: ek line e shob tag validate kore result list banalam ---
    results = [(tag, *validate_tag(tag)) for tag in tags]

    for tag, is_valid, message in results:
        status = "PASS" if is_valid else "FAIL"
        print(f"[{status}] {tag:<20} {message}")

    # --- dictionary loop diye available tag types dekhano ---
    print("\nAvailable tag types:")
    for prefix, full_name in TAG_TYPES.items():
        print(f"  {prefix} = {full_name}")

    passed = sum(1 for _, is_valid, _ in results if is_valid)
    print(f"\n{passed}/{len(tags)} tags valid")


if __name__ == "__main__":
    main()
"""
Day 03 - Command-line tag validator using argparse
Run: python day03_tag_cli.py WWTP_FIT_101
Run: python day03_tag_cli.py WWTP_FIT_101 --verbose
"""

import argparse

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

    return True, TAG_TYPES[tag_type]


def main():
    parser = argparse.ArgumentParser(description="Validate a SCADA tag name")
    parser.add_argument("tag", help="Tag name to validate, e.g. WWTP_FIT_101")
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show the full type name on success"
    )
    args = parser.parse_args()

    is_valid, message = validate_tag(args.tag)
    status = "PASS" if is_valid else "FAIL"

    if is_valid and args.verbose:
        print(f"[{status}] {args.tag} -> {message}")
    else:
        print(f"[{status}] {args.tag}")

    if not is_valid:
        print(f"  Reason: {message}")


if __name__ == "__main__":
    main()
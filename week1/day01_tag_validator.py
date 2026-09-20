"""
Day 01 - ISA-style tag name validator
Checks a list of SCADA tag names against basic naming rules.
"""

VALID_PREFIXES = ["FIT", "LIT", "PIT", "TIT", "PMP", "VLV"]


def validate_tag(tag):
    """Return (is_valid, message) for a single tag name."""
    parts = tag.split("_")

    if len(parts) != 3:
        return False, "Expected 3 parts: AREA_TYPE_NUMBER"

    area, tag_type, number = parts

    if not area.isalpha():
        return False, f"Area '{area}' should be letters only"

    if tag_type not in VALID_PREFIXES:
        return False, f"Unknown type '{tag_type}'"

    if not number.isdigit():
        return False, f"Number '{number}' should be digits"

    return True, "OK"


def main():
    tags = [
        "WWTP_FIT_101",
        "WWTP_XYZ_102",
        "WWTP_PMP_A03",
        "CLEARWELL_LIT_201",
        "BADTAG",
    ]

    passed = 0
    for tag in tags:
        is_valid, message = validate_tag(tag)
        status = "PASS" if is_valid else "FAIL"
        print(f"[{status}] {tag:<20} {message}")
        if is_valid:
            passed += 1

    print(f"\n{passed}/{len(tags)} tags valid")


if __name__ == "__main__":
    main()
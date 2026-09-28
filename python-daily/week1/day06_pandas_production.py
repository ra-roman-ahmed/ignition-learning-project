"""
Day 06 - Production data analysis with pandas
Filter, calculate, group and sort shift production data.
"""

import pandas as pd


def build_data():
    """Sample shift-wise production data for 3 lines."""
    return pd.DataFrame({
        "line": ["Line1", "Line1", "Line1",
                 "Line2", "Line2", "Line2",
                 "Line3", "Line3", "Line3"],
        "shift": ["Morning", "Evening", "Night"] * 3,
        "produced": [1200, 1150, 980, 1300, 1250, 1100, 900, 950, 870],
        "rejected": [24, 35, 49, 20, 31, 22, 45, 38, 52],
        "downtime_min": [15, 30, 55, 10, 20, 25, 60, 45, 70],
    })


def add_calculated_columns(df):
    """Add good units and quality % columns."""
    df["good"] = df["produced"] - df["rejected"]
    df["quality_pct"] = (df["good"] / df["produced"] * 100).round(1)
    return df


def summarize_by_line(df):
    """Total production and average downtime per line."""
    summary = df.groupby("line").agg(
        total_produced=("produced", "sum"),
        total_rejected=("rejected", "sum"),
        avg_downtime=("downtime_min", "mean"),
    )
    summary["quality_pct"] = (
        (summary["total_produced"] - summary["total_rejected"])
        / summary["total_produced"] * 100
    ).round(1)
    summary["avg_downtime"] = summary["avg_downtime"].round(1)
    return summary


def main():
    df = build_data()
    df = add_calculated_columns(df)

    print("--- Full data ---")
    print(df)
    print(f"\nRows: {df.shape[0]}, Columns: {df.shape[1]}")

    print("\n--- Shifts with downtime over 40 min ---")
    high_downtime = df[df["downtime_min"] > 40]
    print(high_downtime[["line", "shift", "downtime_min"]])

    print("\n--- Summary by line ---")
    print(summarize_by_line(df))

    print("\n--- Top 3 shifts by quality ---")
    best = df.sort_values("quality_pct", ascending=False).head(3)
    print(best[["line", "shift", "quality_pct"]])


if __name__ == "__main__":
    main()
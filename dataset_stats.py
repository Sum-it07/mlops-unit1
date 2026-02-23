import csv
from pathlib import Path
from statistics import mean


def load_dataset(file_path: Path) -> list[dict[str, str]]:
    with file_path.open(mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)


def to_float_list(rows: list[dict[str, str]], column: str) -> list[float]:
    values: list[float] = []
    for row in rows:
        raw_value = row.get(column, "").strip()
        if not raw_value:
            continue
        values.append(float(raw_value))
    return values


def main() -> None:
    dataset_path = Path(__file__).parent / "data" / "sample_data.csv"
    rows = load_dataset(dataset_path)

    print(f"Dataset loaded from: {dataset_path}")
    print(f"Rows: {len(rows)}")
    print(f"Columns: {len(rows[0]) if rows else 0}")

    if not rows:
        print("No data found.")
        return

    for numeric_column in ("age", "score"):
        values = to_float_list(rows, numeric_column)
        if not values:
            continue
        print(f"\n{numeric_column} statistics:")
        print(f"  min: {min(values):.2f}")
        print(f"  max: {max(values):.2f}")
        print(f"  mean: {mean(values):.2f}")

    print("\nProcessed numeric columns: age, score")


if __name__ == "__main__":
    main()

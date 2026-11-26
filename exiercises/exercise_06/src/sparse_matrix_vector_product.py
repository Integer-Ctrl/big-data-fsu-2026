import argparse
import random
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent / "data"


def generate_matrix_vector(m: int, n: int, density: float) -> None:
    """Write one file per column with tab-separated row, value, and x fields.

    Each line in j.txt represents one nonzero and repeats the same x[j].
    A column with no nonzeros produces an empty file.
    """
    if m < 0 or n < 0:
        raise ValueError("Matrix dimensions must be nonnegative.")
    if not 0 <= density <= 1:
        raise ValueError("Density must be between 0 and 1.")

    # Clean existing data
    if DATA_DIR.exists():
        for file in DATA_DIR.iterdir():
            file.unlink()

    nonzero_count = round(density * m * n)
    rows_by_column: dict[int, list[int]] = {}
    for position in random.sample(range(m * n), nonzero_count):
        column, row = divmod(position, m)
        rows = rows_by_column.setdefault(column, [])
        rows.append(row)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for column in range(n):
        vector_value = random.choice((-1, 1)) * random.randint(1, 100) / 10
        with (DATA_DIR / f"{column}.txt").open("w", encoding="utf-8") as output:
            for row in sorted(rows_by_column.get(column, ())):
                value = random.randint(1, 100) / 10
                output.write(f"{row}\t{value}\t{vector_value}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate sparse matrix and vector column files.")
    parser.add_argument("m", type=int, nargs="?", default=4, help="row count (default: 4)")
    parser.add_argument("n", type=int, nargs="?", default=3, help="column count (default: 3)")
    parser.add_argument("density", type=float, nargs="?", default=0.5, help="density (default: 0.5)")
    args = parser.parse_args()
    try:
        generate_matrix_vector(args.m, args.n, args.density)
    except ValueError as error:
        parser.error(str(error))

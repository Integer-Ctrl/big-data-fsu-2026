import shutil
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


class SparseMatrixVectorProductTest(unittest.TestCase):
    def test_run_with_custom_dimensions_and_density(self):
        source = Path(__file__).resolve().parent
        with TemporaryDirectory() as directory:
            workspace = Path(directory)
            for filename in ("run.sh", "sparse_matrix_vector_product.py", "mapper.py", "reducer.py"):
                shutil.copy2(source / filename, workspace)

            output = subprocess.check_output(["bash", workspace / "run.sh", "5", "2", "1"], text=True)
            files = sorted((workspace / "data").glob("*.txt"))
            self.assertEqual([file.name for file in files], ["0.txt", "1.txt"])
            expected = [0.0] * 5
            for file in files:
                records = [line.split("\t") for line in file.read_text(encoding="utf-8").splitlines()]
                self.assertEqual([int(row) for row, _, _ in records], list(range(5)))
                for row, value, x in records:
                    expected[int(row)] += float(value) * float(x)

        entries = [line.split("\t") for line in output.splitlines()]
        self.assertEqual([int(row) for row, _ in entries], list(range(5)))
        for (_, value), total in zip(entries, expected):
            self.assertAlmostEqual(float(value), total)


if __name__ == "__main__":
    unittest.main()

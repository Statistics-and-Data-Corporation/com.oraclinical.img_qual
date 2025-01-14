from ora_img_qual import process_image
import unittest
from pathlib import Path


class TestImageProcessing(unittest.TestCase):
    def test_process_image_pass(self):
        p = Path(__file__).parent.resolve()
        with open(p / "pass.jpg", "rb") as f:
            result = process_image(f.read())

        self.assertEqual(result[1], True)

    def test_process_image_fail(self):
        p = Path(__file__).parent.resolve()
        with open(p / "fail.jpg", "rb") as f:
            result = process_image(f.read())

        self.assertEqual(result[1], False)

if __name__ == '__main__':
    unittest.main()
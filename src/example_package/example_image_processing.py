"""
SDC Example Package;

Please note, all returns that are used by SDC
must return a tuple with the following format:
        return (bool, number, str)

    bool: True if the function executed successfully, and the output is correct/expected/valid, False otherwise
    number: The score of the ML model, 0-1 or 0-100 is fine.  This will be stored as metadata in the database.
    str: A message that will be displayed to the user, should the bool be False.
        This should be a human-readable message that explains why the function failed.

A couple points to note:
1. SDC will always pass in a bytes object to an image processing function.
2. You should never attempt to read from disk or write to disk.
2.1 With the exception of loading a model from disk, which is fine.

"""

from PIL import Image
from io import BytesIO


def main(value: bytes) -> tuple:
    try:
        img = Image.open(BytesIO(value))

        if img.mode != "RGB":
            img = img.convert("RGB")

        # Do some processing here
        # For example, let's just resize the image to 100x100
        img = img.resize((100, 100))
        # model = load_model("model.pl")
        # prediction = model.predict(img)
        prediction = 95

        if prediction < 90:
            return (
                False,
                prediction,
                "Please try again, the image wasn't of high enough quality",
            )

        return True, prediction, "The prediction is correct"
    except Exception as e:
        return False, 0, f"This message is incorrect: {str(e)}"

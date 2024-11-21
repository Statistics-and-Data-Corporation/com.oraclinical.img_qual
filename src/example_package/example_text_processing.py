"""
SDC Example Package;

Please note, all returns that are used by SDC
must return a tuple with the following format:
        return (bool, number, str)

    bool: True if the function executed successfully, and the output is correct/expected/valid, False otherwise
    number: The score of the ML model, 0-1 or 0-100 is fine.  This will be stored as metadata in the database.
    str: A message that will be displayed to the user, should the bool be False.
        This should be a human-readable message that explains why the function failed.

"""


def main(value: str) -> tuple:
    if value == "Hello, World!":
        return True, 99, "This message is correct"

    return False, 12, "This message is incorrect"

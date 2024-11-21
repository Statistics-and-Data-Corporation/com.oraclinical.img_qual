from example_package import example_text_processing


def test_hello_world():
    assert example_text_processing.main("Hello, World!") == (
        True,
        99,
        "This message is correct",
    )


def test_not_hello_world():
    assert example_text_processing.main("Something else!") == (
        False,
        12,
        "This message is incorrect",
    )

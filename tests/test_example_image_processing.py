from example_package import example_image_processing


def test_image():
    # load image and convert to bytes
    with open("tests/sample.jpg", "rb") as f:
        img = f.read()

    assert example_image_processing.main(img) == (
        True,
        95,
        "The prediction is correct",
    )


def test_bad_image():
    bad_bytes = b"bad image"
    result, score, message = example_image_processing.main(bad_bytes)

    assert result is False
    assert score == 0
    assert message.startswith("This message is incorrect")

from app.rules import get_category_for_file


def test_pdf_goes_to_docs():
    assert get_category_for_file("resume.pdf") == "Docs"


def test_jpg_goes_to_images():
    assert get_category_for_file("photo.jpg") == "Images"


def test_mp4_goes_to_videos():
    assert get_category_for_file("clip.mp4") == "Videos"


def test_unknown_extension_goes_to_others():
    assert get_category_for_file("file.xyz") == "Others"


def test_uppercase_extension_is_handled():
    assert get_category_for_file("PHOTO.JPG") == "Images"
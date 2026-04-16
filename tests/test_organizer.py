from app.organizer import organize_directory


def test_organize_directory_moves_files_into_correct_folders(tmp_path):
    pdf_file = tmp_path / "resume.pdf"
    image_file = tmp_path / "photo.jpg"
    other_file = tmp_path / "notes.xyz"

    pdf_file.write_text("pdf")
    image_file.write_text("jpg")
    other_file.write_text("other")

    organize_directory(str(tmp_path))

    assert (tmp_path / "Docs" / "resume.pdf").exists()
    assert (tmp_path / "Images" / "photo.jpg").exists()
    assert (tmp_path / "Others" / "notes.xyz").exists()
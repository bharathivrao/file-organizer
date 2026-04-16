from pathlib import Path

from app.mover import move_file_to_category


def test_move_file_to_category_creates_folder_and_moves_file(tmp_path):
    source_file = tmp_path / "resume.pdf"
    source_file.write_text("sample content")

    move_file_to_category(str(source_file), str(tmp_path), "Docs")

    moved_file = tmp_path / "Docs" / "resume.pdf"

    assert not source_file.exists()
    assert moved_file.exists()


def test_move_file_to_category_renames_duplicate_file(tmp_path):
    source_file = tmp_path / "resume.pdf"
    source_file.write_text("new file")

    docs_folder = tmp_path / "Docs"
    docs_folder.mkdir()
    existing_file = docs_folder / "resume.pdf"
    existing_file.write_text("existing file")

    move_file_to_category(str(source_file), str(tmp_path), "Docs")

    renamed_file = docs_folder / "resume_1.pdf"

    assert existing_file.exists()
    assert renamed_file.exists()
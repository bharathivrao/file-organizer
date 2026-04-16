from app.watcher import FileChangeHandler


def test_should_ignore_hidden_file():
    handler = FileChangeHandler("/tmp")
    assert handler.should_ignore_file(".DS_Store") is True


def test_should_not_ignore_normal_file():
    handler = FileChangeHandler("/tmp")
    assert handler.should_ignore_file("resume.pdf") is False
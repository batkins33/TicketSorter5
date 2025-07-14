from pathlib import Path
from processor.file_handler import get_dynamic_paths


def test_get_dynamic_paths(tmp_path):
    file_path = tmp_path / "docs" / "sample.pdf"
    file_path.parent.mkdir(parents=True)
    file_path.touch()

    out_dir, log_dir, combined_dir = get_dynamic_paths(file_path)
    assert out_dir == file_path.parent / "processed" / "sample" / "Vendor"
    assert log_dir == file_path.parent / "logs" / "sample"
    assert combined_dir == file_path.parent / "processed" / "sample" / "Combined"

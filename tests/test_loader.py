import yaml
from utils.loader import load_configs


def test_load_configs(tmp_path):
    config_file = tmp_path / "cfg.yaml"
    config_data = {
        "output_format": "pdf",
        "file_format": "camel",
    }
    config_file.write_text(yaml.dump(config_data))
    cfg = load_configs(config_file)
    assert cfg["output_format"] == "pdf"
    assert cfg["file_format"] == "camel"


def test_load_configs_invalid(tmp_path):
    config_file = tmp_path / "cfg.yaml"
    config_data = {
        "output_format": "doc",  # invalid
        "file_format": "camel",
    }
    config_file.write_text(yaml.dump(config_data))
    try:
        load_configs(config_file)
        assert False, "Expected ValueError"
    except ValueError:
        pass

from processor.filename_utils import (
    parse_input_filename,
    parse_input_filename_fuzzy,
    format_output_filename_camel,
)


def test_parse_input_filename():
    fname = "1234_2023-10-01_Gravel_Denton_Plano.pdf"
    result = parse_input_filename(fname)
    assert result["JOB_ID"] == "1234"
    assert result["DATE"] == "2023-10-01"
    assert result["MATERIAL"] == "Gravel"
    assert result["SOURCE"] == "Denton"
    assert result["DESTINATION"] == "Plano"


def test_parse_input_filename_fuzzy():
    fname = "5678_20231002_rock_source_dest.pdf"
    result = parse_input_filename_fuzzy(fname)
    assert result["JOB_ID"] == "5678"
    assert result["DATE"] == "2023-10-02"
    assert result["MATERIAL"].lower() == "rock"


def test_format_output_filename_camel():
    meta = {
        "JOB_ID": "1234",
        "DATE": "2023-10-01",
        "MATERIAL": "Gravel",
        "SOURCE": "Denton",
        "DESTINATION": "Plano",
    }
    out = format_output_filename_camel("Acme Trucking", 2, meta, "pdf")
    assert out == "1234_2023-10-01_AcmeTrucking_Gravel_Denton_Plano_2.pdf"

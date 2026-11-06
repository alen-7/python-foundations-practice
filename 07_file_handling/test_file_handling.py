from file_handling import read_scores, write_report


def test_read_scores(tmp_path):
    f = tmp_path / "scores.txt"
    f.write_text("Ada,70\nBola,50\n")
    assert read_scores(f) == {"Ada": 70, "Bola": 50}


def test_write_report_contents(tmp_path):
    out = tmp_path / "report.txt"
    write_report({"Ada": 70, "Bola": 50}, out)
    text = out.read_text()
    assert "Students: 2" in text
    assert "Average score: 60.0" in text
    assert "Top student: Ada (70)" in text

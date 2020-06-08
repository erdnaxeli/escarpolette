from escarpolette.tools import get_content_metadata


def test_get_content_metadata__ok():
    result = get_content_metadata("https://youtu.be/bpA6fAz_r04")
    expected_result = {
        "artist": "Vic Dibitetto",
        "duration": 94,
        "title": "Anybody want cawfee?! | VicDibitetto.net",
        "url": "https://www.youtube.com/watch?v=bpA6fAz_r04",
    }
    assert result == expected_result

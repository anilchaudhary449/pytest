import pytest
import requests

@pytest.mark.duckduckgo
@pytest.mark.api
def test_api_duckduckgo():
    #arrange
    url = "https://api.duckduckgo.com/?q=Python+programming&format=json"

    #act
    response = requests.get(url)
    data = response.json()

    #assert
    # accept any 2xx status code (some environments may return 202)
    assert 200 <= response.status_code < 300, f"Unexpected status code: {response.status_code}"

    # ensure AbstractText exists and contains the expected word
    abstract = (data.get('AbstractText') or "")
    assert isinstance(abstract, str)
    assert "Python" in abstract or "python" in abstract, "Expected 'Python' in AbstractText"

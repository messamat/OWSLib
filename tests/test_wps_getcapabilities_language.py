from owslib.wps import WebProcessingService
import owslib.wps


def test_wps_getcapabilities_language(monkeypatch):

    def mock_open_url(*args, **kwargs):
        assert 'language=fr-CA' in args[1]

        class FakeResponse:
            def read(self):
                return b'<xml></xml>'

        return FakeResponse()

    monkeypatch.setattr(owslib.wps, "openURL", mock_open_url)
    WebProcessingService('http://www.example.com', language='fr-CA')

from src.media import Media

class Test_Media:

    def test_media(self):
        result = Media.calc(10, 32)
        assert result == 21

import random_string_generator as rsg

class TestClass:

    def test_one(self):
        """Test the generated ID is the correct length
        """
        string = rsg.build_id(str_length=20, segments=1, separator='_', symbols=False)
        assert len(string) == 20

    def test_three(self):
        """Test the generated ID is the correct length with multiple separators
        """
        string = rsg.build_id(str_length=5, segments=6, separator='_', symbols=False)
        assert len(string) == 35

    def test_four(self):
        """Test the generated ID does not contain symbols
        """
        string = rsg.build_id(str_length=50, segments=1, separator='_', symbols=False)
        symbols = ['$', '%', '*', '@', '#', '£']
        exists = False
        for sym in symbols:
            if sym in string:
                exists = True
                break

        assert exists is False

    def test_five(self):
        """Test the generated ID does contain symbols
        """
        string = rsg.build_id(str_length=50, segments=1, separator='_', symbols=True)
        symbols = ['$', '%', '*', '@', '#', '£']
        exists = False
        for sym in symbols:
            if sym in string:
                exists = True
                break

        assert exists is True

    def test_two(self):
        """"""
        string = rsg.RandomString(separator='_', string_length=20, symbols=False)

        assert len(string) == 20+1  # string length + separator




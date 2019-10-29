
import random_string_generator as rsg

class TestClass:

    def test_one(self):
        string = rsg.build_id(str_length=20, segments=1, separator='_', symbols=False)
        assert len(string) == 20

    def test_two(self):
        string = rsg.RandomString(separator='_', string_length=20, symbols=False)

        assert len(string) == 20+1  # string length + separator


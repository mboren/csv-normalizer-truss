import normalizer
import pytest


class TestConvertTimestamp:
    def test_simple_cast_dst(self):
        input_text = '4/1/11 11:00:00 AM'
        expected = '2011-04-01T14:00:00-04:00'
        assert normalizer.convert_timestamp(input_text) == expected

    def test_year_transition(self):
        input_text = '12/31/16 11:59:59 PM'
        expected = '2017-01-01T02:59:59-05:00'
        assert normalizer.convert_timestamp(input_text) == expected

    def test_dst_transition(self):
        input_text = '3/12/16 11:01:00 PM'
        expected = '2016-03-13T03:01:00-04:00'
        assert normalizer.convert_timestamp(input_text) == expected

    def test_timestamp_with_utf8_replacement_char(self):
        input_text = '3/12/1� 11:01:00 PM'

        with pytest.raises(normalizer.ParseError):
            normalizer.convert_timestamp(input_text)


class TestPadZipcode:
    def test_valid_zip(self):
        assert normalizer.pad_zipcode('94121') == '94121'

    def test_short_zip(self):
        assert normalizer.pad_zipcode('12') == '00012'

    def test_long_zip(self):
        assert normalizer.pad_zipcode('123456') == '123456'

    def test_nonnumeric_zip(self):
        with pytest.raises(normalizer.ParseError):
            normalizer.pad_zipcode('123�')


class TestConvertDuration:
    def test_zero_duration(self):
        assert normalizer.convert_duration('00:00:00.000') == '0'

    def test_nonzero_duration(self):
        assert normalizer.convert_duration('1:23:32.123') == '5012.123'

    def test_large_duration(self):
        assert normalizer.convert_duration('111:23:32.123') == '401012.123'

    def test_duration_with_utf8_replacement_char(self):
        with pytest.raises(normalizer.ParseError):
            normalizer.convert_duration('111:2�3:32.123')


class TestTotalDuration:
    def test_large_sum(self):
        assert normalizer.total_duration('5012.123', '401012.123') == '406024.246'

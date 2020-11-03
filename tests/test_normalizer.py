import normalizer


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

from solution import get_sequences, newValue, look_and_say

def test_sequencing():
    assert get_sequences(1) == [['1']]
    assert get_sequences(11) == [["1","1"]]
    assert get_sequences(21) == [["2"],["1"]]
    assert get_sequences(1211) == [["1"],["2"],["1","1"]]
    assert get_sequences(111221) == [["1","1","1"],["2","2"],["1"]]

def test_new_value():
    assert newValue(1) == '11'
    assert newValue(11) == '21'
    assert newValue(21) == '1211'
    assert newValue(1211) == '111221'
    assert newValue(111221) == '312211'

def test_look_and_say():
    result = ["11","21","1211","111221","312211"]
    for n, number in enumerate(look_and_say(1)):
        try: 
            assert result[n] == number
        except IndexError:
            return
 
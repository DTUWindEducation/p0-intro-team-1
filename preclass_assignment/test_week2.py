"""Test your functions from Week 2 assignment.
"""
import functions as fxn
import pytest  

def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect



def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    # Given
    length = 145  # Test input to function
    expected_output = "Just right :)\n"  # Expected output
    # When
    fxn.goldilocks(length)  # Run the function
    # Capture the printed output
    captured = capsys.readouterr()
    # Then
    assert captured.out.strip() == expected_output   # Check output matches expected
# test_goldilocks(capsys)



def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 4, 9] # test input to function
    exp_out = [1, 2, 3]   # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match
test_square_list()

def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    # given
    max_value = 30  # maximum value for fibonacci sequence
    expected_out = [1, 1, 2, 3, 5, 8, 13, 21]  # expected output

    # when
    output = fxn.fibonacci_stop(max_value)  # actual output
    # then
    assert output == expected_out #  Update the contents of this function so it correctly tests fibonacci_stop
test_fibonacci_stop()


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    x = [-1, 2, 6, 95]  # test input to function
    state = [1, 0, 0, 0]  # test input to function
    expected_out2 = [-999, 2, 6, 95]  # expected output

    # when
    result = fxn.clean_pitch(x, state)  # actual output
    
    # then
    assert result == expected_out2   #  Update the contents of this function so it correctly tests clean_pitch
test_clean_pitch()



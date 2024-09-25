"""Tests for statistics functions within the Model layer."""

import pandas as pd
import pytest

# Parameterisation for max_mag function testing
@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[1, 5, 3], [7, 8, 9], [3, 4, 1]], columns=list("abc")), "a", 7),
        (pd.DataFrame(data=[[0, 0, 0], [0, 0, 0], [0, 0, 0]], columns=list("abc")), "b", 0),
        (pd.DataFrame(data=[[1, 5, None], [7, 8, 9], [3, 4, 1]], columns=list("abc")), "c", 9),
    ])
def test_max_mag(test_df, test_colname, expected):
    """Test max function works for array of zeros and positive integers."""
    from lcanalyzer.models import max_mag
    assert max_mag(test_df, test_colname) == expected


def test_max_mag_strings():
    # Test for TypeError when passing a string
    from lcanalyzer.models import max_mag

    test_input_colname = "b"
    with pytest.raises(TypeError):
        error_expected = max_mag('string', test_input_colname)


# Parameterisation for min_mag function testing
@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[1, 5, 3], [7, 8, 9], [3, 4, 1]], columns=list("abc")), "a", 1),
        (pd.DataFrame(data=[[0, 0, 0], [0, 0, 0], [0, 0, 0]], columns=list("abc")), "b", 0),
        (pd.DataFrame(data=[[1, 5, None], [7, 8, 9], [3, 4, 1]], columns=list("abc")), "c", 1),
    ])
def test_min_mag(test_df, test_colname, expected):
    """Test min function works for array of zeros and positive integers."""
    from lcanalyzer.models import min_mag
    assert min_mag(test_df, test_colname) == expected


# Parameterisation for mean_mag function testing
@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[1, 5, 3], [7, 8, 9], [3, 4, 1]], columns=list("abc")), "a", pytest.approx(3.66,0.01)),
        (pd.DataFrame(data=[[0, 0, 0], [0, 0, 0], [0, 0, 0]], columns=list("abc")), "b", 0),
        (pd.DataFrame(data=[[1, 5, None], [7, 8, 9], [3, 4, 1]], columns=list("abc")), "c", 5),
    ])
def test_mean_mag(test_df, test_colname, expected):
    # Test that min_mag function works for integers
    from lcanalyzer.models import mean_mag
    assert mean_mag(test_df, test_colname) == expected


def test_calc_stat():
    # Test that calc_stat function works for integers
    from lcanalyzer.models import calc_stat 

    test_input_df1 = pd.DataFrame(data=[[9, 8, 8], 
                                        [7, 1, 3], 
                                        [5, 4, 1]], columns=list("abc"))
    test_input_df2 = pd.DataFrame(data=[[0, 8, 8], 
                                        [4, 1, 3], 
                                        [6, 4, 1]], columns=list("abc"))
    test_input_dict = {"x":test_input_df1, "y":test_input_df2} 
    test_input_string = "xy" 
    test_input_colname = "a"
    test_output = {"x_max":9, "y_max":6} 

    assert calc_stat(test_input_dict, test_input_string, test_input_colname) == test_output
    
    
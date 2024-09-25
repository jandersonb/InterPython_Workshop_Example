"""Tests for statistics functions within the Model layer."""

import pandas as pd
import pytest

def test_max_mag_strings():
    # Test for TypeError when passing a string
    from lcanalyzer.models import max_mag

    test_input_colname = "b"
    with pytest.raises(TypeError):
        error_expected = max_mag('string', test_input_colname)

def test_max_mag_integers():
    # Test that max_mag function works for integers
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 7

    assert max_mag(test_input_df, test_input_colname) == test_output

def test_max_mag_zeros():
    # Test that max_mag function works for zeros
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[0, 0, 0], 
                                       [0, 0, 0], 
                                       [0, 0, 0]], columns=list("abc"))
    test_input_colname = "b"
    test_output = 0

    assert max_mag(test_input_df, test_input_colname) == test_output

def test_min_mag_integers():
    # Test that min_mag function works for integers
    from lcanalyzer.models import min_mag

    test_input_df = pd.DataFrame(data=[[7, 8, 8], 
                                       [3, 1, 3], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 3

    assert min_mag(test_input_df, test_input_colname) == test_output

def test_mean_mag_integers():
    # Test that min_mag function works for integers
    from lcanalyzer.models import mean_mag

    test_input_df = pd.DataFrame(data=[[9, 8, 8], 
                                       [7, 1, 3], 
                                       [5, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 7

    assert mean_mag(test_input_df, test_input_colname) == test_output

def test_calc_stat_integers():
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
    
    
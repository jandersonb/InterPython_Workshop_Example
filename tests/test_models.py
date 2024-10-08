"""Tests for statistics functions within the Model layer."""

import pandas as pd
import pandas.testing as pdt
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


def test_calc_stats():
    # Test calc_stats function
    from lcanalyzer.models import calc_stats

    test_cols = list("abc")
    test_dict = {}
    test_dict["df0"] = pd.DataFrame(
        data=[[8, 8, 0], 
              [0, 1, 1], 
              [2, 3, 1], 
              [7, 9, 7]], columns=test_cols
    )
    test_dict["df1"] = pd.DataFrame(
        data=[[3, 8, 2], 
              [3, 8, 0], 
              [3, 9, 8], 
              [8, 2, 5]], columns=test_cols
    )
    test_dict["df2"] = pd.DataFrame(
        data=[[8, 4, 3], 
              [7, 6, 3], 
              [4, 2, 9], 
              [6, 4, 0]], columns=test_cols
    )
    test_output = pd.DataFrame(data=[[9,9,6],[5.25,6.75,4.],[1,2,2]],
                               columns=['df0','df1','df2'],
                               index=['max','mean','min'])
    
    pdt.assert_frame_equal(calc_stats(test_dict, test_dict.keys(), 'b'),
                           test_output,
                           check_exact=False,
                           atol=0.01)


# Parametrization for normalize_lc function testing with ValueError
@pytest.mark.parametrize(
    "test_input_df, test_input_colname, expected, expected_raises",
    [
        (pd.DataFrame(data=[[8, 9, 1], 
                            [1, 4, 1], 
                            [1, 2, 4], 
                            [1, 4, 1]], 
                      columns=list("abc")),
        "b",
        pd.Series(data=[1,0.285,0,0.285]),
        None),
        (pd.DataFrame(data=[[1, 1, 1], 
                            [1, 1, 1], 
                            [1, 1, 1], 
                            [1, 1, 1]], 
                      columns=list("abc")),
        "b",
        pd.Series(data=[0.,0.,0.,0.]),
        None),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        pd.Series(data=[0.,0.,0.,0.]),
        None),
        (pd.DataFrame(data=[[8, 9, 1], 
                            [1, -99.9, 1], 
                            [1, 2, 4], 
                            [1, 4, 1]], 
                      columns=list("abc")),
        "b",
        pd.Series(data=[1,0.285,0,0.285]),
        ValueError),
    ])
def test_normalize_lc(test_input_df, test_input_colname, expected, expected_raises):
    """Test how normalize_lc function works for arrays of nonnegative integers."""
    from lcanalyzer.models import normalize_lc
    import pandas.testing as pdt
    if expected_raises is not None:
        with pytest.raises(expected_raises):
            pdt.assert_series_equal(normalize_lc(test_input_df,test_input_colname),
                                    expected,
                                    check_exact=False,
                                    atol=0.01,
                                    check_names=False)
    else:
        pdt.assert_series_equal(normalize_lc(test_input_df,test_input_colname),
                                expected,
                                check_exact=False,
                                atol=0.01,
                                check_names=False)
    
    
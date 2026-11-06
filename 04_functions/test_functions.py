import pytest
from functions import calculate_average, is_passing, format_name


def test_average_of_three_scores():
    assert calculate_average([60, 70, 80]) == 70


def test_average_of_single_score():
    assert calculate_average([55]) == 55


def test_empty_list_raises_error():
    with pytest.raises(ValueError):
        calculate_average([])


def test_is_passing_true_and_false():
    assert is_passing(40) is True
    assert is_passing(39) is False


def test_format_name_cleans_spaces_and_case():
    assert format_name("  chinecherem", "UDE ") == "Ude, Chinecherem"

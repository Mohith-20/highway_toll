import pytest
from highway_toll import toll_for, toll_charge, pass_advice


def test_ambulance_is_exempt():
    assert toll_charge("ambulance", 2, False, False) == 0


def test_fire_engine_is_exempt():
    assert toll_charge("fire_engine", 4, True, True) == 0


def test_regular_vehicle_toll():
    assert toll_charge("car", 2, False, False) == 100


def test_two_axle_base_toll():
    assert toll_for(2, False, False) == 100


def test_three_axle_peak_toll():
    assert toll_for(3, True, False) == 187.5


def test_two_axle_fastag_discount():
    assert toll_for(2, False, True) == 90


def test_four_axle_fastag_discount():
    assert toll_for(4, False, True) == 237.5


def test_unknown_axle_category():
    assert toll_for(5, False, False) == 400


def test_invalid_axle_count():
    with pytest.raises(ValueError):
        toll_for(1, False, False)


def test_pass_advice_buy_pass():
    assert pass_advice(
        [(False, False), (False, False)], 2, 150
    ) == "buy_pass"


def test_pass_advice_either():
    assert pass_advice(
        [(False, False)], 2, 100
    ) == "either"


def test_pass_advice_pay_per_trip():
    assert pass_advice(
        [(False, False)], 2, 150
    ) == "pay_per_trip"
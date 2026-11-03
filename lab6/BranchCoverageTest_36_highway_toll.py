import pytest
from highway_toll import toll_for, toll_charge, pass_advice


# Invalid axle count
def test_invalid_axle_count():
    with pytest.raises(ValueError):
        toll_for(1, False, False)


# Known and unknown axle categories
@pytest.mark.parametrize(
    "axles, expected",
    [
        (2, 100),
        (3, 150),
        (4, 250),
        (5, 400)
    ]
)
def test_axle_categories(axles, expected):
    assert toll_for(axles, False, False) == expected


# Peak and non-peak pricing
def test_peak_pricing():
    assert toll_for(2, True, False) == 125


def test_non_peak_pricing():
    assert toll_for(2, False, False) == 100


# FASTag discounts
def test_fastag_two_axle_discount():
    assert toll_for(2, False, True) == 90


@pytest.mark.parametrize(
    "axles, expected",
    [
        (3, 142.5),
        (4, 237.5),
        (5, 380)
    ]
)
def test_fastag_other_axles(axles, expected):
    assert toll_for(axles, False, True) == expected


def test_peak_and_fastag_combined():
    assert toll_for(3, True, True) == 178.12


# Exempt and non-exempt vehicles
@pytest.mark.parametrize(
    "vehicle",
    ["ambulance", "fire_engine"]
)
def test_exempt_vehicles(vehicle):
    assert toll_charge(vehicle, 2, False, False) == 0


def test_non_exempt_vehicle():
    assert toll_charge("car", 2, False, False) == 100


# Pass advice decisions
def test_buy_pass():
    assert pass_advice(
        [(False, False), (False, False)], 2, 150
    ) == "buy_pass"


def test_exact_pass_price():
    assert pass_advice(
        [(False, False)], 2, 100
    ) == "either"


def test_pay_per_trip():
    assert pass_advice(
        [(False, False)], 2, 150
    ) == "pay_per_trip"


def test_empty_trip_list():
    assert pass_advice([], 2, 0) == "either"

import pytest

from elevator_dispatch import (
    next_direction,
    door_action,
    pick_elevator
)


# ==========================================
# NEXT DIRECTION TESTS
# ==========================================

def test_up_direction_with_requests_above():
    assert next_direction(3, "up", [5, 7]) == "up"


def test_up_direction_with_only_requests_below():
    assert next_direction(5, "up", [2, 3]) == "down"


def test_up_direction_with_no_requests():
    assert next_direction(5, "up", []) == "idle"


def test_down_direction_with_requests_below():
    assert next_direction(5, "down", [2, 3]) == "down"


def test_down_direction_with_only_requests_above():
    assert next_direction(3, "down", [5, 7]) == "up"


def test_down_direction_with_no_requests():
    assert next_direction(3, "down", []) == "idle"


def test_idle_direction_with_requests_above():
    assert next_direction(3, "idle", [5, 7]) == "up"


def test_idle_direction_with_requests_below():
    assert next_direction(5, "idle", [1, 2]) == "down"


def test_idle_direction_with_no_requests():
    assert next_direction(3, "idle", []) == "idle"


# ==========================================
# DOOR ACTION TESTS
# ==========================================

def test_emergency_holds_doors():
    assert door_action(100, False, True) == "hold_open"


def test_overload_condition():
    assert door_action(700, False, False) == "overload"


def test_blocked_door_reopens():
    assert door_action(100, True, False) == "reopen"


def test_normal_door_closes():
    assert door_action(100, False, False) == "close"


# ==========================================
# PICK ELEVATOR TESTS
# ==========================================

def test_pick_nearest_idle_elevator():
    cars = [
        ("A", 2, True),
        ("B", 8, True)
    ]
    assert pick_elevator(cars, 3) == "A"


def test_pick_elevator_with_busy_penalty():
    cars = [
        ("A", 3, False),
        ("B", 5, True)
    ]
    assert pick_elevator(cars, 4) == "B"


def test_pick_elevator_with_busy_car_still_closest():
    cars = [
        ("A", 4, False),
        ("B", 15, True)
    ]
    assert pick_elevator(cars, 4) == "A"


def test_pick_elevator_empty_list():
    assert pick_elevator([], 5) is None


def test_pick_first_elevator_on_equal_gap():
    cars = [
        ("A", 2, True),
        ("B", 4, True)
    ]
    assert pick_elevator(cars, 3) == "A"

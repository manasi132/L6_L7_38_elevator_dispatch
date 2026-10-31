import pytest

from elevator_dispatch import (
    next_direction,
    door_action,
    pick_elevator
)


# Next direction branches
@pytest.mark.parametrize(
    "current,direction,requests,expected",
    [
        (3, "up", [5], "up"),
        (3, "up", [1], "down"),
        (3, "up", [], "idle"),

        (3, "down", [1], "down"),
        (3, "down", [5], "up"),
        (3, "down", [], "idle"),

        (3, "idle", [5], "up"),
        (3, "idle", [1], "down"),
        (3, "idle", [], "idle"),
    ]
)
def test_next_direction_branches(
    current, direction, requests, expected
):
    assert next_direction(
        current, direction, requests
    ) == expected


# Door action branches
@pytest.mark.parametrize(
    "load,blocked,emergency,expected",
    [
        (100, False, True, "hold_open"),
        (700, False, False, "overload"),
        (630, True, False, "reopen"),
        (630, False, False, "close"),
    ]
)
def test_door_action_branches(
    load, blocked, emergency, expected
):
    assert door_action(
        load, blocked, emergency
    ) == expected


# Elevator selection branches
def test_pick_elevator_first_car():
    assert pick_elevator(
        [("A", 2, True)], 3
    ) == "A"


def test_pick_elevator_busy_penalty():
    assert pick_elevator(
        [
            ("A", 3, False),
            ("B", 5, True)
        ], 4
    ) == "B"


def test_pick_elevator_busy_car_still_wins():
    assert pick_elevator(
        [
            ("A", 4, False),
            ("B", 15, True)
        ], 4
    ) == "A"


def test_pick_elevator_equal_gap():
    assert pick_elevator(
        [
            ("A", 2, True),
            ("B", 4, True)
        ], 3
    ) == "A"


def test_pick_elevator_empty_list():
    assert pick_elevator([], 5) is None
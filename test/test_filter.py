from typing import Dict

import pytest

from json_schema_filter.filter import JsonSchemaFilter


class TestJsonSchemaFilter:
    @pytest.mark.parametrize(
        "input_schema, input_data, total_selected, total_rejected",
        [
            # no schema, empty input
            ({}, [], 0, 0),
            # equals match
            (
                {"properties": {"greeting": {"type": "string", "equals": "hello"}}},
                [{"greeting": "hello"}, {"greeting": "hi"}],
                1,
                1,
            ),
            # iequals match
            (
                {"properties": {"greeting": {"type": "string", "iequals": "hello"}}},
                [{"greeting": "HELLO"}, {"greeting": "Hello"}],
                2,
                0,
            ),
            # iequals on non-string
            (
                {"properties": {"greeting": {"type": "number", "iequals": "hello"}}},
                [{"greeting": 1}],
                0,
                1,
            ),
            # nequals happy path
            (
                {"properties": {"greeting": {"type": "number", "nequals": 1}}},
                [{"greeting": 2}],
                1,
                0,
            ),
            # nequals rejected due to valid check
            (
                {"properties": {"greeting": {"type": "number", "nequals": 1}}},
                [{"greeting": 1}],
                0,
                1,
            ),
        ],
    )
    def test_filter(
        self,
        input_schema: Dict,
        input_data: Dict,
        total_selected: int,
        total_rejected: int,
    ):
        filtered_result = JsonSchemaFilter(schema=input_schema).filter(
            input_data=input_data
        )
        assert filtered_result.total_selected == total_selected
        assert filtered_result.total_rejected == total_rejected

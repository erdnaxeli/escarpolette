import hypothesis.strategies as st
import pytest
from hypothesis import given
from pydantic import ValidationError

from escarpolette.schemas import ItemSchemaIn


def test_item_schema_in__url__ok():
    ItemSchemaIn(url="http://perdu.com")


@given(st.text())
def test_item_schema_in__url__nok(url):
    with pytest.raises(ValidationError):
        ItemSchemaIn(url=url)

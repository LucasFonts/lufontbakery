from conftest import check_id
from fontTools.ttLib import TTFont

from fontbakery.codetesting import (
    TEST_FILE,
    assert_PASS,
    assert_results_contain,
)
from fontbakery.status import FAIL


@check_id("nested_components")
def test_check_nested_components(check):
    """Ensure glyphs do not have components which are themselves components."""

    ttFont = TTFont(TEST_FILE("nunito/Nunito-Regular.ttf"))
    assert_PASS(check(ttFont))

    # We need to create a nested component. "second" has components, so setting
    # one of "quotedbl"'s components to "second" should do it.
    # pylint: disable=[E1136]  # false positive
    ttFont["glyf"]["quotedbl"].components[0].glyphName = "second"
    # pylint: enable=[E1136]

    assert_results_contain(check(ttFont), FAIL, "found-nested-components")

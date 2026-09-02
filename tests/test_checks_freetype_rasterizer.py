from conftest import check_id

from fontbakery.codetesting import (
    TEST_FILE,
    assert_PASS,
    assert_results_contain,
)
from fontbakery.status import FAIL


@check_id("freetype_rasterizer")
def test_check_freetype_rasterizer(check):
    """Ensure that the font can be rasterized by FreeType."""

    font = TEST_FILE("cabin/Cabin-Regular.ttf")
    assert_PASS(check(font), "with a good font...")

    font = TEST_FILE("ancho/AnchoGX.ttf")
    msg = assert_results_contain(check(font), FAIL, "freetype-crash")
    assert "FT_Exception:  (too many function definitions)" in msg

    font = TEST_FILE("rubik/Rubik-Italic.ttf")
    msg = assert_results_contain(check(font), FAIL, "freetype-crash")
    assert "FT_Exception:  (stack overflow)" in msg

    # Example that segfaults with 'freetype-py' version 2.4.0
    font = TEST_FILE("source-sans-pro/VAR/SourceSansVariable-Italic.ttf")
    assert_PASS(check(font), "with a good font...")

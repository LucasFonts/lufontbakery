from conftest import check_id

from fontbakery.codetesting import (
    TEST_FILE,
    assert_PASS,
    assert_results_contain,
)
from fontbakery.status import FAIL, WARN


@check_id("ots")
def test_check_ots(check):
    """Checking with ots-sanitize."""

    fine_font = TEST_FILE("cabin/Cabin-Regular.ttf")
    assert_PASS(check(fine_font))

    warn_font = TEST_FILE("bad_fonts/ots/bad_post_version.otf")
    message = assert_results_contain(check(warn_font), WARN, "ots-sanitize-warn")
    assert message is not None
    assert (
        "WARNING: post: Only version supported for fonts with CFF table is"
        " 0x00030000 not 0x20000" in message
    )

    bad_font = TEST_FILE("bad_fonts/ots/no_glyph_data.ttf")
    message = assert_results_contain(check(bad_font), FAIL, "ots-sanitize-error")
    assert message is not None
    assert "ERROR: no supported glyph data table(s) present" in message
    # assert "Failed to sanitize file!" in message

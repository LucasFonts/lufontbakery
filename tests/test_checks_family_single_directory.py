from conftest import check_id

from fontbakery.codetesting import (
    TEST_FILE,
    assert_PASS,
    assert_results_contain,
)
from fontbakery.status import FAIL


@check_id("family/single_directory")
def test_check_family_single_directory(check):
    """Fonts are all in the same directory."""

    same_dir = [
        TEST_FILE("cabin/Cabin-Thin.ttf"),
        TEST_FILE("cabin/Cabin-ExtraLight.ttf"),
    ]
    multiple_dirs = [
        TEST_FILE("mada/Mada-Regular.ttf"),
        TEST_FILE("cabin/Cabin-ExtraLight.ttf"),
    ]

    assert_PASS(check(same_dir), f"with same dir: {same_dir}")

    assert_results_contain(
        check(multiple_dirs),
        FAIL,
        "single-directory",
        f"with multiple dirs: {multiple_dirs}",
    )

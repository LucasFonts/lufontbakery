from fontbakery.prelude import WARN, Message, check


@check(
    id="ots",
    rationale="""
       The OpenType Sanitizer (OTS) is a tool that checks that the font is
       structually well-formed and passes various sanity checks. It is used by
       many web browsers to check web fonts before using them; fonts which fail
       such checks are blocked by browsers.

       This check runs OTS on the font and reports any errors or warnings that
       it finds.
       """,
    proposal="https://github.com/fonttools/fontbakery/issues/4829",  # legacy check
)
def check_ots(font):
    """Checking with ots-sanitize."""
    import pyots

    result = pyots.sanitize(font.file)

    if not result.sanitized and result.messages:
        messages = [m for m in result.messages if m]
        if messages:
            yield (
                WARN,
                Message(
                    "ots-sanitize-warn",
                    "ots-sanitize passed this file, however warnings were printed:\n\n"
                    f"{'\n'.join(messages)}",
                ),
            )

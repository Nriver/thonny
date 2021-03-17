from thonny.plugins.pip_gui import _EXTRA_MARKER_RE


def test_extra_marker_re() -> None:
    for text in [
        "extra == 'dev'",
        r"extra == 'dev \' with quote'",
        "  extra  ==  'dev'  ",
        'extra == "dev"',
        r'extra == "dev \"with quote"',
    ]:
        assert _EXTRA_MARKER_RE.match(text) is not None

    for text in ["extra == 'dev' and extra == 'dev1'", "extra == 'dev' or extra == 'dev1'"]:
        assert _EXTRA_MARKER_RE.match(text) is None

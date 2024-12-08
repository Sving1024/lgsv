import sys

import pytest

try:
    import luogu
    import setting
except ModuleNotFoundError:
    from lgsv import luogu, setting

def test_luogu_training():
    t=luogu.Training("100")
    t.fetch_resources()
    md = t.get_markdown(["b", "d", "if", "of", "s", "h", "tr"])
    with open("./100.md",encoding="utf-8") as f:
        assert f.read() == md

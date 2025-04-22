import sys

import pytest
import pathlib
from lgsv import luogu
import asyncio

basepath = pathlib.Path(__file__).parent


def test_luogu_training():
    """test training class"""
    t = luogu.Training("100")
    asyncio.run(t.fetch_resources())
    md = t.get_markdown(["b", "d", "if", "of", "s", "h", "tr"])
    with open(basepath / "sample" / "t100.md", encoding="utf-8") as f:
        assert f.read() == md

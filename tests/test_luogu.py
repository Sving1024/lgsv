"""
test lgsv.luogu
"""

import asyncio
import pathlib

from lgsv import luogu

basepath = pathlib.Path(__file__).parent


def test_luogu_training():
    """test training class"""
    t = luogu.Training("100")
    asyncio.run(t.fetch_resources())
    md = t.get_markdown(["b", "d", "if", "of", "s", "h", "tr"])
    with open(basepath / "sample" / "t100.md", encoding="utf-8") as f:
        assert f.read() == md


def test_luogu_filter():
    """test filter class"""
    f = luogu.ProblemFilter(
        diffclty=[0, 1, 2, 3, 4, 5],
        include_tags=["tag1", "tag2"],
        exclude_tags=["tag3"],
    )
    assert f.diffclty == [0, 1, 2, 3, 4, 5]
    assert f.include_tags == ["tag1", "tag2"]
    assert f.exclude_tags == ["tag3"]
    assert f.accepted is False
    assert f.submitted is False
    problem = luogu.Problem(problem_id="P1001")
    asyncio.run(problem.fetch_resources())
    assert True

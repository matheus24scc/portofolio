import os, tempfile, json
from portofolio import core

def test_build():
    d = tempfile.mkdtemp(); data = {"name": "Ana", "bio": "dev", "projects": [{"title": "X", "url": "http://x"}]}
    out = os.path.join(d, "index.html")
    core.build(data, out)
    html = open(out).read()
    assert "Ana" in html and "X" in html

def test_build_empty():
    d = tempfile.mkdtemp(); out = os.path.join(d, "i.html")
    core.build({}, out)
    assert os.path.exists(out)

def test_links():
    d = tempfile.mkdtemp(); out = os.path.join(d, "i.html")
    core.build({"links": {"GitHub": "http://gh"}}, out)
    assert "GitHub" in open(out).read()

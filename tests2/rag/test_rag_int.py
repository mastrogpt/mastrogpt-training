import os, requests as req
def test_rag():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/rag/rag"
    res = req.get(url).json()
    assert res.get("output") == "rag"

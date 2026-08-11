from app.tools import ToolError, ToolRegistry


class S:
    workspace = "/tmp/asi-os-test"
    shell_timeout = 5

def test_write_and_read(tmp_path):
    S.workspace = str(tmp_path)
    t = ToolRegistry(S())
    assert t.execute("write_file", {"path":"a.txt","content":"abc"})["ok"]
    assert t.execute("read_file", {"path":"a.txt"})["content"] == "abc"

def test_path_escape(tmp_path):
    S.workspace = str(tmp_path)
    t = ToolRegistry(S())
    try:
        t.execute("read_file", {"path":"../secret"})
        assert False
    except ToolError:
        assert True

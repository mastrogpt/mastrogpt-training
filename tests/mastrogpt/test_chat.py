import sys
sys.path.append("packages/mastrogpt/chat")
import chat as m

def test_chat():
    args = {}
    m.url(args, "generate")

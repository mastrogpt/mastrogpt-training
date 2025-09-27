import os, json, requests as req

from tests.streamock import args

MODEL = "llama3.2-vision:11b"

def collect(lines):
  out = ""
  for line in lines:
    #line = next(lines)
    chunk = json.loads(line.decode("UTF-8"))
    out +=  chunk.get("message", {}).get("content", "")
  return out

class Vision:
  def __init__(self, args):
    host = args.get("OLLAMA_HOSTPORT", os.getenv("OLLAMA_HOSTPORT")) or args.get("OLLAMA_HOST", os.getenv("OLLAMA_HOST"))
    auth = args.get("OLLAMA_AUTH", os.getenv("OLLAMA_AUTH")) or args.get("AUTH", os.getenv("AUTH"))
    proto = args.get("OLLAMA_PROTO", os.getenv("OLLAMA_PROTO")) or "https"
    self.url = f"{proto}://{auth}@{host}/api/chat"

  def decode(self, img):
    msg = {
      "model": MODEL,
      "messages": [ {
        "role": "user",
        "content": "what is in this image?",
        "images": [img]
      }]
    }
    lines = req.post(self.url, json=msg, stream=True).iter_lines()
    return collect(lines)

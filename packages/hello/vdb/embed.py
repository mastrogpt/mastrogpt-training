import os, requests as req
MODEL="mxbai-embed-large:latest"
DIMENSION=1024

def url(args):
    host = args.get("OLLAMA_HOST", os.getenv("OLLAMA_HOST"))
    auth = args.get("AUTH", os.getenv("AUTH"))
    proto = args.get("OLLAMA_PROTO", os.getenv("OLLAMA_PROTO", "https"))
    url = f"{proto}://{auth}@{host}/api/embeddings"
    return url

def embed(url, inp):    
  msg = { "model": MODEL, "prompt": inp, "stream": False }
  res = req.post(url, json=msg).json()
  out = res.get('embedding', [])
  return out

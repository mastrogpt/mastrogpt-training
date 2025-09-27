import os, requests as req
MODEL="mxbai-embed-large:latest"
DIMENSION=1024

def url(args):
    host = args.get("OLLAMA_HOSTPORT", os.getenv("OLLAMA_HOSTPORT")) or args.get("OLLAMA_HOST", os.getenv("OLLAMA_HOST"))
    auth = args.get("OLLAMA_AUTH", os.getenv("OLLAMA_AUTH")) or args.get("AUTH", os.getenv("AUTH"))
    proto = args.get("OLLAMA_PROTO", os.getenv("OLLAMA_PROTO")) or "https"
    url = f"{proto}://{auth}@{host}/api/embeddings"
    return url

def embed(url, inp):    
  msg = { "model": MODEL, "prompt": inp, "stream": False }
  res = req.post(url, json=msg).json()
  out = res.get('embedding', [])
  return out

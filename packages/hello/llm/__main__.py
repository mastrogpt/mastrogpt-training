#--kind python:default
#--web true
#--param "OLLAMA_PROTO" "$OLLAMA_PROTO"
#--param "OLLAMA_HOST" "$OLLAMA_HOST"
#--param "AUTH" "$AUTH"

import llm
def main(args):
  return { "body": llm.llm(args) }

#--kind python:default
#--web true
#--param "OLLAMA_HOST" "$OLLAMA_HOST"
#--param "AUTH" "$AUTH"
#--param "OLLAMA_HOSTPORT" "$OLLAMA_HOSTPORT"
#--param "OLLAMA_AUTH" "$OLLAMA_AUTH"
#--param "OLLAMA_PROTO" "$OLLAMA_PROTO"

import puzzle
def main(args):
  return { "body": puzzle.puzzle(args) }

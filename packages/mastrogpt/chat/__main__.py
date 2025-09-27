#--kind python:default
#--web true
#--param "OLLAMA_HOST" "$OLLAMA_HOST"
#--param "AUTH" "$AUTH"
#--param "OLLAMA_HOSTPORT" "$OLLAMA_HOSTPORT"
#--param "OLLAMA_AUTH" "$OLLAMA_AUTH"
#--param "OLLAMA_PROTO" "$OLLAMA_PROTO"
#--annotation index '80:Demo:Ollama:pinocchio:'

import chat
def main(args):
  return { "body": chat.chat(args) }


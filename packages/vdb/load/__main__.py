#--kind python:default
#--web true
#--param "OLLAMA_HOST" "$OLLAMA_HOST"
#--param "AUTH" "$AUTH"
#--param "OLLAMA_HOSTPORT" "$OLLAMA_HOSTPORT"
#--param "OLLAMA_AUTH" "$OLLAMA_AUTH"
#--param "OLLAMA_PROTO" "$OLLAMA_PROTO"
#--param MILVUS_HOST $MILVUS_HOST
#--param MILVUS_PORT $MILVUS_PORT
#--param MILVUS_DB_NAME $MILVUS_DB_NAME
#--param MILVUS_TOKEN $MILVUS_TOKEN
import load
def main(args):
  return { "body": load.load(args) }

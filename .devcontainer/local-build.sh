#!/bin/bash
cd "$(dirname $0)"
source .env
TAG=$(jq -r .image <devcontainer.json | awk -F: '{print $2}')
LATEST=https://api.github.com/repos/apache/openserverless-cli/releases/latest
OPS_VERSION=$(curl -s  "$LATEST" | jq -r '.name | .[1:]')
DH_USER=sciabarracom
DH_BUILDER=openserverless-builder
DH_IMAGE=$DH_USER/mastrogpt-starter
DH_TOKEN=${DOCKERHUB_TOKEN:?please set DOCKERHUB_TOKEN in .env} 
docker login -u "$DH_USER" -p "$DH_TOKEN"
docker buildx create  --driver cloud $DH_USER/$DH_BUILDER
nohup docker buildx build --no-cache \
  --build-arg OPS_VERSION=$OPS_VERSION \
  --builder cloud-$DH_USER-$DH_BUILDER \
  --platform linux/amd64,linux/arm64 \
  -t $DH_IMAGE:$TAG . --push &
tail -f nohup.out

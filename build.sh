#!/bin/bash

set -e

VERSION_FILE=".default_version"

if [ -f "$VERSION_FILE" ]; then
    DEFAULT_VERSION=$(cat "$VERSION_FILE")
else
    DEFAULT_VERSION="0.2.0"
fi

VERSION=${1:-$DEFAULT_VERSION}

echo "$VERSION" > "$VERSION_FILE"

git tag -a "release-$VERSION" -m "Release $VERSION"
git push origin "release-$VERSION"




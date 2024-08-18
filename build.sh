#! /bin/bash

set -e

DEFAULT_VERSION="0.1.0"

VERSION=${1:-$DEFAULT_VERSION}

git tag -a release-$VERSION -m "Release $VERSION"
git push origin release-$VERSION




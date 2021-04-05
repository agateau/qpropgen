#!/bin/sh
set -e

echo "---> Running unit tests"
pytest

echo "---> Building examples"
cd $(dirname $0)/examples
rm -rf build
mkdir build
cd build
cmake -G Ninja ..
ninja

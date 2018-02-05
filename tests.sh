#!/bin/sh
set -e
cd $(dirname $0)/examples
rm -rf build
mkdir build
cd build
cmake ..
cmake --build .

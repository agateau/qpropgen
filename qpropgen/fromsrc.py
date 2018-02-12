#!/usr/bin/env python3
# Script to run qpropgen without installing it. Useful when bundling propgen
# in a source tree.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))

from qpropgen.main import main

sys.exit(main())

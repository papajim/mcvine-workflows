#!/usr/bin/env python
import sys
import os
import csv
from datetime import datetime
from Pegasus.DAX3 import *
from optparse import OptionParser

# API Documentation: http://pegasus.isi.edu/documentation

base_dir = os.path.abspath('.')

# Create a abstract dag
ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
workflow = ADAG("mcvine-instrument-%s" % ts)

# Write the DAX to file
with open("instrument.dax", "w") as f:
    workflow.writeXML(f)

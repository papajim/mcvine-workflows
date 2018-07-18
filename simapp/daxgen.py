#!/usr/bin/env python
import sys
import os
import csv
import yaml
from datetime import datetime
from Pegasus.DAX3 import *
from optparse import OptionParser

# API Documentation: http://pegasus.isi.edu/documentation

# Load config
with open("config.yml", 'r') as f:
    cfg = yaml.load(f)

# Create a abstract dag
ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
workflow = ADAG("simapp1-%s" % ts)

# Config file for simmapp1 job
config_in = File("simapp1.pml")
# Energy output from simapp1 job
energy_dat = File("IE.dat")
energy_hdf5 = File("IE.h5")

simapp1_job = Job(name="simapp1")
simapp1_job.addArguments("--output-dir=.",
                         "--ncount=" + cfg["simapp1"]["neutrons"])
                         "--mpirun.nodes=" + cfg["simapp1"]["cores"],
                         "--overwrite-datafiles")
simapp1_job.uses(config_in, link=Link.INPUT)
simapp1_job.uses(energy_dat, link=Link.OUTPUT, register=True, transfer=True)
simapp1_job.uses(energy_hdf5, link=Link.OUTPUT, register=True, transfer=True)

simapp1_job.profile("pegasus", "cores", cfg["simapp1"]["cores"])

workflow.addJob(simapp1_job)

# Energy plot from post processing job
energy_plot = File("energy.png")

post_job = Job(name="postprocessing")
post_job.uses(energy_hdf5, link=Link.INPUT)
post_job.uses(energy_plot, link=Link.OUTPUT, register=True, transfer=True)
workflow.addJob(post_job)


with open("simapp1.dax", 'w') as f:
    workflow.writeXML(f)

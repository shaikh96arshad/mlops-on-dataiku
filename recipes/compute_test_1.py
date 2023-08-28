# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
covid19___orignal = dataiku.Dataset("covid19___orignal")
covid19___orignal_df = covid19___orignal.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_1_df = covid19__orignal_df.head(3)

test_1_df = covid19___orignal_df # For this sample code, simply copy input to output


# Write recipe outputs
test_1 = dataiku.Dataset("test_1")
test_1.write_with_schema(test_1_df)

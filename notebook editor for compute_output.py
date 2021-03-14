
# coding: utf-8

# In[ ]:



import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
airline_tweets_unique = dataiku.Dataset("airline_tweets_unique")
airline_tweets_unique_df = airline_tweets_unique.get_dataframe()

##test

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

output_df = airline_tweets_unique_df # For this sample code, simply copy input to output


# Write recipe outputs
output = dataiku.Dataset("output")
output.write_with_schema(output_df)


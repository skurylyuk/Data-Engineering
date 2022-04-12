

from Inspections_EDA import preprocess_df
from fetch_data import get_data
import pandas as pd
from sodapy import Socrata
from sqlalchemy import create_engine, inspect
import sqlite3
import matplotlib.pyplot as plt
import os
import numpy as np

def run_pipeline():
	data= get_data()
	df_new= preprocess_df(data)


run_pipeline()




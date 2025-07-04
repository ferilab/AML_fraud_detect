
import os
import sys
import kaggle
import pandas as pd

from src import train_model

filepath = "data/Big_Black_Money_Dataset.csv"

# Let's train and validate a model and save it
train_model.train_and_save_model(filepath)

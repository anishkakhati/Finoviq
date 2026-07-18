import numpy as np


def validate_features(data):

    print("\n========== VALIDATING ENGINEERED FEATURES ==========\n")

    print("Checking Missing Values...\n")

    missing = data.isnull().sum()

    print(missing)
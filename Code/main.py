import pandas as pd

train_df = pd.read_csv("../train.csv", delimiter=";")
test_df = pd.read_csv("../test.csv", delimiter=";")
sample_submission_df = pd.read_csv("../sample_submission.csv", delimiter=";")
print(train_df)
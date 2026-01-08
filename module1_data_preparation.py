import csv, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "heart.csv")

def load_data():
    with open(DATA_PATH) as f:
        reader = csv.reader(f)
        header = next(reader)
        data = [row for row in reader]
    return header, data

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEST_DATA_DIR = os.path.join(BASE_DIR, 'TestData')

print(TEST_DATA_DIR)
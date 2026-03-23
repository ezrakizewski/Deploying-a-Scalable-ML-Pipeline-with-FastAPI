import pytest
import pandas as pd
import os
import pickle
import math
from sklearn.ensemble import RandomForestClassifier

# ------------------ Fixtures ------------------

@pytest.fixture
def project_path():
    return "."

@pytest.fixture
def loaded_model(project_path):
    model_path = os.path.join(project_path, "model", "model.pkl")
    with open(model_path, "rb") as f:
        return pickle.load(f)

@pytest.fixture
def loaded_encoder(project_path):
    encoder_path = os.path.join(project_path, "model", "encoder.pkl")
    with open(encoder_path, "rb") as f:
        return pickle.load(f)
    
@pytest.fixture
def data(project_path):
    data_path = os.path.join(project_path, "data", "census.csv")
    return pd.read_csv(data_path)

# ------------------ TESTS ------------------

def test_dataset_split_size_is_valid(data):
    """
    # Read in the census.csv dataset and verify that the record count is 32,561
    """
    assert len(data) == 32561
    assert math.ceil(len(data) * 0.8) == 26049
    assert math.floor(len(data) * 0.2) == 6512


def test_model_loads_and_is_type_RandomForestClassifier(loaded_model):
    """
    # Check if the loaded model is of type RandomForestClassifier
    """   
     # Verify the loaded object is the expected model type
    assert isinstance(loaded_model, RandomForestClassifier), (
        f"Expected RandomForestClassifier, got {type(loaded_model)}"
    )


def test_encoder_knows_expected_categories(loaded_encoder):
    """Test that the encoder was fitted on the expected number of features."""
    # RandomForest with 8 categorical features should have 8 categories lists
    assert len(loaded_encoder.categories_) == 8, \
        f"Expected 8 categorical feature groups, got {len(loaded_encoder.categories_)}"

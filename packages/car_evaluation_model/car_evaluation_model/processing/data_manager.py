import joblib
import pandas as pd
from pathlib import Path
from car_evaluation_model.config.core import INTERIM_DATA_DIR, TRAINED_MODEL_DIR, config
from sklearn.model_selection import train_test_split

from car_evaluation_model import __version__ as _version


def load_dataset(path_to_data, names=None):
    """
    Load the data into memory
    
    Parameters
    ----------
    :param path_to_data: data file location.
    :param names: specify the give names of each column.
    :return the dataset that has been loaded into memory. 
    """
    if names: 
        dataset = pd.read_csv(
            path_to_data,
            names = config.model_config.column_names
            )
    else: 
        dataset = pd.read_csv(path_to_data)
        
    return dataset

def create_train_and_test(data):
    """
    Create the training and test set. Both datasets are 
    automatically saved as interim data. 

    :param data: the data to split into train and test sets
    """
    data = data.copy()
    
    # Convert labels to numeric
    data.loc[:, config.model_config.target] = data.loc[:, config.model_config.target].map(
        config.model_config.class_mappings
        )

    # Split data into features and labels
    X = data[config.model_config.features]
    y = data[config.model_config.target]

    # Create train and test splits 
    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        y, 
        test_size = config.model_config.test_size,
        random_state = config.model_config.random_state
    )
    
    # Join the labels to the features to create one dataframe
    train_data = pd.concat([X_train, y_train], axis=1)
    test_data = pd.concat([X_test, y_test], axis=1)

    # Save data files. 
    train_data.to_csv(
        Path(f"{INTERIM_DATA_DIR}/{config.app_config.train_data}"),
        index=False
        )
    test_data.to_csv(
        Path(f"{INTERIM_DATA_DIR}/{config.app_config.test_data}"),
        index=False)

    return X_train, X_test, y_train, y_test
    

def save_pipeline(*, pipeline_to_persist):
    """
    Persist the pipeline. Saves the versioned model, and overwrites 
    any previous saved models. This ensures that when the package is
    published, there is only one trained model that can be
    called, and we know exactly how it was built.
    """

    # Prepare versioned save file name
    save_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
    save_path = TRAINED_MODEL_DIR / save_file_name

    remove_old_pipelines(files_to_keep=[save_file_name])
    joblib.dump(pipeline_to_persist, save_path)


def load_pipeline(*, file_name):
    """Load a persisted pipeline."""

    file_path = TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model


def remove_old_pipelines(*, files_to_keep) -> None:
    """
    Remove old model pipelines.
    This is to ensure there is a simple one-to-one
    mapping between the package version and the model
    version to be imported and used by other applications.
    """
    do_not_delete = files_to_keep + ["__init__.py"]
    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()

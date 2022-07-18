import logging
from pathlib import Path

from config.core import RAW_DATA_DIR, config
from pipeline import car_evaluation_pipe
from processing import data_manager as dm

from car_evaluation_model import __version__ as _version

_logger = logging.getLogger(__name__)

def run_training():
    """Train the model"""

    # Read the training data
    dataset = dm.load_dataset(
        path_to_data= Path(f"{RAW_DATA_DIR}/{config.app_config.data}"),
        names=True
        )

    # Create train and test sets 
    X_train, _, y_train, _ = dm.create_train_and_test(data=dataset)

    # Train the pipeline 
    car_evaluation_pipe.fit(X_train, y_train)

    # Persist the trained model 
    _logger.warning(f"saving model version: {_version}")
    dm.save_pipeline(pipeline_to_persist=car_evaluation_pipe)

if __name__ == "__main__":
    run_training()

import logging
from pathlib import Path 

import pandas as pd  

from car_evaluation_model import __version__ as _version
from car_evaluation_model.config.core import config
from car_evaluation_model.processing import data_manager as dm
from car_evaluation_model.processing.validation import validate_inputs

_logger = logging.getLogger(__name__)

pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
_car_evaluation_pipe = dm.load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, inputs):
    """Make a prediction using a saved model pipeline."""

    input_df = pd.DataFrame(inputs)

    validated_data, errors = validate_inputs(inputs=input_df)
    results = {"predictions": None, "version": _version, "errors": errors}

    if not errors:
        predictions = _car_evaluation_pipe.predict(
            X=pd.DataFrame(validated_data)
        )
        _logger.info(
            f"Making predictions with model version: {_version} "
            f"Predictions: {predictions}"
        )
        results = {
            "predictions": predictions.tolist(),
            "version": _version,
            "errors": errors,
        }

    return results
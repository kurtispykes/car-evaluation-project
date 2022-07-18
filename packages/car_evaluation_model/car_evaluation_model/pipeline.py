import logging
from multiprocessing.connection import Pipe 

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression 
from sklearn.preprocessing import FunctionTransformer

from car_evaluation_model.config.core import config 
from car_evaluation_model.processing import features as f

_logger = logging.getLogger(__name__)

# Define pipeline 
car_evaluation_pipe = Pipeline(
    [
        (
            "get_buying_and_maint_mappings",
            FunctionTransformer(func=f.convert_mapping, 
            kw_args = {"columns": config.model_config.buying_and_maint,
            "values_to_replace": config.model_config.buying_and_maint_mappings}
            )
        ),
        (
            "get_doors_mappings",
            FunctionTransformer(func=f.convert_mapping, 
            kw_args = {"columns": config.model_config.doors,
            "values_to_replace": config.model_config.doors_mappings}
            )
        ),
        (
            "get_persons_mappings",
            FunctionTransformer(func=f.convert_mapping, 
            kw_args = {"columns": config.model_config.persons,
            "values_to_replace": config.model_config.persons_mappings}
            )
        ),
        (
            "get_lug_boot_mappings",
            FunctionTransformer(func=f.convert_mapping, 
            kw_args = {"columns": config.model_config.lug_boot,
            "values_to_replace": config.model_config.lug_boot_mappings}
            )
        ),
        (
            "get_safety_mappings",
            FunctionTransformer(func=f.convert_mapping,
            kw_args = {"columns": config.model_config.safety,
            "values_to_replace": config.model_config.safety_mappings}
            )
        ),
        (
            "logistic_regression",
            LogisticRegression(random_state=config.model_config.random_state)
        )
    ]
)
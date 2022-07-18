import typing as t

import numpy as np
import pandas as pd  
from pydantic import BaseModel, ValidationError

from car_evaluation_model.config.core import config


def validate_inputs(*, inputs: pd.DataFrame):
    """Check model inputs for unprocessable values."""
    # replace numpy nans so that Marshmallow can validate
    data_ = inputs.replace({np.nan: None}).to_dict(orient="records")
    errors = None

    try:
        MultipleCarTransactionInputData(inputs=data_)
    except ValidationError as exc:
        errors = exc.json()

    return data_, errors


class CarTransactionInputData(BaseModel):
    buying: t.Optional[str]
    maint: t.Optional[str]
    doors: t.Optional[str]
    persons: t.Optional[str]
    lug_boot: t.Optional[str]
    safety: t.Optional[str]

class MultipleCarTransactionInputData(BaseModel):
    inputs: t.List[CarTransactionInputData]
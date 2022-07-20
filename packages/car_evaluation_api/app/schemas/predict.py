from typing import Any, List, Optional

from car_evaluation_model.processing import validation as v
from pydantic import BaseModel


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[int]]


class MultipleCarTransactionInputData(BaseModel):
    inputs: List[v.CarTransactionInputData]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "buying": "vhigh",
                        "maint": "med",
                        "doors": 4, 
                        "persons": "more",
                        "lug_boot": "med",
                        "safety": "high"
                    }
                ]
            }
        }
        
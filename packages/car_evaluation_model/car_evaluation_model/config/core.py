from pathlib import Path

import strictyaml
from pydantic import BaseModel

import car_evaluation_model

# Project directories 
PACKAGE_ROOT = Path(car_evaluation_model.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"
DATASET_DIR = PACKAGE_ROOT / "data"
RAW_DATA_DIR = DATASET_DIR / "raw"
INTERIM_DATA_DIR = DATASET_DIR / "interim"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "models"


class AppConfig(BaseModel): 
    """
    Application level configuration. 
    """
    package_name: str 
    pipeline_name: str
    pipeline_save_file: str
    data: str
    train_data: str
    test_data: str 

class ModelConfig(BaseModel): 
    """
    All configuration relevant to model 
    training and feature engineering
    """
    features: list
    column_names: list
    target: str
    buying: str 
    maint: str 
    doors: str
    persons: str
    lug_boot: str
    safety: str
    buying_and_maint: list
    buying_and_maint_mappings: dict
    doors_mappings: dict
    persons_mappings: dict
    lug_boot_mappings: dict
    safety_mappings: dict
    class_mappings: dict
    random_state: int
    test_size: float

class Config(BaseModel): 
    """Master config object"""
    app_config: AppConfig
    model_config: ModelConfig

def find_config_file(): 
    """Locate the configuration file"""
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    raise Exception(f"Config not found at {CONFIG_FILE_PATH}")

def fetch_config_from_yaml(cfg_path= None):
    "Parse YAML containing the package configuration."

    if not cfg_path:
        cfg_path = find_config_file()

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = strictyaml.load(conf_file.read())
            return parsed_config
    raise OSError(f"Did not find confige file at path: {cfg_path}")

def create_and_validate_config(parsed_config= None):
    """Run validation on config values."""
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()

    # specify the data attribute from the strictyaml YAML type.
    _config = Config(
        app_config=AppConfig(**parsed_config.data),
        model_config=ModelConfig(**parsed_config.data),
    )
    return _config


config = create_and_validate_config()
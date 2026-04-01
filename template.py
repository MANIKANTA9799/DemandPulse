import os
from pathlib import Path
from datetime import datetime

project_name = "src"

list_of_files = [

    # core
    f"{project_name}/__init__.py",

    # components (core ML logic)
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/components/drift_detection.py",

    # pipelines
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/pipeline/retraining_pipeline.py",

    # configuration
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/aws_connection.py",

    # cloud
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",

    # data access
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/data_loader.py",

    # constants (VERY IMPORTANT)
    f"{project_name}/constants/__init__.py",
    f"{project_name}/constants/constants.py",

    # entity
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",

    # logging & exception
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/custom_exception.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/logger/logger.py",

    # utils
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/common.py",

    # api
    "api/app.py",

    # configs
    "config/model.yaml",
    "config/schema.yaml",

    # root
    "main.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    ".gitignore",
    "README.md"
]

def create_files():
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
                pass
        else:
            print(f"file already exists: {filepath}")

if __name__ == "__main__":
    create_files()
    print("project structure created successfully")
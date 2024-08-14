import os
from pathlib import Path



list_of_files = [
    ".github/workflows/.gitkeep",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt"
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "toxi.ini",
    "experiment/experiments.ipynb"

    ]



for file in list_of_files:
    path = Path(file)
    file_dir, file_name = os.path.split(path)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        print(f"Creating directory {file_dir} for file {file_name}")

    if (not os.path.exists(path)) or (os.path. getsize(filepath)==0):
        with open(path, "w"):
            pass
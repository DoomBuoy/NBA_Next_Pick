from pathlib import Path
from loguru import logger
from tqdm import tqdm
import typer
import zipfile
import os
import subprocess
from nba_next_pick.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()

def fetch_kaggle_data():
    """
    Downloads and unzips the UTS-36120-25SP Kaggle competition data into RAW_DATA_DIR.
    """
    logger.info("Downloading dataset from Kaggle...")

    # Ensure the processed data directory exists
    os.makedirs(RAW_DATA_DIR, exist_ok=True)

    # Run Kaggle CLI command
    subprocess.run([
        "kaggle", "competitions", "download",
        "-c", "uts-36120-25-sp",
        "-p", str(RAW_DATA_DIR)
    ], check=True)

    logger.info("Unzipping files...")
    for file in os.listdir(RAW_DATA_DIR):
        if file.endswith(".zip"):
            zip_path = RAW_DATA_DIR / file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(RAW_DATA_DIR)
            os.remove(zip_path)

    logger.success(f"Data ready in {RAW_DATA_DIR}")

@app.command()
def main(
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = RAW_DATA_DIR / "dataset.csv",
):
    logger.info("Starting data pipeline...")
    fetch_kaggle_data()
    logger.info("Dataset downloaded and extracted.")

if __name__ == "__main__":
    app()

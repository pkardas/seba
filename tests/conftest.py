from pathlib import Path


def load_example(file_name: str) -> str:
    with open(Path(__file__).parent / "examples" / file_name) as file:
        return file.read()

import json
from pathlib import Path


def save_json(data, filename):

    output_dir = Path("raw_data/stripe")

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = output_dir / filename

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    return file_path
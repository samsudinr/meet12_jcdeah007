import pandas as pd
from pathlib import Path
import re

def extract_usernames_from_folder(folder_path):
    folder = Path(folder_path)
    csv_files = list(folder.glob("*.csv"))
    usernames = []

    pattern = re.compile(r'"userName":"([^"]+)"')

    for file in csv_files:
        df = pd.read_csv(file)
        if 'http.request.body.original' not in df.columns:
            continue
        for body in df['http.request.body.original']:
            if isinstance(body, str):
                match = pattern.search(body.replace('""', '"'))
                if match:
                    usernames.append(match.group(1))

    return pd.Series(usernames).drop_duplicates()

def save_csv(series, filepath, header=True):
    series.to_csv(filepath, index=False, header=header)

def save_txt(series, filepath):
    series.to_csv(filepath, index=False, header=False)

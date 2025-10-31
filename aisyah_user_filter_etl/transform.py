def filter_difference(series_a, series_b):
    return series_a[~series_a.isin(series_b)]

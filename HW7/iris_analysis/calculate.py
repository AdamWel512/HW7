import statistics
def calculate_statistics(data):
    """calculate statistics"""
    col = {}
    for row in data:
        for col_name, col_value in row.items():
            if col_name not in col:
                col[col_name] = []
            col[col_name].append(float(col_value))
    stats_result = {}
    for col, data in col.items():
        stats_result[col] = {
            "mean": round(statistics.mean(data), 3),
            'median': round(statistics.median(data),3),
            'std': round(statistics.stdev(data), 3)
    }
    return stats_result

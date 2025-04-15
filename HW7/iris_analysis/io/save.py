import csv

def save_stat(file_path, stats):
    """Save statistics dictionary to a CSV file."""
    with open(file_path, mode='w', newline='') as csvfile:
        fieldnames = ['column', 'mean', 'median', 'std']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for column, stats in stats.items():
            writer.writerow({
                'column': column,
                'mean': stats['mean'],
                'median': stats['median'],
                'std': stats['std']
            })
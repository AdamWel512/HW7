import argparse
from iris_analysis.io.load import load_data
from iris_analysis.io.save import save_stat
from iris_analysis.calculate import calculate_statistics

def main():
    parser = argparse.ArgumentParser(description='Calculate basic statistics for iris dataset.')
    parser.add_argument('input_path', type=str, help='Path to the input CSV file.')
    parser.add_argument('output_path', type=str, help='Path to save the result CSV file.')
    args = parser.parse_args()

    data = load_data(args.input_path)
    stats = calculate_statistics(data)
    save_stat(args.output_path, stats)

if __name__ == '__main__':
    main()
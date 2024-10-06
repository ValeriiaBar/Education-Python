import math
import pandas as pd

# CONSTANTS FOR FILE NAMES

INPUT_FILE_NAME = "quadratic_coefficients.csv"
OUTPUT_FILE_NAME = "roots_output.csv"

def read_coefficients_from_csv(file_path: str) -> pd.DataFrame:
    """
    Read coefficients from a CSV file and return a DataFrame.
    :param file_path: Path to the CSV file
    :return: DataFrame containing coefficients
    """
    return pd.read_csv(file_path)


def roots_of_equation(row: pd.Series) -> tuple:
    """
    Calculate the roots of a quadratic equation.
    :return: Tuple of two roots or strings indicating complex roots
    """
    a, b, c = row['a'], row['b'], row['c']
    d = b**2 - 4*a*c

    if d < 0:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-d) / (2 * a)
        return (f"{real_part} + {imaginary_part}i", f"{real_part} - {imaginary_part}i")

    x_1 = (-b + math.sqrt(d)) / (2 * a)
    x_2 = (-b - math.sqrt(d)) / (2 * a)
    return (x_1, x_2)

def create_roots_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate roots for each set of coefficients and create a DataFrame.
    :param DataFrame with coefficients
    :return: DataFrame with calculated roots
    """
    results = df.apply(roots_of_equation, axis = 1)
    return pd.DataFrame(results.tolist(), columns=['x_1', 'x_2'])

def save_dataframe_to_csv(df: pd.DataFrame, output_file_path: str) -> None:
    """
    Save the DataFrame to a CSV file.
    :param df: DataFrame to save
    :param output_file_path: Path to save the output CSV file
    """
    df.index.name = 'Index'
    df.to_csv(output_file_path)

def main():
    coefficients_df = read_coefficients_from_csv(INPUT_FILE_NAME)
    results_df = create_roots_dataframe(coefficients_df)
    save_dataframe_to_csv(results_df, OUTPUT_FILE_NAME)
if __name__ == '__main__':
    main()

import math
import pandas as pd

INPUT_FILE_NAME = "quadratic_coefficients.csv"
OUTPUT_FILE_NAME = "roots_output.csv"

def read_coefficients_from_csv(file_path: str) -> pd.DataFrame:
    """
    Read coefficients from a CSV file and return a DataFrame.
    :param file_path: Path to the CSV file
    :return: DataFrame containing coefficients
    """
    return pd.read_csv(file_path)

def extract_coefficients(df: pd.DataFrame) -> list[tuple[float, float, float]]:
    """
    Extract coefficients (a, b, c) from a DataFrame.
    :param df: DataFrame containing the coefficients
    :return: List of tuples containing coefficients
    """
    return [(row['a'], row['b'], row['c']) for index, row in df.iterrows()]

def roots_of_equation(coefficients: tuple[float]) -> tuple:
    """
    Calculate the roots of a quadratic equation.
    :param coefficients: Tuple of three floats (a, b, c)
    :return: Tuple of two roots or strings indicating complex roots
    """
    a, b, c = coefficients
    d = b**2 - 4*a*c

    if d < 0:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-d) / (2 * a)
        return (f"{real_part} + {imaginary_part}i", f"{real_part} - {imaginary_part}i")

    x_1 = (-b + math.sqrt(d)) / (2 * a)
    x_2 = (-b - math.sqrt(d)) / (2 * a)
    return (x_1, x_2)

def create_roots_dataframe(coefficients: list[tuple[float, float, float]]) -> pd.DataFrame:
    """
    Calculate roots for each set of coefficients and create a DataFrame.
    :param coefficients: List of tuples containing the coefficients
    :return: DataFrame with calculated roots
    """
    results = [roots_of_equation(coeff) for coeff in coefficients]
    return pd.DataFrame(results, columns=['x_1', 'x_2'])

def save_dataframe_to_csv(df: pd.DataFrame, output_file_path: str) -> None:
    """
    Save the DataFrame to a CSV file.
    :param df: DataFrame to save
    :param output_file_path: Path to save the output CSV file
    """
    df.index.name = 'Index'
    df.to_csv(output_file_path)

def main(file_path: str, output_file_path: str):
    coefficients_df = read_coefficients_from_csv(file_path)
    coefficients = extract_coefficients(coefficients_df)
    results_df = create_roots_dataframe(coefficients)
    save_dataframe_to_csv(results_df, output_file_path)

if __name__ == '__main__':
    main(input_file_name, output_file_name)
    

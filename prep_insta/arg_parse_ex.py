"""
ArgumentParser example
"""


import argparse


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="A simple command-line tool")

    # Add command-line arguments
    parser.add_argument("--input", help="Input file path")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values of the arguments
    input_file = args.input
    output_file = args.output
    verbose = args.verbose

    # Your script logic goes here
    if verbose:
        print(f"Input file: {input_file}")
        print(f"Output file: {output_file}")
        print("Verbose mode is enabled")


if __name__ == "__main__":
    main()

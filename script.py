# Get linear reference genome
import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(
        description="Use existing dataset files (filtered by extension)."
    )

    parser.add_argument(
        "--input_dir", type=str, required=True, help="Where to put the output copies."
    )
    parser.add_argument(
        "--output_dir", type=str, required=True, help="Where to put the output copies."
    )
    parser.add_argument("--name", type=str, required=True, help="Dataset name.")

    return parser.parse_args()


def main():
    args = parse_args()

    # This allows us to use the script for multiple modules
    if args.name == "linear":
        # Just touch the file for now.
        with open(os.path.join(args.output_dir, f"{args.name}.cram"), "w") as _:
            pass
    else:
        raise ValueError(args.name)


if __name__ == "__main__":
    main()

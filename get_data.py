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

    with open("/tmp/args", "w") as file:
        print(args, file=file)

    if args.name == "linear":
        os.symlink(args.input_dir, args.output_dir)
    else:
        raise ValueError(args.name)


if __name__ == "__main__":
    main()

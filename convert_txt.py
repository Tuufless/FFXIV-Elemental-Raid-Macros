import argparse
import os
from pathlib import Path

def convert_to_md(directory_path):
    for filename in os.listdir(directory_path):
        if Path(filename).suffix != ".txt":
            continue

        full_txt_path = Path(os.path.join(directory_path, filename))
        full_md_path = full_txt_path.with_suffix(".md")
        with open(full_txt_path, mode="r", encoding='utf-8') as txt, open(full_md_path, mode="w", encoding='utf-8') as md:
            md.write("```\n")
            for line in txt:
                md.write(line)
            md.write("\n```")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert .txt to .md")
    parser.add_argument("-i", "--input", required=True)

    args = parser.parse_args()

    convert_to_md(args.input)

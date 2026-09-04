import subprocess
import os
import sys
from datetime import date, timedelta


# 5x7 pixel font
FONT = {
    "A": [
        "01110",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "10001",
    ],

    "B": [
        "11110",
        "10001",
        "10001",
        "11110",
        "10001",
        "10001",
        "11110",
    ],

    "C": [
        "01111",
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "01111",
    ],

    "D": [
        "11110",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "11110",
    ],

    "E": [
        "11111",
        "10000",
        "10000",
        "11110",
        "10000",
        "10000",
        "11111",
    ],

    "F": [
        "11111",
        "10000",
        "10000",
        "11110",
        "10000",
        "10000",
        "10000",
    ],

    "G": [
        "01111",
        "10000",
        "10000",
        "10111",
        "10001",
        "10001",
        "01111",
    ],

    "H": [
        "10001",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "10001",
    ],

    "I": [
        "11111",
        "00100",
        "00100",
        "00100",
        "00100",
        "00100",
        "11111",
    ],

    "J": [
        "00111",
        "00010",
        "00010",
        "00010",
        "10010",
        "10010",
        "01100",
    ],

    "K": [
        "10001",
        "10010",
        "10100",
        "11000",
        "10100",
        "10010",
        "10001",
    ],

    "L": [
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "11111",
    ],

    "M": [
        "10001",
        "11011",
        "10101",
        "10101",
        "10001",
        "10001",
        "10001",
    ],

    "N": [
        "10001",
        "11001",
        "10101",
        "10011",
        "10001",
        "10001",
        "10001",
    ],

    "O": [
        "01110",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "01110",
    ],

    "P": [
        "11110",
        "10001",
        "10001",
        "11110",
        "10000",
        "10000",
        "10000",
    ],

    "Q": [
        "01110",
        "10001",
        "10001",
        "10001",
        "10101",
        "10010",
        "01101",
    ],

    "R": [
        "11110",
        "10001",
        "10001",
        "11110",
        "10100",
        "10010",
        "10001",
    ],

    "S": [
        "01111",
        "10000",
        "10000",
        "01110",
        "00001",
        "00001",
        "11110",
    ],

    "T": [
        "11111",
        "00100",
        "00100",
        "00100",
        "00100",
        "00100",
        "00100",
    ],

    "U": [
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "01110",
    ],

    "V": [
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "01010",
        "00100",
    ],

    "W": [
        "10001",
        "10001",
        "10001",
        "10101",
        "10101",
        "11011",
        "10001",
    ],

    "X": [
        "10001",
        "10001",
        "01010",
        "00100",
        "01010",
        "10001",
        "10001",
    ],

    "Y": [
        "10001",
        "10001",
        "01010",
        "00100",
        "00100",
        "00100",
        "00100",
    ],

    "Z": [
        "11111",
        "00001",
        "00010",
        "00100",
        "01000",
        "10000",
        "11111",
    ],

    " ": [
        "00000",
        "00000",
        "00000",
        "00000",
        "00000",
        "00000",
        "00000",
    ],
    "0": [
        "01110",
        "10001",
        "10011",
        "10101",
        "11001",
        "10001",
        "01110",
    ],

    "1": [
        "00100",
        "01100",
        "00100",
        "00100",
        "00100",
        "00100",
        "01110",
    ],

    "2": [
        "01110",
        "10001",
        "00001",
        "00010",
        "00100",
        "01000",
        "11111",
    ],

    "3": [
        "11110",
        "00001",
        "00001",
        "01110",
        "00001",
        "00001",
        "11110",
    ],

    "4": [
        "00010",
        "00110",
        "01010",
        "10010",
        "11111",
        "00010",
        "00010",
    ],

    "5": [
        "11111",
        "10000",
        "10000",
        "11110",
        "00001",
        "00001",
        "11110",
    ],

    "6": [
        "01110",
        "10000",
        "10000",
        "11110",
        "10001",
        "10001",
        "01110",
    ],

    "7": [
        "11111",
        "00001",
        "00010",
        "00100",
        "01000",
        "01000",
        "01000",
    ],

    "8": [
        "01110",
        "10001",
        "10001",
        "01110",
        "10001",
        "10001",
        "01110",
    ],

    "9": [
        "01110",
        "10001",
        "10001",
        "01111",
        "00001",
        "00001",
        "01110",
    ],

    "-": [
        "00000",
        "00000",
        "00000",
        "11111",
        "00000",
        "00000",
        "00000",
    ],

    " ": [
        "00000",
        "00000",
        "00000",
        "00000",
        "00000",
        "00000",
        "00000",
    ],
}


def render_text(text):
    """Convert text into a 7-row pixel-art matrix."""

    text = text.upper()

    result = [[] for _ in range(7)]

    for char in text:

        if char not in FONT:
            print(f"Skipping unsupported character: {char}")
            continue

        pattern = FONT[char]

        for row in range(7):
            result[row].extend(pattern[row])

        # one empty column between letters
        for row in range(7):
            result[row].append("0")

    return result


def print_art(art):
    print("\nGenerated art:\n")

    for row in art:
        print(
            "".join("██" if pixel == "1" else "  " for pixel in row)
        )

    print()


def git(command, env=None):
    subprocess.run(
        command,
        check=True,
        env=env
    )


def create_commits(art, start_date):

    start_date = date.fromisoformat(start_date)

    # Make sure we're starting on Sunday.
    # Python: Monday = 0 ... Sunday = 6
    if start_date.weekday() != 6:
        raise ValueError(
            "start_date must be a Sunday."
        )

    # Make sure the repository exists.
    if not os.path.isdir(".git"):
        raise RuntimeError(
            "Run this script inside a Git repository."
        )

    commit_count = 0

    for column, _ in enumerate(art[0]):

        for row in range(7):

            if art[row][column] != "1":
                continue

            commit_date = start_date + timedelta(
                weeks=column,
                days=row
            )

            timestamp = (
                commit_date.isoformat()
                + " 12:00:00"
            )

            env = os.environ.copy()

            env["GIT_AUTHOR_DATE"] = timestamp
            env["GIT_COMMITTER_DATE"] = timestamp

            # Change a file so every commit has actual content.
            with open("contribution-art.txt", "a") as f:
                f.write(
                    f"Contribution pixel: "
                    f"{commit_date.isoformat()}\n"
                )

            git(
                [
                    "git",
                    "add",
                    "contribution-art.txt"
                ],
                env
            )

            git(
                [
                    "git",
                    "commit",
                    "-m",
                    f"Pixel {commit_count + 1}"
                ],
                env
            )

            commit_count += 1

    print(
        f"Created {commit_count} commits."
    )


def main():

    if len(sys.argv) < 2:
        print(
            'Usage: python github_art.py "HELLO"'
        )
        sys.exit(1)

    text = sys.argv[1]

    # Change this to the Sunday where your drawing should begin.
    start_date = "2026-01-04"

    art = render_text(text)

    print_art(art)

    answer = input(
        "Create commits? [y/N]: "
    )

    if answer.lower() != "y":
        print("Cancelled.")
        return

    create_commits(
        art,
        start_date
    )


if __name__ == "__main__":
    main()
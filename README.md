# GitHub Contribution Art

Generate pixel-art text on your GitHub contribution graph using Git commits.

This Python utility converts text into a 7-row pixel-art pattern and creates dated Git commits corresponding to the filled pixels. Once pushed to GitHub, the commit history forms a visual pattern on your contribution graph.

> **Example:** `HELLO`, `1000-7`, `404`, `ROFL`, or any other supported characters.

## Features

* 🟩 Generate pixel-art text on the GitHub contribution graph
* 🔤 Built-in 5×7 pixel font
* 🔢 Support for uppercase letters, numbers, and `-`
* 📅 Control the starting date of the artwork
* 🖥️ Preview the generated artwork directly in the terminal
* 🎨 Adjustable commit intensity for darker contribution squares
* 🔒 Works entirely locally using Git
* 🐍 Written in pure Python using the standard library

## How It Works

GitHub's contribution graph is based on the number of contributions made on each day.

This project takes advantage of that system by mapping each pixel in a 7-row character matrix to a specific calendar date:

```text
Pixel → Calendar date → Git commit → GitHub contribution
```

For example, a character can be represented as:

```text
01110
10001
10001
11111
10001
10001
10001
```

Each `1` represents a contribution on a particular day, while each `0` represents an empty cell.

The result is a small piece of pixel art embedded directly into your contribution history.

## Installation

Clone the repository:

```bash
git clone git@github.com:Muivexee/gitabuse.git
cd gitabuse
```

No external Python packages are required.

Python 3.8+ is recommended.

## Usage

Run the generator with a text argument:

```bash
python github_art.py "GHOUL"
```

The program will display a preview before creating any commits:

```text
Generated art:

  ██████    ██████  ...
██      ██  ██      ██
██      ██  ██      ██
...
```

You will then be asked for confirmation:

```text
Create commits? [y/N]:
```

Enter:

```text
Y
```

to generate the Git history.

After the commits have been created, push them to GitHub:

```bash
git push
```

Your contribution graph should then begin reflecting the generated artwork.

## Commit Intensity

The contribution graph supports multiple levels of intensity depending on how many contributions occur on a given day.

The generator can create multiple commits for each filled pixel.

For example:

```python
create_commits(
    art,
    start_date,
    intensity=10
)
```

Higher values produce darker contribution squares.

A rough example:

```text
intensity = 1    → light
intensity = 5    → medium
intensity = 10   → dark
```

The exact appearance depends on GitHub's contribution display and account activity.

## Supported Characters

The current font supports:

### Letters

```text
A B C D E F G H I J K L M
N O P Q R S T U V W X Y Z
```

### Numbers

```text
0 1 2 3 4 5 6 7 8 9
```

### Symbols

```text
-
```

Spaces can also be used to separate words.

Unsupported characters are skipped automatically.

## Changing the Artwork

The text can be changed directly from the command line:

```bash
python github_art.py "HELLO"
```

Examples:

```bash
python github_art.py "HELLO"
python github_art.py "ROFL"
python github_art.py "1000-7"
python github_art.py "404"
python github_art.py "DEBUG"
```

## Important: Commit Dates

The artwork is generated using Git commit dates.

The starting date is configured in `main()`:

```python
start_date = "2026-01-04"
```

The date must be a **Sunday**, because GitHub's contribution graph is organized into seven-day columns.

Changing the starting date changes where the artwork appears on the contribution graph.

## GitHub Requirements

For contributions to appear on your GitHub profile, make sure:

1. The commits are associated with an email address connected to your GitHub account.
2. The repository is hosted on GitHub.
3. The commits are pushed to GitHub.
4. The repository and branch satisfy GitHub's contribution-display rules.

You can check your configured Git email with:

```bash
git config user.email
```

If necessary, configure it with:

```bash
git config user.email "your-email@example.com"
```

Use an email address associated with your GitHub account.

## Project Structure

```text
gitabuse/
│
├── github_art.py
├── contribution-art.txt
└── README.md
```

`github_art.py` contains the font, rendering logic, Git integration, and commit generation.

`contribution-art.txt` is modified for each generated commit so that every commit contains an actual repository change.

## Safety & Cleanup

This tool creates potentially large numbers of Git commits.

Before running it on an existing project, consider using a dedicated repository.

For example:

```text
gitabuse
```

is ideal for experimentation.

If you want to completely replace previously generated artwork, you can recreate the repository history and force-push the new history.

**Do not use this workflow on repositories containing important history unless you understand Git history rewriting.**

## Limitations

The current version intentionally keeps the implementation simple.

Currently supported:

* ASCII uppercase letters
* Numbers
* `-`
* 7-row pixel-art rendering
* Git commit generation
* Configurable commit intensity

Planned possibilities include:

* Unicode characters
* Japanese text
* Custom fonts
* PNG/JPG image conversion
* Pixel-art image generation
* Multiple colors/intensity levels
* More flexible artwork positioning

## Why?

Because GitHub contribution graphs are basically tiny calendars made of pixels.

Why not use them as one?

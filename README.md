# Bible

A Python program that opens up Bible verses that are asked.

## Description

This is a simple command-line program that allows you to look up and read Bible verses. The program includes a collection of popular Bible verses from the King James Version (KJV).

## Requirements

- Python 3.x

## Usage

### Command-line Mode

You can look up verses directly from the command line:

```bash
python3 bible.py "John 3:16"
python3 bible.py "Psalm 23:1"
python3 bible.py "Genesis 1:1"
```

To see all available verses:

```bash
python3 bible.py list
```

### Interactive Mode

Run the program without arguments to enter interactive mode:

```bash
python3 bible.py
```

Then type verse references when prompted:

```
Enter verse reference: John 3:16
Enter verse reference: Psalm 23:1
```

Type `list` to see all available verses, or `quit`/`exit` to exit the program.

## Available Verses

The program currently includes the following popular verses:

- John 3:16
- Genesis 1:1
- Psalm 23:1
- Proverbs 3:5-6
- Romans 8:28
- Philippians 4:13
- Matthew 6:33
- Jeremiah 29:11
- Isaiah 41:10
- 1 Corinthians 13:4-7

## Example Output

```
Bible Verse Lookup Program
----------------------------------------

John 3:16
=========

For God so loved the world, that he gave his only begotten Son, 
that whosoever believeth in him should not perish, but have 
everlasting life.

(King James Version (KJV))
```

## Making the Script Executable

You can make the script executable and run it directly:

```bash
chmod +x bible.py
./bible.py "John 3:16"
```

## Expanding the Database

To add more verses, edit the `BIBLE_DATA` dictionary in the `bible.py` file.
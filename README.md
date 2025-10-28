# Bible

A Python program that opens up Bible verses that are asked.

## Description

This is a simple command-line program that allows you to look up and read any Bible verse. The program uses the Bible API (bible-api.com) to fetch verses dynamically, supporting multiple translations including King James Version (KJV), NIV, ESV, and more.

## Requirements

- Python 3.8 or higher (Python 3.6 reached end-of-life in December 2021)
- Install Python packages: `pip3 install -r requirements.txt`

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

Type `help` or `list` to see usage examples, or `quit`/`exit` to exit the program.

## Supported Features

The program can fetch **any verse from the entire Bible**, including:

- All Old Testament books (Genesis through Malachi)
- All New Testament books (Matthew through Revelation)
- Single verses (e.g., "John 3:16")
- Verse ranges (e.g., "Psalm 23:1-6", "Matthew 5:3-12")
- Multiple Bible translations (KJV, NIV, ESV, NASB, NLT, and more)

### Translation Support

Specify a translation by adding it in parentheses:
```bash
python3 bible.py "John 3:16 (NIV)"
python3 bible.py "Genesis 1:1 (ESV)"
```

Default translation is King James Version (KJV) if not specified.

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

## API and Data Source

This program uses the [Bible API](https://bible-api.com) to fetch verses dynamically. The API provides access to the entire Bible in multiple translations. No local database is needed - all verses are fetched in real-time from the API.

## Contributing

Feel free to submit issues or pull requests to improve the program. When contributing, please follow the coding guidelines outlined in `.github/copilot-instructions.md`.
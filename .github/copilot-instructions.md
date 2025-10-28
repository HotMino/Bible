# GitHub Copilot Instructions for Bible Verse Lookup

This repository contains a Python-based Bible verse lookup program that uses the Bible API to fetch and display verses dynamically.

## Project Overview

- **Language**: Python 3
- **Purpose**: Command-line tool for looking up Bible verses
- **API**: Uses https://bible-api.com for verse retrieval
- **Translations**: Supports multiple Bible translations (KJV, NIV, ESV, etc.)

## Coding Style

### Python Style Guide
- Follow PEP 8 guidelines for Python code
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 79 characters for code, 72 for docstrings
- Use double quotes for strings consistently (already established in codebase)
- Use meaningful variable and function names

### Docstrings
- Use triple double-quotes (`"""`) for all docstrings
- Include docstrings for all functions, classes, and modules
- Follow Google-style docstring format:
  ```python
  def function_name(param1, param2):
      """
      Brief description of function.
      
      Args:
          param1 (type): Description of param1
          param2 (type): Description of param2
      
      Returns:
          type: Description of return value
      """
  ```

### Naming Conventions
- Functions and variables: `snake_case`
- Constants: `UPPER_CASE_WITH_UNDERSCORES`
- Classes: `PascalCase` (if added in the future)

## Project-Specific Conventions

### API Usage
- Always use the Bible API (https://bible-api.com) as the primary data source
- Handle network errors gracefully with user-friendly error messages
- Include timeout parameters for all API requests (default: 10 seconds)
- Support multiple Bible translations via URL parameters

### Error Handling
- Use try-except blocks for all external API calls
- Return error dictionaries with an 'error' key for consistent error handling
- Display user-friendly error messages (avoid technical jargon)
- Handle common exceptions:
  - `requests.exceptions.RequestException` for network errors
  - `json.JSONDecodeError` for API response parsing errors
  - `KeyboardInterrupt` and `EOFError` for graceful program termination

### User Input
- Accept Bible references in various formats (full names, common abbreviations)
- Normalize references using the `normalize_reference()` function
- Support verse ranges (e.g., "Psalm 23:1-6")
- Allow translation specification in parentheses (e.g., "John 3:16 (NIV)")

### Output Formatting
- Use clear section separators (`=` characters matching header length)
- Include verse reference, text, and translation information
- Maintain consistent spacing and formatting for readability

## Command-Line Interface

### Modes
- **Command-line mode**: Accept verse reference as command-line arguments
- **Interactive mode**: Enter interactive loop when no arguments provided
- **Help mode**: Display help with `--help`, `-h`, or `help` command

### Special Commands
- `help`, `list`, `-h`, `--help`: Show help information
- `quit`, `exit`, `q`: Exit the program

## Testing Considerations

When adding tests:
- Test both successful verse lookups and error conditions
- Mock external API calls to avoid network dependencies
- Test reference normalization with book name abbreviations (e.g., 'gen' -> 'Genesis')
- Test both command-line and interactive modes
- Verify error handling for network failures and invalid references

## Security Best Practices

- Never hardcode API keys or credentials (current API is public, but maintain this practice)
- Validate and sanitize user input to prevent injection attacks
- Use HTTPS for all API calls
- Handle timeouts to prevent hanging on slow connections
- Be cautious with external dependencies - keep them minimal

## Documentation

- Keep README.md up to date with usage examples and available features
- Document any new command-line options or features
- Include examples of supported Bible reference formats
- List available Bible translations

## Dependencies

- Use minimal external dependencies
- Current dependencies:
  - `requests`: For HTTP API calls (includes JSON parsing via `.json()` method)
  - `sys`, `re`: Standard library modules
- When adding new dependencies, justify their necessity and check for security vulnerabilities

## Compatibility

- Maintain Python 3.x compatibility
- Test with common Python 3 versions (3.6+)
- Maintain compatibility with currently supported Python 3 versions (3.8+)
- Python 3.6 reached end-of-life in December 2021
- Test with multiple Python 3 versions when possible
- Ensure cross-platform compatibility (Windows, macOS, Linux)
- Make the script executable with shebang: `#!/usr/bin/env python3`

## Code Organization

- Keep the single-file structure for simplicity
- Use clear function separation for different concerns:
  - API interaction functions
  - Display and formatting functions
  - Input parsing functions
  - Main program flow

## Future Enhancements to Consider

When adding new features, maintain simplicity and consider:
- Offline caching of frequently accessed verses (if it doesn't add significant complexity)
- Support for searching verses by keyword (if the API supports it)
- Simple text export of verses
Note: Avoid features that would significantly increase complexity or require many new dependencies

## Common Pitfalls to Avoid

- Don't break the simple command-line interface
- Don't add unnecessary complexity or dependencies
- Don't remove error handling for edge cases
- Don't change the API endpoint without good reason
- Don't sacrifice user-friendliness for technical features

## Setup and Build Instructions

### Initial Setup
1. Ensure Python 3.8+ is installed (Python 3.6 reached end-of-life in December 2021)
2. Install dependencies: `pip3 install -r requirements.txt`
3. Make script executable (optional): `chmod +x bible.py`

### Running the Program
- Command-line mode: `python3 bible.py "John 3:16"`
- Interactive mode: `python3 bible.py`
- Help: `python3 bible.py --help`

### Testing
- No test framework is currently set up
- When adding tests in the future, use `pytest` as it's a minimal and widely-used testing framework
- Tests should be placed in a `tests/` directory

## Repository Structure

```
Bible/
├── .github/
│   └── copilot-instructions.md  # This file
├── .gitignore                   # Python build artifacts
├── README.md                    # User documentation
├── requirements.txt             # Python dependencies
└── bible.py                     # Main program file
```

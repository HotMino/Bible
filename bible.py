#!/usr/bin/env python3
"""
Bible Verse Lookup Program
A program to look up and display any Bible verse from the Bible.
Uses the Bible API to fetch verses dynamically.
"""

import sys
import re
import requests

# Bible API configuration
BIBLE_API_BASE = "https://bible-api.com"
DEFAULT_TRANSLATION = "kjv"  # King James Version


def normalize_reference(reference):
    """
    Normalize a Bible verse reference for API lookup.
    
    Args:
        reference (str): The Bible verse reference
    
    Returns:
        str: Normalized reference for API
    """
    # Remove extra spaces and clean up
    reference = reference.strip()
    
    # Replace common abbreviations with full book names
    abbreviations = {
        'gen': 'Genesis', 'exo': 'Exodus', 'lev': 'Leviticus', 'num': 'Numbers', 'deu': 'Deuteronomy',
        'jos': 'Joshua', 'jdg': 'Judges', 'rut': 'Ruth', '1sa': '1 Samuel', '2sa': '2 Samuel',
        '1ki': '1 Kings', '2ki': '2 Kings', '1ch': '1 Chronicles', '2ch': '2 Chronicles',
        'ezr': 'Ezra', 'neh': 'Nehemiah', 'est': 'Esther', 'job': 'Job', 'psa': 'Psalms',
        'pro': 'Proverbs', 'ecc': 'Ecclesiastes', 'sng': 'Song of Solomon', 'isa': 'Isaiah',
        'jer': 'Jeremiah', 'lam': 'Lamentations', 'ezk': 'Ezekiel', 'dan': 'Daniel',
        'hos': 'Hosea', 'jol': 'Joel', 'amo': 'Amos', 'oba': 'Obadiah', 'jon': 'Jonah',
        'mic': 'Micah', 'nam': 'Nahum', 'hab': 'Habakkuk', 'zep': 'Zephaniah',
        'hag': 'Haggai', 'zec': 'Zechariah', 'mal': 'Malachi',
        'mat': 'Matthew', 'mar': 'Mark', 'luk': 'Luke', 'joh': 'John', 'act': 'Acts',
        'rom': 'Romans', '1co': '1 Corinthians', '2co': '2 Corinthians', 'gal': 'Galatians',
        'eph': 'Ephesians', 'phi': 'Philippians', 'col': 'Colossians', '1th': '1 Thessalonians',
        '2th': '2 Thessalonians', '1ti': '1 Timothy', '2ti': '2 Timothy', 'tit': 'Titus',
        'phm': 'Philemon', 'heb': 'Hebrews', 'jam': 'James', '1pe': '1 Peter',
        '2pe': '2 Peter', '1jo': '1 John', '2jo': '2 John', '3jo': '3 John',
        'jud': 'Jude', 'rev': 'Revelation'
    }
    
    # Check for abbreviations and replace them
    parts = reference.split()
    if parts and parts[0].lower() in abbreviations:
        parts[0] = abbreviations[parts[0].lower()]
        reference = ' '.join(parts)
    
    return reference


def fetch_verse(reference, translation=DEFAULT_TRANSLATION):
    """
    Fetch a Bible verse from the Bible API.
    
    Args:
        reference (str): The Bible verse reference (e.g., "John 3:16", "Genesis 1:1")
        translation (str): Bible translation to use (default: KJV)
    
    Returns:
        dict: The verse data or error information
    """
    try:
        # Normalize the reference
        normalized_ref = normalize_reference(reference)
        
        # Prepare the API URL
        # Replace spaces with + for URL encoding
        api_reference = normalized_ref.replace(' ', '+')
        url = f"{BIBLE_API_BASE}/{api_reference}"
        
        # Add translation parameter if not KJV
        if translation.lower() != 'kjv':
            url += f"?translation={translation}"
        
        # Make the API request
        response = requests.get(url, timeout=10)

        if not response.ok:
            try:
                error_payload = response.json()
            except ValueError:
                error_payload = {}

            message = error_payload.get(
                "error",
                error_payload.get(
                    "message",
                    "Bible API returned an unexpected error while looking up the verse.",
                ),
            )

            if not message and response.reason:
                message = f"{response.status_code} {response.reason}"
            elif not message:
                message = f"Bible API returned status code {response.status_code}."

            return {"error": message, "reference": normalized_ref}

        # Parse the JSON response
        data = response.json()
        
        # Extract verse information
        verse_text = data.get('text', '').strip()
        verse_reference = data.get('reference', normalized_ref)
        translation_name = data.get('translation_name', f'{translation.upper()}')
        
        if not verse_text:
            return {
                'error': 'No verse text found for the given reference.',
                'reference': normalized_ref
            }
        
        return {
            'reference': verse_reference,
            'text': verse_text,
            'translation_name': translation_name,
            'translation': translation
        }
        
    except requests.exceptions.RequestException as e:
        return {
            'error': f'Network error: Unable to fetch verse. Please check your internet connection.',
            'reference': normalized_ref
        }
    except (ValueError, requests.exceptions.JSONDecodeError):
        return {
            'error': 'Invalid response from Bible API. The verse reference may be invalid.',
            'reference': normalized_ref
        }
    except Exception as e:
        return {
            'error': f'Unexpected error: {str(e)}',
            'reference': normalized_ref
        }


def show_help():
    """
    Show help information for using the Bible verse lookup.
    """
    print("\nBible Verse Lookup Help")
    print("=" * 40)
    print("This program can fetch any Bible verse from the Bible!")
    print("\nUsage examples:")
    print("  - John 3:16")
    print("  - Genesis 1:1")
    print("  - Psalm 23:1-6")
    print("  - Matthew 5:3-12")
    print("  - Romans 8:28")
    print("  - 1 Corinthians 13:4-7")
    print("\nYou can also specify a translation:")
    print("  - John 3:16 (NIV)")
    print("  - Genesis 1:1 (ESV)")
    print("\nAvailable translations include: KJV, NIV, ESV, NASB, NLT, and more!")
    print("\nSpecial commands:")
    print("  - 'list' or 'help': Show this help")
    print("  - 'quit' or 'exit': Exit the program")
    print()


def display_verse(verse_data):
    """
    Display the verse information in a formatted way.
    
    Args:
        verse_data (dict): The verse data
    """
    if not verse_data:
        print("\nVerse not found.")
        print("Type 'help' for usage instructions.")
        return
    
    if 'error' in verse_data:
        print(f"\nError: {verse_data['error']}")
        print("Type 'help' for usage instructions.")
        return
    
    # Display the reference
    reference = verse_data.get('reference', 'Unknown Reference')
    print(f"\n{reference}")
    print("=" * len(reference))
    
    # Display the verse text
    text = verse_data.get('text', '').strip()
    print(f"\n{text}")
    
    # Display translation info
    translation = verse_data.get('translation_name', 'Unknown')
    print(f"\n({translation})")
    print()


def parse_reference_with_translation(input_text):
    """
    Parse input to extract reference and optional translation.
    
    Args:
        input_text (str): User input that may contain reference and translation
    
    Returns:
        tuple: (reference, translation)
    """
    # Check if translation is specified in parentheses
    if '(' in input_text and ')' in input_text:
        parts = input_text.split('(')
        reference = parts[0].strip()
        translation = parts[1].rstrip(')').strip().lower()
        return reference, translation
    
    return input_text.strip(), DEFAULT_TRANSLATION


def main():
    """
    Main function to run the Bible verse lookup program.
    """
    print("Bible Verse Lookup Program")
    print("=" * 40)
    print("Fetch any Bible verse from the entire Bible!")
    print()
    
    # Check if verse reference is provided as command-line argument
    if len(sys.argv) > 1:
        # Join all arguments to handle references with spaces
        reference = ' '.join(sys.argv[1:])
        
        # Check for special commands
        if reference.lower() in ['help', '--help', '-h']:
            show_help()
        else:
            ref, translation = parse_reference_with_translation(reference)
            verse_data = fetch_verse(ref, translation)
            display_verse(verse_data)
    else:
        # Interactive mode
        print("Enter Bible verse references (e.g., 'John 3:16', 'Psalm 23:1-6')")
        print("You can also specify translation: 'John 3:16 (NIV)'")
        print("Type 'help' for more information")
        print("Type 'quit' or 'exit' to exit the program.\n")
        
        while True:
            try:
                reference = input("Enter verse reference: ").strip()
                
                if reference.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break
                
                if reference.lower() in ['help', 'h']:
                    show_help()
                    continue
                
                if not reference:
                    continue
                
                ref, translation = parse_reference_with_translation(reference)
                verse_data = fetch_verse(ref, translation)
                display_verse(verse_data)
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break


if __name__ == "__main__":
    main()

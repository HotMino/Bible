#!/usr/bin/env python3
"""
Bible Verse Lookup Program
A simple program to look up and display Bible verses.
"""

import sys
import re

# Local Bible data (sample verses from King James Version)
BIBLE_DATA = {
    "John 3:16": "For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.",
    "Genesis 1:1": "In the beginning God created the heaven and the earth.",
    "Psalm 23:1": "The LORD is my shepherd; I shall not want.",
    "Proverbs 3:5-6": "Trust in the LORD with all thine heart; and lean not unto thine own understanding. In all thy ways acknowledge him, and he shall direct thy paths.",
    "Romans 8:28": "And we know that all things work together for good to them that love God, to them who are the called according to his purpose.",
    "Philippians 4:13": "I can do all things through Christ which strengtheneth me.",
    "Matthew 6:33": "But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you.",
    "Jeremiah 29:11": "For I know the thoughts that I think toward you, saith the LORD, thoughts of peace, and not of evil, to give you an expected end.",
    "Isaiah 41:10": "Fear thou not; for I am with thee: be not dismayed; for I am thy God: I will strengthen thee; yea, I will help thee; yea, I will uphold thee with the right hand of my righteousness.",
    "1 Corinthians 13:4-7": "Charity suffereth long, and is kind; charity envieth not; charity vaunteth not itself, is not puffed up, Doth not behave itself unseemly, seeketh not her own, is not easily provoked, thinketh no evil; Rejoiceth not in iniquity, but rejoiceth in the truth; Beareth all things, believeth all things, hopeth all things, endureth all things.",
}


def normalize_reference(reference):
    """
    Normalize a Bible verse reference for lookup.
    
    Args:
        reference (str): The Bible verse reference
    
    Returns:
        str: Normalized reference
    """
    # Remove extra spaces and capitalize properly
    parts = reference.strip().split()
    if len(parts) >= 2:
        # Capitalize first word (book name)
        parts[0] = parts[0].capitalize()
        # Join back together
        return ' '.join(parts)
    return reference.strip()


def fetch_verse(reference):
    """
    Fetch a Bible verse from the local database.
    
    Args:
        reference (str): The Bible verse reference (e.g., "John 3:16", "Genesis 1:1")
    
    Returns:
        dict: The verse data or None if not found
    """
    # Normalize the reference
    normalized_ref = normalize_reference(reference)
    
    # Try to find exact match
    if normalized_ref in BIBLE_DATA:
        return {
            'reference': normalized_ref,
            'text': BIBLE_DATA[normalized_ref],
            'translation_name': 'King James Version (KJV)'
        }
    
    # Try case-insensitive search
    for key in BIBLE_DATA:
        if key.lower() == normalized_ref.lower():
            return {
                'reference': key,
                'text': BIBLE_DATA[key],
                'translation_name': 'King James Version (KJV)'
            }
    
    return None


def list_available_verses():
    """
    List all available verses in the database.
    """
    print("\nAvailable verses:")
    print("-" * 40)
    for reference in sorted(BIBLE_DATA.keys()):
        print(f"  - {reference}")
    print()


def display_verse(verse_data):
    """
    Display the verse information in a formatted way.
    
    Args:
        verse_data (dict): The verse data
    """
    if not verse_data:
        print("\nVerse not found in database.")
        print("Type 'list' to see all available verses.")
        return
    
    if 'error' in verse_data:
        print(f"Error: {verse_data['error']}")
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
    translation_note = verse_data.get('translation_note', '')
    print(f"\n({translation})")
    if translation_note:
        print(f"Note: {translation_note}")
    print()


def main():
    """
    Main function to run the Bible verse lookup program.
    """
    print("Bible Verse Lookup Program")
    print("-" * 40)
    
    # Check if verse reference is provided as command-line argument
    if len(sys.argv) > 1:
        # Join all arguments to handle references with spaces
        reference = ' '.join(sys.argv[1:])
        
        # Check for special commands
        if reference.lower() in ['list', 'help', '--list', '--help', '-h']:
            list_available_verses()
        else:
            verse_data = fetch_verse(reference)
            display_verse(verse_data)
    else:
        # Interactive mode
        print("Enter Bible verse references (e.g., 'John 3:16', 'Psalm 23:1')")
        print("Type 'list' to see available verses")
        print("Type 'quit' or 'exit' to exit the program.\n")
        
        while True:
            try:
                reference = input("Enter verse reference: ").strip()
                
                if reference.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break
                
                if reference.lower() in ['list', 'help']:
                    list_available_verses()
                    continue
                
                if not reference:
                    continue
                
                verse_data = fetch_verse(reference)
                display_verse(verse_data)
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break


if __name__ == "__main__":
    main()

import os
import random
import string
from pathlib import Path


# Create a sample file for testing
def create_sample_file():
    """Create a sample text file for demonstration"""
    sample_content = """This is line 1 of the sample file.
This is line 2 with some random text.
Line 3 contains the word Python multiple times. Python is great!
Line 4: This is a longer line to demonstrate various file operations.
Line 5: Short line.
Line 6: Another line with some content.
Line 7: The quick brown fox jumps over the lazy dog.
Line 8: Python programming is fun and exciting.
Line 9: Learning file handling in Python.
Line 10: Last line of the sample file."""

    with open("sample.txt", "w") as file:
        file.write(sample_content)
    print("Sample file 'sample.txt' created successfully!\n")


# 1. Read an entire text file
def read_entire_file(filename):
    print("\n1. Read Entire File:")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None


# 2. Read first n lines of a file
def read_first_n_lines(filename, n):
    print(f"\n2. Read First {n} Lines:")
    try:
        with open(filename, 'r') as file:
            lines = []
            for i in range(n):
                line = file.readline()
                if not line:
                    break
                lines.append(line.strip())
                print(f"Line {i + 1}: {line.strip()}")
            return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return []


# 3. Append text to a file and display the text
def append_to_file(filename, text):
    print("\n3. Append Text to File:")
    try:
        with open(filename, 'a') as file:
            file.write(text + '\n')
        print(f"Successfully appended: '{text}'")

        # Display the appended text
        with open(filename, 'r') as file:
            content = file.read()
            print("\nUpdated file content:")
            print(content)
    except Exception as e:
        print(f"Error: {e}")


# 4. Read last n lines of a file
def read_last_n_lines(filename, n):
    print(f"\n4. Read Last {n} Lines:")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            last_n_lines = lines[-n:] if n <= len(lines) else lines
            for i, line in enumerate(last_n_lines, 1):
                print(f"Line {len(lines) - len(last_n_lines) + i}: {line.strip()}")
            return last_n_lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return []


# 5. Read file line by line and store it into a list
def file_to_list(filename):
    print("\n5. File to List:")
    try:
        with open(filename, 'r') as file:
            lines_list = [line.strip() for line in file]
        print(f"List created with {len(lines_list)} lines:")
        for i, line in enumerate(lines_list, 1):
            print(f"  {i}: {line}")
        return lines_list
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return []


# 6. Read file line by line store it into a variable
def file_to_variable(filename):
    print("\n6. File to Variable:")
    try:
        with open(filename, 'r') as file:
            file_variable = file.read()
        print(f"File content stored in variable (first 100 characters):")
        print(file_variable[:100] + "..." if len(file_variable) > 100 else file_variable)
        return file_variable
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return ""


# 7. Find the longest words
def find_longest_words(filename):
    print("\n7. Longest Words in File:")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            max_length = max(len(word) for word in words)
            longest_words = [word for word in words if len(word) == max_length]
            unique_longest = list(set(longest_words))

        print(f"Maximum word length: {max_length}")
        print(f"Longest word(s): {', '.join(unique_longest)}")
        return unique_longest
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return []


# 8. Count the number of lines in a text file
def count_lines(filename):
    print("\n8. Count Lines in File:")
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        print(f"Total number of lines: {line_count}")
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return 0


# 9. Count the frequency of words in a file
def count_word_frequency(filename):
    print("\n9. Word Frequency in File:")
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            # Remove punctuation
            translator = str.maketrans('', '', string.punctuation)
            clean_content = content.translate(translator)
            words = clean_content.split()

            word_freq = {}
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1

            # Sort by frequency (descending)
            sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

            print("Top 10 most frequent words:")
            for word, count in sorted_words[:10]:
                print(f"  '{word}': {count} time(s)")
            return word_freq
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return {}


# 10. Get the file size of a plain file
def get_file_size(filename):
    print("\n10. File Size:")
    try:
        size_bytes = os.path.getsize(filename)
        size_kb = size_bytes / 1024
        size_mb = size_kb / 1024

        print(f"File: {filename}")
        print(f"Size in bytes: {size_bytes} bytes")
        print(f"Size in KB: {size_kb:.2f} KB")
        print(f"Size in MB: {size_mb:.4f} MB")
        return size_bytes
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return 0


# 11. Write a list to a file
def write_list_to_file(filename, data_list):
    print("\n11. Write List to File:")
    try:
        with open(filename, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print(f"Successfully wrote {len(data_list)} items to '{filename}'")
        print(f"List content: {data_list}")

        # Verify by reading back
        with open(filename, 'r') as file:
            print("\nFile content:")
            print(file.read())
    except Exception as e:
        print(f"Error: {e}")


# 12. Copy the contents of a file to another file
def copy_file(source, destination):
    print(f"\n12. Copy File from '{source}' to '{destination}':")
    try:
        with open(source, 'r') as source_file:
            content = source_file.read()

        with open(destination, 'w') as dest_file:
            dest_file.write(content)

        print(f"Successfully copied '{source}' to '{destination}'")

        # Show destination file size
        dest_size = os.path.getsize(destination)
        print(f"Destination file size: {dest_size} bytes")
    except FileNotFoundError:
        print(f"Error: Source file '{source}' not found!")
    except Exception as e:
        print(f"Error: {e}")


# 13. Read a random line from a file
def read_random_line(filename):
    print("\n13. Read Random Line from File:")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        if lines:
            random_line = random.choice(lines)
            line_number = lines.index(random_line) + 1
            print(f"Random line (line {line_number}): {random_line.strip()}")
            return random_line.strip()
        else:
            print("File is empty!")
            return None
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None


# 14. Assess if a file is closed or not
def check_file_closed_status():
    print("\n14. Check if File is Closed:")
    try:
        # Method 1: Check after closing
        file1 = open("sample.txt", "r")
        print(f"File 'sample.txt' open status: {not file1.closed}")
        file1.close()
        print(f"After closing: File is closed? {file1.closed}")

        # Method 2: Using with statement (auto-closes)
        with open("sample.txt", "r") as file2:
            print(f"Inside 'with' block: File is closed? {file2.closed}")
        print(f"After 'with' block: File is closed? {file2.closed}")

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


# 15. Count number of words in a text file
def count_words(filename):
    print("\n15. Count Words in File:")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Remove punctuation and split
            translator = str.maketrans('', '', string.punctuation)
            clean_content = content.translate(translator)
            words = clean_content.split()
            word_count = len(words)

        print(f"Total number of words: {word_count}")
        print(f"Sample of first 20 words: {' '.join(words[:20])}...")
        return word_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return 0


# Bonus: Comprehensive file analyzer
def analyze_file(filename):
    print("\n" + "=" * 60)
    print("COMPREHENSIVE FILE ANALYSIS")
    print("=" * 60)

    try:
        with open(filename, 'r') as file:
            content = file.read()
            lines = content.splitlines()
            words = content.split()

            print(f"\nFile: {filename}")
            print(f"Total characters: {len(content)}")
            print(f"Total lines: {len(lines)}")
            print(f"Total words: {len(words)}")
            print(f"Total unique words: {len(set(words))}")

            # File size
            size_bytes = os.path.getsize(filename)
            print(f"File size: {size_bytes} bytes ({size_bytes / 1024:.2f} KB)")

            # Longest line
            longest_line = max(lines, key=len) if lines else ""
            print(f"Longest line length: {len(longest_line)} characters")

            # Most common word
            from collections import Counter
            word_counter = Counter(words)
            most_common = word_counter.most_common(1)
            if most_common:
                print(f"Most common word: '{most_common[0][0]}' ({most_common[0][1]} times)")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")


# Main function to demonstrate all programs
def main():
    # Create sample file
    create_sample_file()

    # Create additional files for testing
    with open("test_list.txt", "w") as f:
        f.write("Initial content\n")

    # Run all programs
    read_entire_file("sample.txt")
    read_first_n_lines("sample.txt", 5)
    append_to_file("sample.txt", "Line 11: This line was appended!")
    read_last_n_lines("sample.txt", 5)
    file_to_list("sample.txt")
    file_to_variable("sample.txt")
    find_longest_words("sample.txt")
    count_lines("sample.txt")
    count_word_frequency("sample.txt")
    get_file_size("sample.txt")

    # Write list to file
    sample_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    write_list_to_file("fruits.txt", sample_list)

    # Copy file
    copy_file("sample.txt", "sample_copy.txt")

    # Read random line
    read_random_line("sample.txt")

    # Check file closed status
    check_file_closed_status()

    # Count words
    count_words("sample.txt")

    # Comprehensive analysis
    analyze_file("sample.txt")

    # Clean up: remove test files (optional)
    print("\n" + "=" * 60)
    print("Test files created:")
    print("- sample.txt")
    print("- sample_copy.txt")
    print("- fruits.txt")
    print("- test_list.txt")
    print("\nYou can keep these files for reference or delete them.")


# Alternative: Simple standalone functions for each requirement
def simple_program_1():
    """Read entire text file"""
    with open("sample.txt", "r") as f:
        return f.read()


def simple_program_2(n):
    """Read first n lines"""
    with open("sample.txt", "r") as f:
        return [next(f).strip() for _ in range(n)]


def simple_program_3(text):
    """Append text to file"""
    with open("sample.txt", "a") as f:
        f.write(text + "\n")


def simple_program_4(n):
    """Read last n lines"""
    with open("sample.txt", "r") as f:
        lines = f.readlines()
        return lines[-n:]


def simple_program_5():
    """File to list"""
    with open("sample.txt", "r") as f:
        return f.readlines()


def simple_program_6():
    """File to variable"""
    with open("sample.txt", "r") as f:
        return f.read()


def simple_program_7():
    """Find longest words"""
    with open("sample.txt", "r") as f:
        words = f.read().split()
        max_len = max(len(w) for w in words)
        return [w for w in words if len(w) == max_len]


def simple_program_8():
    """Count lines"""
    with open("sample.txt", "r") as f:
        return sum(1 for _ in f)


def simple_program_9():
    """Word frequency"""
    from collections import Counter
    with open("sample.txt", "r") as f:
        words = f.read().split()
        return Counter(words)


def simple_program_10():
    """Get file size"""
    return os.path.getsize("sample.txt")


def simple_program_11(lst, filename="output.txt"):
    """Write list to file"""
    with open(filename, "w") as f:
        f.write("\n".join(map(str, lst)))


def simple_program_12(src, dst):
    """Copy file"""
    with open(src, "r") as f1, open(dst, "w") as f2:
        f2.write(f1.read())


def simple_program_13(filename):
    """Read random line"""
    with open(filename, "r") as f:
        lines = f.readlines()
        return random.choice(lines) if lines else None


def simple_program_14(filename):
    """Check if file is closed"""
    f = open(filename, "r")
    status1 = f.closed
    f.close()
    status2 = f.closed
    return status1, status2


def simple_program_15(filename):
    """Count words"""
    with open(filename, "r") as f:
        return len(f.read().split())


if __name__ == "__main__":
    main()
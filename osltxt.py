import hashlib
import sys
import os

def create_file(filename, author, license_type, text_content):
    hash_object = hashlib.sha256(text_content.encode('utf-8'))
    file_hash = hash_object.hexdigest()

    file_data = f"""# OSLTXT v1.0
# License: {license_type}
# Author: {author}
----------------------------------------
{text_content}
----------------------------------------
# HASH: {file_hash}
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(file_data)
    print(f"Successfully created file: {filename}")

def verify_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "# HASH:" not in content:
        print("ERROR: Invalid file structure (missing hash).")
        return

    text_part, hash_part = content.split("# HASH:")
    saved_hash = hash_part.strip()

    parts = text_part.split("----------------------------------------")
    if len(parts) < 3:
        print("ERROR: Could not detect the note body.")
        return
    
    clean_body = parts[1].strip()
    calculated_hash = hashlib.sha256(clean_body.encode('utf-8')).hexdigest()

    print(f"Checking file: {filepath}")
    if calculated_hash == saved_hash:
        print("[OK] File is valid. No unauthorized modifications detected!")
    else:
        print("[WARNING] File has been MODIFIED! Hash does not match.")

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "verify":
        verify_file(sys.argv[2])
    elif len(sys.argv) > 1 and sys.argv[1] == "new":
        filename = input("File name (e.g., note.osltxt): ")
        author = input("Author: ")
        license_type = input("License (e.g., MIT): ")
        print("Enter the note text (type 'end' on a new line when finished):")
        lines = []
        while True:
            line = input()
            line_str = str(line)
            if line_str == "end":
                break
            lines.append(line_str)
        text_content = "\n".join(lines)
        create_file(filename, author, license_type, text_content)
    else:
        print("Usage:")
        print("  Create new:  python osltxt.py new")
        print("  Verify file: python osltxt.py verify filename.osltxt")
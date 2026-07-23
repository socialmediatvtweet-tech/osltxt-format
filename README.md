OSLTXT (Open Source Licensed Text)
==================================

.osltxt is a minimalist, plain-text file format designed for sharing notes, ideas, and text documents with clear open-source licensing and cryptographic integrity protection.

Features
--------

*   **100% Plain Text:** Readable in any text editor (Notepad, VS Code, terminal) across any operating system.
    
*   **Explicit Licensing:** Every file contains its open-source license right in the header (e.g., MIT, CC-BY).
    
*   **Integrity Check (SHA-256):** A cryptographic hash is attached at the end of the file. If anyone alters a single character of the original text, the verification script will instantly catch it.
    

File Structure Example
----------------------

`# OSLTXT v1.0 # License: MIT  # Author: Jakub Fríbl  ----------------------------------------  This is the genesis file of the OSLTXT format.  A minimalist plain-text standard designed for open sharing,  transparency, and cryptographic integrity.  Let the history of open-source text begin here.  ----------------------------------------  # HASH:` 

How to Use & Requirements
-------------------------

To work with .osltxt files and verify their integrity, you need **Python** installed on your computer along with the official companion script (osltxt.py).

### Step 1: Install Python

1.  Go to [python.org](https://www.python.org/) and download the installer for your system.
    
2.  **Important:** During installation, make sure to check the box **"Add Python to PATH"**.
    

### Step 2: Get the Files

Download both the osltxt.py script and your .osltxt files (like genesis.osltxt) into the same folder on your computer.

### Step 3: Commands

Open your terminal or command prompt (cmd) in that folder and use the following commands:

*   Bashpython osltxt.py new_(Follow the prompts, write your text, and type end on a new line when you are finished)._
    
*   Bashpython osltxt.py verify genesis.osltxt_(The script will check if the text has been modified or if it matches the original cryptographic hash)._

Or You can just install Python and our .exe file.
    

License
-------

This specification and the companion script are open-source under the MIT License. Feel free to use and adapt .osltxt for your own projects.

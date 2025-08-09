# **Text Line Merger**

A simple and efficient Python script to read a multi-line text file and merge all its contents into a single line. Each original line is separated by a space in the final output.

This is useful for cleaning up text data, preparing text for natural language processing (NLP) models, or simply formatting text into a continuous block.

## **Features**

* **Reads any .txt file**: Processes standard text files.  
* **Merges all lines**: Concatenates every line into one.  
* **Smart Spacing**: Adds a single space between the content of each former line.  
* **Cleans up empty lines**: Automatically removes blank lines and leading/trailing whitespace.  
* **UTF-8 Support**: Handles a wide range of characters and languages.

## **How to Use**

### **Prerequisites**

* You need to have [Python 3](https://www.python.org/downloads/) installed on your system.

### **Steps**

1. **Clone the Repository**  
   git clone https://github.com/YOUR\_USERNAME/YOUR\_REPOSITORY\_NAME.git  
   cd YOUR\_REPOSITORY\_NAME

2. **Prepare Your Input File**  
   * Place the text file you want to process (e.g., transkrip.txt) in the same directory as the proses\_teks.py script.  
   * Your input file can look like this:

\[Oke, apakah sudah ready?  
\>\> Oke, ready yuk, let's go.  
\>\> Oke, sip. Jadi, kita langsung saja ke  
inti dari pembahasannya pada malam hari  
ini.

3. **Run the Script**  
   * Open your terminal or command prompt and run the script:

   python proses\_teks.py

   * The script will automatically use transkrip.txt as the input and create hasil.txt as the output.  
4. **Check the Output**  
   * A new file named hasil.txt will be created in the same directory. Its content will be a single line of text.

\[Oke, apakah sudah ready? \>\> Oke, ready yuk, let's go. \>\> Oke, sip. Jadi, kita langsung saja ke inti dari pembahasannya pada malam hari ini.

## **Customization**

You can easily change the input and output filenames by editing the last section of the proses\_teks.py script:

\# \--- Cara Penggunaan \---  
if \_\_name\_\_ \== "\_\_main\_\_":  
    \# Change this to your input file's name  
    file\_input \= "nama\_file\_anda.txt"

    \# Change this to your desired output file's name  
    file\_output \= "output\_kustom.txt"

    \# Run the function  
    gabungkan\_baris(file\_input, file\_output)

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

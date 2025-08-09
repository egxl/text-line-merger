# **Text Line Merger**

A simple and efficient Python script that reads a multi-line text file and merges all of its contents into a single line. Each original line is separated by a space in the final output.

This is useful for cleaning up text data, preparing text for natural language processing (NLP) models, or formatting text into a continuous block.

## **Features**

* **Reads any .txt file**: Processes standard text files.
* **Merges all lines**: Concatenates every line into one.
* **Smart Spacing**: Adds a single space between the content of each former line.
* **Cleans up empty lines**: Automatically removes blank lines and leading/trailing whitespace.
* **UTF-8 Support**: Handles a wide range of characters and languages.
* **Interactive dialogs**: Uses Tkinter to select input and output files.

## **How to Use**

### **Prerequisites**

* You need to have [Python 3](https://www.python.org/downloads/) installed on your system.

### **Steps**

1. **Clone the Repository**
   ```
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
   cd YOUR_REPOSITORY_NAME
   ```

2. **Run the Script**
   ```
   python text-line-merger.py
   ```
   * A dialog will appear asking you to select the input `.txt` file.
   * After choosing the input, another dialog will ask where to save the merged output.

3. **Check the Output**
   * The selected output file will contain the entire text merged into a single line.

## **Customization**

The merging logic is contained in the `merge_lines` function within `text-line-merger.py`. You can reuse or modify this function in your own scripts if you prefer to bypass the dialogs or integrate the logic elsewhere.

## **License**

This project is licensed under the MIT License.

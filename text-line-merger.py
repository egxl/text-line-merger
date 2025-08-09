import tkinter as tk
from tkinter import filedialog


def merge_lines(input_file_path, output_file_path):
    """
    Read a text file, merge all lines into a single space-separated line, and
    write it to an output file.

    Example:
        Input file (``input.txt``)::
            Lorem ipsum dolor sit amet,
            consectetur adipiscing elit.
            Sed do eiusmod tempor.

        Output file (``output.txt``)::
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor.

    Args:
        input_file_path (str): Path to the input (.txt) file.
        output_file_path (str): Path to save the output file.
    """

    try:
        # Open and read the input file
        with open(input_file_path, "r", encoding="utf-8") as file_input:
            # Read all lines into a list
            lines = file_input.readlines()

            # Strip leading/trailing whitespace and remove empty lines
            clean_lines = [line.strip() for line in lines if line.strip()]

            # Join all lines into one space-separated string
            single_line = " ".join(clean_lines)

        # Write the result to the output file
        with open(output_file_path, "w", encoding="utf-8") as file_output:
            file_output.write(single_line)

        print(
            f"✅ Success! File '{input_file_path}' has been processed and saved as '{output_file_path}'."
        )

    except FileNotFoundError:
        print(f"❌ Failed: Input file '{input_file_path}' not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


# --- Usage ---
if __name__ == "__main__":
    # Create the root window for Tkinter
    root = tk.Tk()
    root.withdraw()  # Hide the main window because we only need the dialogs

    # 1. Open a dialog to choose the input file
    print("Please select the input (.txt) file to process...")
    file_input = filedialog.askopenfilename(
        title="Select input file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
    )

    # 2. If the user selected a file, continue to choose the output location
    if file_input:
        print(f"Input file selected: {file_input}")
        print("Now choose where to save the result...")

        # Open a dialog to save the output file
        file_output = filedialog.asksaveasfilename(
            title="Save file as...",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )

        # 3. If the user specifies a save location, run the main function
        if file_output:
            print(f"The output file will be saved to: {file_output}")
            merge_lines(file_input, file_output)
        else:
            print("❌ Process canceled: No save location selected.")
    else:
        print("❌ Process canceled: No input file selected.")

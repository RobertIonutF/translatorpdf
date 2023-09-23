import sys
import os
from pdfreader import SimplePDFViewer, PageDoesNotExist
from fpdf import FPDF
from translate import Translator

def translate_text(text, source_language="en", target_language="es"):
    """Translate text using the 'translate' library."""
    translator = Translator(from_lang=source_language, to_lang=target_language)
    return translator.translate(text)

def translate_pdf(file_name, source_language, target_language):
    input_path = os.path.join("input", file_name)
    output_path = os.path.join("output", "translated_" + file_name)

    with open(input_path, "rb") as fd:
        viewer = SimplePDFViewer(fd)
        pdf_writer = FPDF()

        # Loop through each page
        while True:
            try:
                print(f"Translating page {viewer.current_page_number + 1}")
                viewer.navigate(viewer.current_page_number + 1)
                viewer.render()
                text = "".join(viewer.canvas.strings)
                translated_text = translate_text(text, source_language, target_language)

                # Create a new page with translated text
                pdf_writer.add_page()
                pdf_writer.set_font("Arial", size=12)
                pdf_writer.multi_cell(0, 10, translated_text)

            except PageDoesNotExist:
                break

        # Save the translated PDF
        pdf_writer.output(output_path)

def list_files():
    files = os.listdir("input")
    for idx, file_name in enumerate(files, 1):
        print(f"{idx}. {file_name}")

def display_help():
    help_text = """
Usage: python translatepdf.py [file_index] [source_language] [target_language]
       python translatepdf.py --list
       python translatepdf.py --help

Commands:
  file_index         : Index of the file in the input folder to translate.
  source_language    : Language code of the source text (e.g., 'en' for English).
  target_language    : Language code of the target translation (e.g., 'ro' for Romanian).
  --list             : List all files in the input folder with their indices.
  --help             : Display this help message.
    """
    print(help_text)

if __name__ == "__main__":
    if "--help" in sys.argv:
        display_help()
    elif "--list" in sys.argv:
        list_files()
    elif len(sys.argv) == 4:
        try:
            files = os.listdir("input")
            file_index = int(sys.argv[1]) - 1
            source_language = sys.argv[2]
            target_language = sys.argv[3]
            translate_pdf(files[file_index], source_language, target_language)
        except (IndexError, ValueError):
            print("Invalid file index. Use --list to see available files.")
    else:
        print("Invalid command. Use --help for usage information.")
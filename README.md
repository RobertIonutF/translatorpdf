
# translatepdf

Translate the contents of a PDF file from one language to another using the `translate` library.

## Installation

### Step 1: Clone the Repository

If the script is part of a repository, you can clone it using:

```
git clone [repository_url]
cd [repository_directory]
```

### Step 2: Install Dependencies

Install the required Python libraries using `pip`:

```
pip install pdfreader fpdf translate
```

### Step 3: Set Up Folders

Ensure you have two folders in the same directory as the script:

- `input`: Place your PDF files here that you want to translate.
- `output`: Translated PDFs will be saved here.

## Usage

### Step 1: List Available Files

To see a list of files available for translation in the `input` folder:

```
python translatepdf.py --list
```

### Step 2: Translate a File

To translate a specific file, use the following command format:

```
python translatepdf.py [file_index] [source_language] [target_language]
```

For example, to translate the first file from English (`en`) to Romanian (`ro`):

```
python translatepdf.py 1 en ro
```

The translated file will be saved in the `output` folder with a `translated_` prefix.

### Step 3: Get Help

For additional information on how to use the script:

```
python translatepdf.py --help
```

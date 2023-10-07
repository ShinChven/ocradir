# ocradir

`ocradir` is a CLI tool that performs Optical Character Recognition (OCR) on all images in a directory and saves the results to `.md` files.

## Prerequisites

### macOS:

1. **Tesseract**:
   Install Tesseract using Homebrew:
   ```bash
   brew install tesseract
   ```

   **Optional**:
   If you wish to add language support, such as for Chinese Simplified and Traditional, you can do the following:
   ```bash
   brew install tesseract-lang
   ```

2. **Python**:
   Ensure you have a recent version of Python 3 installed. If not, install it using Homebrew:
   ```bash
   brew install python
   ```

### Windows:

1. **Tesseract**:
   - Download the Tesseract installer from the [GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki).
   - Install Tesseract using the installer.
   - Add Tesseract's installation directory to your system's PATH.

   **Optional**:
   - If you wish to add specific language support, visit the [Tesseract GitHub releases](https://github.com/tesseract-ocr/tessdata) to download language data files.
   - As an example, for Chinese Simplified, you can download `chi_sim.traineddata` and for Chinese Traditional, download `chi_tra.traineddata`.
   - Place the downloaded `.traineddata` files into the `tessdata` directory of your Tesseract installation.

2. **Python**:
   - Download the installer from the [official Python website](https://www.python.org/downloads/windows/).
   - Install Python and ensure the "Add to PATH" option is selected during installation.

### Linux (Ubuntu/Debian):

1. **Tesseract**:
   Install Tesseract:
   ```bash
   sudo apt-get update
   sudo apt-get install tesseract-ocr
   ```

   **Optional**:
   For those who wish to add specific language support, such as Chinese Simplified and Traditional, you can do:
   ```bash
   sudo apt-get install tesseract-ocr-chi-sim tesseract-ocr-chi-tra
   ```

2. **Python**:
   Python 3 is usually pre-installed on most Linux distributions. If not, you can install it using:
   ```bash
   sudo apt-get install python3
   ```

## Installation

### From GitHub:

```bash
pip install git+https://github.com/ShinChven/ocradir.git
```

### From Source:

1. Clone the repository:

   ```bash
   git clone https://github.com/ShinChven/ocradir.git
   ```

2. Navigate to the cloned directory:

   ```bash
   cd ocradir
   ```

3. Install using `pip`:

   ```bash
   pip install .
   ```

## Usage

To perform OCR on all images in a directory:

```bash
ocradir /path/to/your/image/directory -l chi_sim
```

- Replace `/path/to/your/image/directory` with the path to the directory containing your images.
- Use `-l chi_sim` for Simplified Chinese (or any other Tesseract supported language code). 

## Uninstallation

To uninstall `ocradir`:

```bash
pip uninstall ocradir
```

## Support

If you encounter any issues or have questions, please open an issue on GitHub.


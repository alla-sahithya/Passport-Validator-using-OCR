# NOLA_AI_Internship
This is an Internship programming challenge.

# Overview:
This project uses the free version of the Mindee API for OCR (Optical Character Recognition) extraction. Once the text is extracted, the project determines if the license is valid or not.

## Features:

- **OCR Extraction:** Uses Mindee API to extract text from images.
- **License Validation:** Analyzes extracted text to determine license validity.

## Installation/ Usage:

1. **Clone the repository:** git clone https://github.com/anvs18/NOLA_AI_Internship.git
2. Navigate into the 'NOLA_AI_Internship' folder.
3. (optional) **Create a virtual environment:** python -m venv venv
   and **Activate it:** ./venv/Scripts/activate
4. **Install the required packages:** pip install -r requirements.txt
5. **Modify** the configs/config.json file according to your input needs and your API key.
6. **Run the program:** python src/main.py

## References:
https://developers.mindee.com/docs/us-driver-license-ocr

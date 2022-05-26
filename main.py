import PyPDF2
import re


def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfFileReader(pdf, strict=False)
        # no_pages = len(reader.pages)
        pdf_text = []

        for page in reader.pages:
            text = page.extract_text()

            pdf_text.append(text)

        return pdf_text


def main():
    extracted_text = extract_text_from_pdf('sample.pdf')
    for t in extracted_text:
        # split_message = re.split(r'\s+|[,;?!.-]\s*', t.lower())
        print(t)


if __name__ == '__main__':
    main()
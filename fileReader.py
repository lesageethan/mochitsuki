import PyPDF2

class FileReader():
    def __init__(self, filename):
        self.filename = filename
        self.pdf_contents = self.read_pdf(filename)
    
    @staticmethod
    def read_pdf(filename):
        pdf_file_object = open(filename, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file_object)
        output = ""
        for i in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[i]
            output += page.extract_text()
        return output

if __name__ == "__main__":
    f = FileReader("Cambridge IGCSE Textbook.pdf")
    print(f.filename)
    print(f.pdf_contents)
    print(len(f.pdf_contents))
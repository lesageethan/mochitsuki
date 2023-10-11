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
        for i in range(3): #len(pdf_reader.pages)
            page = pdf_reader.pages[i]
            output += page.extract_text()
        return output
    
    @property
    def contents_list(self):
        n = 1000
        return [self.pdf_contents[i:i+n] for i in range(0, len(self.pdf_contents), n)]

if __name__ == "__main__":
    f = FileReader("test_textbook.pdf")
    print(f.filename)
    #print(f.pdf_contents)
    print(len(f.pdf_contents))
    print(len(f.contents_list))
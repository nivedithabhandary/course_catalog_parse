from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re

'''class page_info():
    def __init__(self, course_id, course_name, course_description, prerequisite, corequisite, grade_rule, unit):
        self.course_id = None
        self.course_name = None
        self.course_description = None
        self.prerequisite = None
        self.corequisite = None
        self.grade_rule = None
        self.unit = None

    def add_course_details(course_info):
'''
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

# List all course IDs
page = convert('catalog-2016-2017.pdf',[1028])
start = re.findall(r'(\A[A-Z]+\s[0-9]+\.)\s([A-Za-z\t .]+)', page)
with_char = re.findall(r'(\n[A-Z]+\s[0-9]+[A-Z]\.)\s([A-Za-z\t .]+)',page)
without_char = re.findall(r'(\n[A-Z]+\s[0-9]+\.)\s([A-Za-z\t .]+)',page)
course_id = []
course_id.extend(start)
course_id.extend(with_char)
course_id.extend(without_char)

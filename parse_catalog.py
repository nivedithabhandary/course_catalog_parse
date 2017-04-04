import PyPDF2
import MySQLdb

# MySQL details
hostname = ''
username = 'admin'
password = 'password'
database = 'courseCatalog'

# Read decrypted pdf file
def readPDF(file_name):
    pdfFileObj = open(file_name,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print pdfReader.getNumPages()

    #import textract
    #text = textract.process("catalog-2016-2017.pdf")


# Setup connection with MySQL DB
def dbSetup():
    conn = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    cursor = conn.cursor()
    cursor.execute("select * from course_details;")
    print cursor.fetchall()


#
readPDF("test.pdf")
readPDF("catalog-2016-2017.pdf")
dbSetup()

If the pdf file is encrypted use the following to decrypt before reading the pdf:

Type the following command to install the qpdf:
$ sudo apt-get install qpdf

Decrypt a PDF called input.pdf with YOURPASSWORD-HERE password and create unencrypted output.pdf, enter:

qpdf --password=YOURPASSWORD-HERE --decrypt input.pdf output.pdf

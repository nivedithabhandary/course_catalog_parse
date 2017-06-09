If the pdf file is encrypted use the following to decrypt before reading the pdf:

Type the following command to install the qpdf:
$ sudo apt-get install qpdf

Decrypt a PDF called input.pdf with YOURPASSWORD-HERE password and create unencrypted output.pdf, enter:

qpdf --password=YOURPASSWORD-HERE --decrypt input.pdf output.pdf



Database setup:

> mysql -u root -p

> CREATE DATABASE edm;
> use edm;

> CREATE TABLE catalog_info (course_number varchar(20), course_title varchar(100), course_description varchar(2048), prerequisites varchar(1028), units int, year int, semester varchar(20), department varchar(50));

> CREATE TABLE syllabus_info (course_number varchar(20), course_title varchar(100), course_description varchar(2048), prerequisites varchar(2048), units int, year int, semester varchar(20), department varchar(50), course_learning_objectives varchar(2048), reference_material varchar(2048), topics varchar(1024), tutor varchar(100), keywords varchar(512));


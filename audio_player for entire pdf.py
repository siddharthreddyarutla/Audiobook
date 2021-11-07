import pyttsx3
import PyPDF2
# open the pdf which you want to play with 'open'
book = open('python_tutorial.pdf', 'rb')
# initialize variable as pdfReader and use the pypdf2 package to read the pdf
pdfReader = PyPDF2.PdfFileReader(book)
# initialize a variable called pages and read the number of pages does the pdf has
pages = pdfReader.numPages

for i in range(14,pages):
    audio_player = pyttsx3.init()
    page_to_read = pdfReader.getPage(14)
    text = page_to_read.extractText()
    audio_player.say(text)
    audio_player.runAndWait()
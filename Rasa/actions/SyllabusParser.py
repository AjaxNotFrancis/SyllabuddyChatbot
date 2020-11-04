from bs4 import BeautifulSoup
import re

# Syllabi Path Variables (for easy switching)
chem123 = "Syllabi/CHEM123.html"
hca540 = "Syllabi/HCA540.html"
template = "Syllabi/TEMP.html"

# Open file and generate soup
#with open(chem123, encoding='utf8') as fp:
   # soup = BeautifulSoup(fp, 'html.parser')


# Some random test inputs
testInput1 = "Who is the course Instructor?"
testInput2 = "What time is the class?"
testInput3 = "What is the textbook?"
testInput4 = "Can you give me the zoom link"


# Function to remove punctuation from a given input and return the processed string
def remove_punc(aString):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for ele in aString:
        if ele in punc:
            aString = aString.replace(ele, "")
    return aString


# syntax to find something based on keyword
# result = soup.find_all(string=re.compile(f'{queryList}'))


# find specific item
#print(soup.find(string=re.compile("Instructor")))
#print((soup.find(string=re.compile("Zoom"))).find_next('a').string)
#print(soup.find(string=re.compile("Email")).find_next('a').string)


def find_instructor(course):
    with open("actions/" + course + ".html", encoding='utf8') as syllabus:
        rasaSoup = BeautifulSoup(syllabus, 'html.parser')

    if rasaSoup.find(string=re.compile("Instructor")) is None:
        return "No instructor found"
    else:
        return rasaSoup.find(string=re.compile("Instructor"))


def find_zoom(course):
    with open("Rasa/actions/Syllabi/" + course, encoding='utf8') as syllabus:
        rasaSoup = BeautifulSoup(syllabus, 'html.parser')

    if (rasaSoup.find(string=re.compile("Zoom"))).find_next('a').string is None:
        return "No zoom link found"
    else:
        return (rasaSoup.find(string=re.compile("Zoom"))).find_next('a').string



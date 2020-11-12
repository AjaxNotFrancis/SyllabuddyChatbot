from bs4 import BeautifulSoup, SoupStrainer
import re

# Syllabi Path Variables (for easy switching)
chem123 = "Syllabi/CHEM123.html"
hca540 = "Syllabi/HCA540.html"
template = "Syllabi/TEMP.html"

# Open file and generate soup
# with open(chem123, encoding='utf8') as fp:
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
# print(soup.find(string=re.compile("Instructor")))
# print((soup.find(string=re.compile("Zoom"))).find_next('a').string)
# print(soup.find(string=re.compile("Email")).find_next('a').string)


def find_instructor(course):
    with open("actions/" + course + ".html", encoding='utf8') as syllabus:
        rasaSoup = BeautifulSoup(syllabus, 'html.parser')

    if rasaSoup.find(string=re.compile("Instructor")) is None:
        return "No instructor found"
    else:
        return rasaSoup.find(string=re.compile("Instructor"))


def find_zoom(course):
    with open("actions/" + course + ".html", encoding='utf8') as syllabus:
        rasaSoup = BeautifulSoup(syllabus, 'html.parser')

    # if (rasaSoup.find(string=re.compile("Zoom"))).find_next('a').string is None:
    if (rasaSoup.find(string=re.compile("Zoom"))) is None:
        return "No zoom link found"
    else:
        return (rasaSoup.find(string=re.compile("Zoom"))).find_next('a').string


def find_prerequisites(course):
    with open("actions/" + course + ".html", encoding='utf8') as syllabus:
        rasaSoup = BeautifulSoup(syllabus, 'html.parser')

    if rasaSoup.find(string=re.compile("Prerequisites")) is None:
        return "No prerequisites found."
    else:
        result = rasaSoup.find(string=re.compile("Prerequisites")).find_next("p").string
        return result


def find_textbook(course):
    with open("actions/" + course + ".html", encoding='utf8') as syllabus:
        rasaSoup = BeautifulSoup(syllabus, 'html.parser', parse_only=SoupStrainer(id="4"))

    if rasaSoup.find(string=re.compile("Textbook")).find_next("h4").find_next("a") is None:
        return "No textbooks found."
    else:
        result = rasaSoup.find(string=re.compile("Textbook")).find_next("h4").find_next("a").get_text(" ")
    return result


def find_email(course):
    with open("actions/" + course + ".html", encoding='utf8') as syllabus:
        rasaSoup = BeautifulSoup(syllabus, 'html.parser', parse_only=SoupStrainer(id="1"))

    if rasaSoup.find(string=re.compile("Email")) is None:
        return "No email address found"
    else:
        result = rasaSoup.find(string=re.compile("Email")).find_next("a").string
    return result


def find_office(course):
    with open("actions/" + course + ".html", encoding='utf8') as syllabus:
        rasaSoup = BeautifulSoup(syllabus, 'html.parser', parse_only=SoupStrainer(id="1"))

    if rasaSoup.find(string=re.compile("Office")) is None:
        return "No office found."
    else:
        result = rasaSoup.find(string=re.compile("Office:"))
        result += rasaSoup.find(string=re.compile("Office:")).next
    return result


def find_phone(course):
    with open("actions/" + course + ".html", encoding='utf8') as syllabus:
        rasaSoup = BeautifulSoup(syllabus, 'html.parser', parse_only=SoupStrainer(id="1"))

    if rasaSoup.find(string=re.compile("Phone")) is None:
        return "No phone number found."
    else:
        result = rasaSoup.find(string=re.compile("Phone"))
        result += rasaSoup.find(string=re.compile("Phone")).next
    return result


#####################################################################
# TESTS
######################################################################
def test_find_prerequisites(course):
    with open(course + ".html", encoding='utf8') as syllabus:
        rasaSoup = BeautifulSoup(syllabus, 'html.parser')

    if rasaSoup.find(string=re.compile("Prerequisites")) is None:
        return "No instructor found"
    else:
        result = rasaSoup.find(string=re.compile("Prerequisites")).find_next("p").string
        return result


# print(test_find_prerequisites("HCA540"))


def test_find_textbook(course):
    with open(course + ".html", encoding='utf8') as syllabus:
        rasaSoup = BeautifulSoup(syllabus, 'html.parser', parse_only=SoupStrainer(id="4"))

    if rasaSoup.find(string=re.compile("Textbook")).find_next("h4").find_next("a") is None:
        return "No textbooks found."
    else:
        result = rasaSoup.find(string=re.compile("Textbook")).find_next("h4").find_next("a").get_text(" ")
    return result


# print(test_find_textbook("chem123"))
# print(test_find_textbook("hca540"))
# print(test_find_textbook("MoodlePageChem123"))
# print(test_find_textbook("TEMP"))


def test_find_email(course):
    with open(course + ".html", encoding='utf8') as syllabus:
        rasaSoup = BeautifulSoup(syllabus, 'html.parser', parse_only=SoupStrainer(id="1"))

    if rasaSoup.find(string=re.compile("Email")) is None:
        return "No email address found"
    else:
        result = rasaSoup.find(string=re.compile("Email")).find_next("a").string
    return result


# print(test_find_email("chem123"))
# print(test_find_email("hca540"))
# print(test_find_email("MoodlePageChem123"))
# print(test_find_email("TEMP"))


def test_find_office(course):
    with open(course + ".html", encoding='utf8') as syllabus:
        rasaSoup = BeautifulSoup(syllabus, 'html.parser', parse_only=SoupStrainer(id="1"))

    if rasaSoup.find(string=re.compile("Office")) is None:
        return "No office found."
    else:
        result = rasaSoup.find(string=re.compile("Office:"))
        result += rasaSoup.find(string=re.compile("Office:")).next
    return result


# print(test_find_office("chem123"))
# print(test_find_office("hca540"))
# print(test_find_office("MoodlePageChem123"))
# print(test_find_office("TEMP"))


def test_find_phone(course):
    with open(course + ".html", encoding='utf8') as syllabus:
        rasaSoup = BeautifulSoup(syllabus, 'html.parser', parse_only=SoupStrainer(id="1"))

    if rasaSoup.find(string=re.compile("Phone")) is None:
        return "No phone number found."
    else:
        result = rasaSoup.find(string=re.compile("Phone"))
        result += rasaSoup.find(string=re.compile("Phone")).next
    return result

# print(test_find_phone("chem123"))
# print(test_find_phone("hca540"))
# print(test_find_phone("MoodlePageChem123"))
# print(test_find_phone("TEMP"))

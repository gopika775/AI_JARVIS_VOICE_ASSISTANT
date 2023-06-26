import datetime
import wikipedia
from speak import Say

# Non-Input Functions

def Time():
    """
    Retrieves the current time and speaks it.
    """
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    """
    Retrieves the current date and speaks it.
    """
    date = datetime.date.today()
    Say(date)

def Day():
    """
    Retrieves the current day and speaks it.
    """
    day = datetime.datetime.now().strftime("%A")
    Say(day)

# Non-Input Execution

def NonInputExecution(query):
    """
    Executes the appropriate non-input function based on the query.

    Args:
        query (str): The user query.

    """
    query = str(query)

    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()

# Input Execution

def InputExecution(tag, query):
    """
    Executes the appropriate input function based on the tag and query.

    Args:
        tag (str): The tag indicating the type of input function.
        query (str): The user query.

    """
    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        result = wikipedia.summary(name)
        Say(result)

    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        import pywhatkit
        pywhatkit.search(query)

    elif "play" in tag:
        query = str(query).replace("play","")
        query = query.replace("search","")
        import pywhatkit
        pywhatkit.playonyt(query)

    


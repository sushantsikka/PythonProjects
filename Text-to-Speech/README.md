## Text to Speech for Adobe Helpx documents

This project uses Flask web framework to create a web app that takes shortened URL of Adobe Helpx articles and converts the content of article to speech.

The Python libraries used in the script are:

* Flask : for creating web application and API
* BeautifulSoup : for extracting content in h1 and p tags
* Speech : acts as an interface between the script and Windows text to speech capabilities

# reddit-flair-detector
## App that claasifies a post from Reddit using Natural Language Processing (NLP) and Classification Modeling.

### Data Extraction and Cleaning
I ectracted the Data using the praw API. I selected *15* flairs based on their number of occurrences (available in flair.txt in /Extraction and Cleaning). Also some of the flairs were simply selected because of their popularity as they pertain to recent events. (For Eg: Coronavirus, CAA-NRC). At first I extracted 100 posts for each flair alongwith 10  top comments per posts. Later on I extracted the data again with 100 posts per flair, but with 20 top comments. This was done due to two main reasons, firstly to try and increase my Model's Accuracy and secondly to get a little variance in the nature of the comments. (Top 10 comments were almost similar, 20 comments meant a little more variation albeit a little off-topic)

### EDA
The Data Analysis along with graphs is present in the directory /EDA. I tried to look at the percentage of which posts and the kind of data they hold. 
I looked at whether a particular attribute for a data was empty or not (Using a HeatMap). I Looked at the number and length of comments, titles flair wise. Using Bar-Graphs. The rationale behind this was to analyse the data and understand the usefulness of data that I have. The thought was: (Lesser the null values of the data, longer the length of titles, comments, bodies, higher the number of comments, better the data) 
I also tried to look at the 10 most reappearing words in the title, comment, body flairwise.
The rationale behind this was again to try to realize the uniqueness or even similarities for the flairs that I had chosen.

Some interesting Insights that I got were, for the flair "Politics" _modi_ was a word that was quite often used. Overall words like _india_ and _coronavirus_ dominated the most reappearing words due to the current scenario. Also the body of more than 50% posts that I extracted was empty.

### Data Training and Testing


  
 ### Web App 
The web app is present in the /webapp directory. The app has a Flask Backend and I have used a (HTML+CSS) template for the Frontend.

Heroku App Deployed on: http://redditflairaditya.herokuapp.com/

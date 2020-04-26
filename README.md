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

#### Finally, the Logistic Regression Model gave the highest accuracy results of about 70%.

I tried out various combinations of the data that I had extracted, trying out all Permutations and Combinations.

#### I have chosen 5 ML Algorithms namely:
1. Naive Bayes
2. Stochastic Gradient Descent
3. Logistic Regression
4. Random Forest
5. Linear Suport Vector Machine

##### 1.
First of all  I started with the *Individual* attributes i.e. titles, comments, url, body individually to see how the model was performing. Here because of the inconsistency of data for body and comments the model could simply be not run ( as for some flairs even in 100 there was not a single post with any body/comment). For title and url the accuracy was somewhere in the neighbourhood of *40%-45%*.

##### 2.
Now I started *grouping* the attributes together. I had expected the combination of [title, body, comments, url] i.e. all the data I had extracted for the purpose of training except for the flair itself to perform the best, but due to the inconsistencies of the data in body and comments the accuracy remained at about *60%-65%*. Then I started to remove these inconsistent data sets one by one to check my accuracy levels and I got the *highest* accuracy for the _combination [title, url, comments]_ for Logistic Regression at *70%*. 

As also I mentioned in the EDA file the longer length of Comments for the flair _[R]eddiquette_, the flair had the highest accuracy levels in almost all the 5 models that I tried.

  
 ### Web App 
The web app is present in the /webapp directory. The app has a Flask Backend and I have used a (HTML+CSS) template for the Frontend.

Heroku App Deployed on: http://redditflairaditya.herokuapp.com/

### How to run Locally (on your machine)
tada

### Sources (also in the sources.txt file)
I am fairly new in the field of Data Science specially NLP and the how do we go about the whole process.

As a result, throughout the project I followed/ took help from a number of Online Resources, Video Tutorials.
Below are the links to some of those resources which were the most helpful to me throughout the project, topic-wise.

#### 1) Data Extraction and Cleaning.

A great article that simply talks what data is, what makes it good, what makes it bad etc.
https://towardsdatascience.com/the-art-of-cleaning-your-data-b713dbd49726

This article is kind of an extension of above, and goes into a little more detail about the nuance of Data Cleaning.
(Also the article has great references for each individual aspect of data cleaning.
https://towardsdatascience.com/what-is-data-cleaning-how-to-process-data-for-analytics-and-machine-learning-modeling-c2afcf4fbf45

A very in-depth article which I found relatively easier to follow along than others online. (Also contains important Code Snippets)
https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html

#### 2) Data Analysis
A YouTube Video link that focusses primarily on seaborn and matplotlib to plot graphs.
https://www.youtube.com/watch?v=5NcbVYhQJvw

Another article which was very easy to follow along (the dataset it uses is also available, link in the article)
https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15

#### 3) Data Training and Testing
A good starting point,
https://www.digitalocean.com/community/tutorials/how-to-build-a-machine-learning-classifier-in-python-with-scikit-learn

These articles talks about how pipelining can be useful.
https://www.analyticsvidhya.com/blog/2020/01/build-your-first-machine-learning-pipeline-using-scikit-learn/
https://towardsdatascience.com/a-simple-example-of-pipeline-in-machine-learning-with-scikit-learn-e726ffbb6976

#### 4) Creating a WebApp and deploying to Heroku
An excellent Flask Tutorial (Video Tutorial + Blog)
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Great Article which takes you through the whole process from start to finish
https://blog.cambridgespark.com/deploying-a-machine-learning-model-to-the-web-725688b851c7

##### Apart from this, official documentation pages of praw, sklearn, rethinkDB were also quite useful for me!

praw: https://praw.readthedocs.io/en/latest/
sklearn: https://scikit-learn.org/stable/user_guide.html
rethinkDB: https://rethinkdb.com/docs

##### Lastly, The image for the background was taken from Google Images (Free to Use), and many elements for html page (css styles) were also taken from Internet with Free to Use licenses.


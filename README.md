# MachineLearningForSports



===================
What is our app?


MVC web app with continuous updating database (containing selective players or teams' incoming matches' schedules)

Viewer: A search tab allowing user to search for a certain player or team and generating a list of near incoming matches; user choose one of the matches to predict

Model: meachine learning trained model to predict the outcome of selected player or team's matches.



=============================
How do we train/evaluate the model? (what is our target?)

Using trained/tested result to compare with historical betting 



==================
What is our model?

Short-term goal(1): a pre-game prediciton model to predict a one-vs-one game outcome BEFORE the game starts; the model will refer to Imperial College London undergradute paper. (Of course, detailed algorithm will be different accordingly).


Short-term goal(2): a pre-game prediction to predict team sporst BEFORE the game starts.The model will refer to Springer paper; currently; we use unsupervised learning to model the underlying features of winning of team groups.


Long-term goal: a during-game prediction to predict sports DURING the game; given previous rounds result to predict next round in discrete time; given previous x minutes to predict the next y minutes in continous time. Using recurrent LSTM model Time series. 


=========
Short-term(1) TODO:

PHASE I :

(1) clean data; desgin a data structure for implementation

(2) Read two papers; considering one or more of the following methods for models: Random Forest, mixture of Gaussian, Principle Components Analysis, Bayesian Inference, Markvov Chain.

(3) Come up with a general strcuture of program(UML,CRC)

Few things to consider:

(1) What should our general features for all players; what are some specific features for some selective players; how about matches features??

(2) How do we treate categorial variables when we do regression ?? (ask Albert; he proposed this question)

(3) Should we let the model to decide the features ? Or we decide it our own.


PHASE I :

COMING SOON

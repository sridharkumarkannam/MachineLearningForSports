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


Long-term goal: a during-game prediction to predict sports DURING the game; given previous rounds result to predict next round in discrete time; given previous x minutes to predict the next y minutes in continous time. Using recurrent LSTM model  real-time streaming model. 


=========
Short-term(1) TODO:

PHASE I :

(1) clean data(done); create database; desgin a data structure and several methods for searching, pointing, sorting for implementation.

Current solution to the DataBase: Relation One contains match details (tournament name; type of court; players); relation Two: player A, Player B inforamtion including historical matches information, ages, L/R, height, weight, nationality, winning ratio on tournament and court, injury and fatigue.



(2) Read two papers; considering one or more of the following methods for models: Random Forest, mixture of Gaussian, Principle Components Analysis, Bayesian Inference, Markvov Chain.

Current solution: fit logitstic regression; minimize the entro-cross cost function and use gradient descent to update parameters until convergence.

(3) Hyperpameter optimization using grid search. 

(4) Evavulate the model with the state of art.

Few things to consider:

(1) What should our general features for all players; what are some specific features for some selective players; how about matches features??

(2) How do we treate categorial variables when we do regression ?? (ask Albert; he proposed this question)

(3) Should we let the model to decide the features ? Or we decide it our own.

(4) If we use Bayesian Inference: what prior do we choose? what's our likelihood function (what if the likelihood function doesn't have closed form) ?

PHASE II :

COMING SOON

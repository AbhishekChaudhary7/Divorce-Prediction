# Divorce_Prediction
## A mini project to predict divorce with the help of divorce dataset. Over that build a interactive Webapp with UI to predict divorce using questionnaire.

##Go through the screenshot folder in the directory to get a glace of Webapp

##Data Understanding:-

Data Source Link: https://archive.ics.uci.edu/ml/datasets/Divorce+Predictors+data+set

#### This dataset contains data about 150 couples with their corresponding Divorce Predictors Scale variables (DPS) on the basis of Gottman couples therapy. The couples are from various regions of Turkey wherein the records were acquired from face-to-face interviews from couples who were already divorced or happily married. All responses were collected on a 5 point scale (0=Never, 1=Seldom, 2=Averagely, 3=Frequently, 4=Always).

## Steps

### <-- Step1 -->---------------->>>Data collection and preprocessing<<<

As the data has no null values and all the cells have ordinal value, there is not much required in data preprocessing.

### <-- Step1 -->---------------->>>Model Building<<<

As the output feature is class variable. I am going to use MLP Classifier. MLPClassifier stands for Multi-layer Perceptron classifier which in the name itself connects to a Neural Network. Unlike other classification algorithms such as Support Vectors or Naive Bayes Classifier, MLPClassifier relies on an underlying Neural Network to perform the task of classification. Model also has been cross-validated using test-train split.


### <-- Step2 -->---------------->>>Dumping Model<<<

After building the model with 91.17% accuracy, it is dumped into a pickle file to use again into the webapp to predict the divorce.

### <-- Step3 -->---------------->>>Building Webapp<<<

With the help of Streamlit library, a basic Webapp has been build, Asking 54 quiestion from user, and detect his/her divorce.

### !!If you want to run this Webapp, please go through the requirment.txt to get all the prerequisite.!!

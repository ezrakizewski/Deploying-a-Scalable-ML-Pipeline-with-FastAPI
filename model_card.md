# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model Type: Random Forest Classifier
Version: 1.0
Framework: scikit-learn
Hyperparameters: n_estimators=100, random_state=42
Trained By: Ezra Kizewski
Date trained: March 2026
Contact: ekizew1@wgu.edu

## Intended Use
Primary use: Predict weather an indivduals incme exceeds $50k based on census demographic data.
Intended users: Students, researchers, ecucators, graders exploring census data.
Out-of-scope: This model should be used for educational purposes only and should not be used for financial decision-making.

## Training Data
Dataset: Census Income (census.csv)
Source: https://archive.ics.uci.edu/dataset/20/census+income
All Data Size: 32,561 rows 14 features + 1 label
Train split: 80% (~26,049 records) of the data using train_test_split with random_state=42
Categorical Features Used: "workclass", "education",
                            "marital-status","occupation", "relationship", "race",
                            "sex", "native-country"
Preprocessing: Categorical data was encoded using OneHotEncoder. The target (salary) was binarized using LabelBinarizer.


## Evaluation Data
Dataset: Census Income (census.csv)
Source: https://archive.ics.uci.edu/dataset/20/census+income
All Data Size: 32,561 rows 14 features + 1 label
Test Split: 20% (~6512 records) of the data
Preprocessing: Same steps as training data
                (preprocessing: Categorical data was encoded using OneHotEncoder. The target (salary) was  binarized using LabelBinarizer.)

## Metrics
The model was evaluated using Precision, Recall and F1 Score (fbeta with beta=1)

| Metric      | Score     |
| ------------| --------- |
| Precision   | 0.7419    |
| Recall      | 0.6384    |
| F1 Scoer    | 0.6863    |

## Ethical Considerations
The Census data reflects socioeconomic conditions from 1994, making it significantly outdated and should not be used for current real-world applications. 

This is an unbalnced dataset that has the majority of records representing those from the United States which could lead to bias.

Decision making should be carefully considered when you start considering native-country, race, sex, age, and education. 
This can create unfair bias and could lead to ethical and potentially legal issues.


## Caveats and Recommendations
Data Age: The data on this website was donated in 1994 and would not be accurate for current incomes by demographic.
class imbalance: The United States has the majority of records, and the majority of records report <= 50K for income.
Hyperparameter Tuning: No hyperparameter tuning was implemented, and I used the default Random Forest Parameters. 
                       GridSearch could be implemented to build a better performing model.
Recommended Next Steps: Try using GridSearch for building a better model. Also, try using and evaluating other ML Models. The dataset should be further evaluated for skewness and steps should be taken to balance this out or make use of tools that will help remove bias.
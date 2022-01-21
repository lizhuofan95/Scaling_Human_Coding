# Scaling_Human_Coding
Replication code for "How Well Does Supervised Machine Learning Code?"

This repository contains code for replication. However, to protect the confidentiality of human subjects data in accordance with IRB mandates, we are unable to provide the dataset at this time. Code for data cleaning has also been removed for the same reason. Nonetheless, this should give other social scientists adequate information to understand how each method is configured and implemented to produce the results we present in the paper, and replicate in their own work.

* `LogisticNgram_forReplication.ipynb` implements logistic regression with bag-of-words features using the `scikit-learn` library.
* `BERTFineTuning_forReplication.ipynb` implements BERT-fine-tuning using the `transformer` and `pytorch` libraries. 
* `LogisticCE_forReplication.ipynb` implements logistic regression with contextualized embedding features extracted from distilled-BERT. 

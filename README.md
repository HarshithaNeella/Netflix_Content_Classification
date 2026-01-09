🎬 Netflix Content Type Classification (Movie vs TV Show)

This project implements a text classification system to predict whether a Netflix title is a Movie or a TV Show using its description text. The project follows a complete NLP workflow, including text preprocessing, feature extraction, model experimentation, and evaluation.

🧠 Project Workflow

Text cleaning and normalization

Feature extraction using TF-IDF (uni-grams & bi-grams)

Model experimentation (SVM, AdaBoost, Logistic Regression)

Model evaluation using accuracy, precision, recall, and F1-score

Final model selection based on generalization and class balance

🛠️ Technologies Used

Python

Libraries:

pandas, numpy

scikit-learn

Techniques:

Natural Language Processing (NLP)

TF-IDF Vectorization

Logistic Regression

Pipeline construction

Model evaluation with classification reports

✅ Conclusion

This project successfully applies TF-IDF and Logistic Regression to classify Netflix content descriptions as Movies or TV Shows. The final model demonstrates stable performance and good generalization on unseen data, making it a reliable solution for text-based classification tasks.


🔮 Future Work

Improve minority class performance by tuning decision thresholds and evaluation metrics such as F1-score.

Experiment with word embeddings (Word2Vec or GloVe) to capture semantic meaning beyond TF-IDF.

Try advanced linear models such as Linear SVM and compare results with Logistic Regression.

Perform hyperparameter tuning using cross-validation for better generalization.


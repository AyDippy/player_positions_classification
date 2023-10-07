# Player Position Classification Project

## Introduction
This project aims to predict the best playing position for soccer players based on their individual statistics and attributes. The project utilizes machine learning techniques to develop a predictive model for assigning players to positions on the field.

## Problem Statement
Soccer is a highly dynamic sport, and the performance of players can vary greatly depending on their positions. The goal of this project is to build a model that can accurately recommend the optimal position for a player based on their skills and attributes.

## Objective
The primary objective of this project is to:
- Collect and preprocess soccer player data.
- Develop a machine learning model for player position prediction.
- Achieve high prediction accuracy and model interpretability.

## Dataset
The dataset used for this project contains detailed statistics and attributes of soccer players, including numerical and categorical features. Each player is associated with a specific playing position, making it suitable for supervised learning.

- Kaggle Dataset: [FIFA 23 Players Dataset](https://www.kaggle.com/datasets/sanjeetsinghnaik/fifa-23-players-dataset)

## Project Structure
The project is structured as follows:
1. Data Collection: Data was obtained from Kaggle.
2. Exploratory Data Analysis (EDA): Initial data exploration was performed to understand the dataset and its characteristics.
3. Feature Selection: A process of selecting relevant features for the model was carried out.
4. Data Preprocessing: Numerical and categorical features were transformed and prepared for model training.
5. Model Training: An XGBoost classifier was trained using the preprocessed data.
6. Hyperparameter Tuning: RandomizedSearchCV was used to optimize the model's hyperparameters.
7. Model Evaluation: The model's performance was assessed using various metrics, including accuracy.
8. Model Saving: The trained model was saved using Joblib for deployment.
9. Deployment: The saved model was deployed using Streamlit.

## Key Findings
During the project, the following key findings were made:
- Certain player attributes are strongly indicative of their playing positions.
- Feature selection and preprocessing play a crucial role in model performance.
- The XGBoost classifier achieved high prediction accuracy (over 92%) for player positions.

## Project Author
- Name: Dipeolu Ayomide
- Email: ayomidedipeolu@gmail.com

## Deployed App
You can access the deployed player position prediction app using the following link:
- [Player Position Prediction App](https://playerpositionsclassification-k7tvekpuveqjskk6scafyt.streamlit.app/)

## How to Run the Project
To run the player position prediction app locally, follow these steps:
1. Clone the GitHub repository.
2. Install the required dependencies (`pip install -r requirements.txt`).
3. Run the Streamlit app (`streamlit run player_position_app.py`).
4. Use the app to input player attributes and receive position predictions.

## Acknowledgments
- The dataset used in this project was obtained from Kaggle.
- Special thanks to the Streamlit community for their support in deploying the app.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

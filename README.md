# 🚗 Car Price Prediction - Morocco

This project aims to build a **Machine Learning application** to predict the price of used cars in Morocco.  
The goal is to provide a **reliable and accurate estimate** based on various features such as brand, model, year, mileage, fuel type, and more.

---

##  Introduction

The used car market in Morocco is growing rapidly, but prices often lack structure and depend on negotiation, location, and seller perception.  
This project aims to:

- Identify the **key factors** that influence car prices.
- Provide an **automatic and reliable price estimation**.
- Help buyers, sellers, and platforms **make data-driven decisions**.

**Expected result:**  
An easy-to-use web application that predicts the price of a used car based on its specifications.

---

##  Dataset

The dataset contains **24,776 real ads** collected from the Moroccan market via Avito.  
After cleaning and processing, the final dataset contains **20,324 records** and **28 features**.

**Main features include:**

- **Brand** (e.g., Volkswagen, Renault, Dacia, Toyota, etc.)
- **Model**
- **Year of manufacture**
- **Mileage**
- **Fuel type** (Diesel, Gasoline, Hybrid)
- **Fiscal power**
- **Transmission type** (Manual, Automatic)
- **Vehicle condition**
- **Price**

---

##  Data Preprocessing

### Main steps:
1. **Handling missing values** and replacing anomalies.
2. Transforming mileage from ranges (`"200000 - 249999" → 224999.5`).
3. **Encoding categorical variables** using `LabelEncoder` and `OneHotEncoder`.
4. Scaling numerical variables using `StandardScaler`.
5. Removing duplicates and irrelevant data (e.g., extreme prices, rare brands).

---

##  Exploratory Data Analysis (EDA)

Some visualizations were created to better understand the data:
- Distribution of cars by **brand**.
- Average price by **brand** and **fuel type**.
- Impact of **mileage on price**.
- **Correlation matrix** between numerical variables.

---

##  Modeling

Several machine learning algorithms were tested:

| Model            | MAE (Mean Absolute Error) | RMSE (Root Mean Squared Error) | R² (Score) |
|------------------|---------------------------|--------------------------------|------------|
| **Random Forest**  | 5,333                    | 17,776                          | **0.95**   |
| XGBoost          | 11,284                    | 27,110                          | 0.88       |
| LightGBM         | 14,616                    | 35,726                          | 0.80       |
| CatBoost         | 17,585                    | 43,046                          | 0.71       |
| Ridge Regression | 33,003                    | 64,800                          | 0.35       |
| Lasso Regression | 33,003                    | 64,800                          | 0.35       |
| Linear Regression| 33,003                    | 64,800                          | 0.35       |

**Final model selected:** `RandomForestRegressor`  
- R² Score: **0.95**  
- High performance and very low prediction error.

---

##  Model Saving

The final trained model is saved using `pickle` under the name: car_model


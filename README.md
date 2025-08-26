# 🍎 Nutritional Analysis Chatbot (Deep Learning + Streamlit)

This project is an **AI-powered Nutrition Assistant** that provides **dietary suggestions, food and nutrition analysis, and calorie recommendations**.
It uses **Deep Learning models** to analyze input (including text and food images) and a **Streamlit UI** for an interactive experience.

---

## 🚀 Features

* ✅ Accepts **food input (text or image)**
* ✅ Performs **nutritional analysis & calorie estimation**
* ✅ Provides **dietary recommendations**
* ✅ User-friendly **Streamlit interface**
* ✅ Modular Python scripts for **model & app separation**

---

## 🛠️ Tech Stack

* **Programming Language:** Python 3.8+
* **Libraries & Frameworks:**

  * Deep Learning: TensorFlow / Keras / PyTorch (based on your code)
  * Data Processing: pandas, numpy
  * Visualization: matplotlib, seaborn
  * UI: Streamlit
* **IDE Used:** VSCode

---

## 📂 Project Structure

```
├── project_DL.py        # Deep Learning model training & prediction
├── Streamlitfile.py     # Streamlit app (UI for chatbot)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/nutritional-analysis-chatbot.git
   cd nutritional-analysis-chatbot
   ```

2. **Create virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate      # Mac/Linux
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Project

### 1. Run the Deep Learning Model

```bash
python project_DL.py
```

* Trains/loads the nutrition analysis model
* Saves the model for later use in the chatbot

### 2. Run the Streamlit App

```bash
streamlit run Streamlitfile.py
```

* Opens the chatbot in your browser
* Upload food images or enter food details
* Get instant nutritional insights & recommendations

---

## 💡 Example Usage

* Input: *“2 boiled eggs and a glass of milk”*
* Output:

  * Calories: \~220 kcal
  * Protein: 14g
  * Fat: 12g
  * Recommendation: “Good protein intake! Pair with some whole grains for a balanced meal.”

---

## 📌 Future Improvements

* 🔹 Enhance food image classification with larger datasets
* 🔹 Integrate with fitness trackers & diet APIs
* 🔹 Add personalized meal planning
* 🔹 Deploy on cloud (AWS/GCP/Streamlit Cloud)

---

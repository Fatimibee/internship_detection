# 🧠 Internship Detection WebApp  
**Detecting Genuine vs. Fake Internships Using Machine Learning**

## 📋 Project Overview
The **Internship Detection WebApp** is an AI-powered solution that helps students verify whether internship postings are **genuine or fake**.  
It leverages **Complemented Naive Bayes (CNB)** for text classification and provides a **Streamlit-based interface** for instant prediction.

This project aims to **empower students** by reducing fraud and misinformation during internship searches.

## 🚨 Problem Statement
The rise of fake internship offers has become a major concern in the digital era. Many fraudulent listings exploit students’ ambitions, leading to:
- Wasted time and effort  
- Loss of trust in legitimate platforms  
- Potential personal and financial risks  

Thus, there is an urgent need for an **automated verification system** to ensure the authenticity of internship postings.

## 🎯 Objective
To develop a **machine learning model** that accurately classifies internship postings as **Genuine** or **Fake**, providing:
- Instant predictions  
- High precision and recall  
- User-friendly web interface for real-time verification  

## 🧩 Features
- 🧾 **Paste internship text:** Users input full internship details.  
- ⚙️ **Instant prediction:** Model outputs “Genuine” or “Fake” with confidence.  
- 🎨 **Simple Streamlit UI:** Interactive and easy-to-use design.  
- 📊 **Model Accuracy:** Achieved **97% accuracy** with robust validation.  

## 🧠 Machine Learning Model
### Algorithm Used:
**Complemented Naive Bayes (CNB)**  
Chosen for its strong performance on text classification tasks and ability to handle imbalanced data.

### Key Advantages:
- Reduces bias towards frequent classes.  
- Performs better than Multinomial Naive Bayes on sparse data.  
- Offers high precision and recall, minimizing false positives/negatives.  

### Data Processing:
- **Dataset:**  
  - Real internship data scraped from *Internshala* using BeautifulSoup.  
  - Fake internship data sourced from *Kaggle*.  
- **Text Preprocessing:**  
  - Tokenization, stopword removal, and TF-IDF vectorization.  
- **Feature Engineering:**  
  - Extracted key fields (company name, description, etc.).  
- **Data Balancing:**  
  - Ensured equal representation of fake and genuine classes.

## 🛠️ Tech Stack
| Component | Technology |
|------------|-------------|
| **Programming Language** | Python |
| **Framework** | Streamlit |
| **ML Library** | Scikit-learn |
| **Model Serialization** | Joblib |
| **Data Collection** | BeautifulSoup, Kaggle datasets |
| **Version Control** | GitHub |

## 💻 Installation & Setup
1. **Clone this repository**
   ```bash
   git clone https://github.com/Fatimibee/internship_detection
   cd internship-detection
   ```


2. **Run the Streamlit App**
   ```bash
   streamlit run page.py
   ```

3. **Paste internship text** into the input box and view prediction instantly!

## 📈 Model Performance
| Metric | Score |
|--------|--------|
| **Accuracy** | 97% |
| **Fake Precision** | 96% |
| **Fake Recall** | 94% |

The model generalizes well and was validated on unseen data to ensure real-world applicability.

## 🚀 Future Enhancements
- 🔍 **Advanced NLP models** – Integrate transformers (e.g., BERT) for deeper semantic understanding.  
- ☁️ **Cloud Deployment** – Deploy for public access (e.g., AWS, Streamlit Cloud).  
- 📱 **Mobile App** – Allow internship verification on the go.  
- 🗂️ **User Feedback Loop** – Improve accuracy based on real user responses.  

## 🧾 Project Contributors
**Developed by:**  
👩‍💻 *Fatimi Bee*  
Roll No.: 23ESKCS077  
B.Tech CSE, 5th Semester  
Swami Keshvanand Institute of Technology, Management & Gramothan, Jaipur  

## 📚 References
- Internshala dataset (scraped data)  
- Kaggle: Fake Internship Listings Dataset  
- Scikit-learn Documentation  
- Streamlit Official Docs  

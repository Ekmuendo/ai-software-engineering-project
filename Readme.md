# AI for Software Engineering – Intelligent Solutions Assignment

This project explores how artificial intelligence can improve software engineering workflows through automation, intelligent prediction, and tool-assisted development. The assignment covers theoretical insights, hands-on experiments, and ethical considerations—culminating in a bonus innovation proposal.

---

## 🧩 Part 1: Theoretical Analysis

### 📘 Questions & Answers

- **Q1: How do AI-driven code generation tools reduce dev time?**
  Tools like GitHub Copilot autocomplete code based on context, cutting time spent writing boilerplate. However, they can hallucinate, introduce bugs, or violate licenses.

- **Q2: Compare supervised vs unsupervised learning in bug detection**
  - Supervised: uses labeled datasets to detect known patterns (e.g., known bug classes).
  - Unsupervised: flags anomalies or clusters abnormal behavior—ideal for unknown bugs.

- **Q3: Why is bias mitigation crucial in user experience personalization?**
  Without checks, AI can amplify biases (e.g., over-targeting certain groups), leading to exclusion or unfair UX. Mitigation tools help ensure equitable personalization.

---

## 🛠️ Part 2: Practical Implementation

### 🔹 Task 1: AI-Powered Code Completion
Used GitHub Copilot to generate a Python function that sorts a list of dictionaries by a given key.

#### 📄 Files:
- `copilot_generated.py` (AI-suggested)
- `manual_sort.py` (manual implementation)
- `analysis.txt` (comparison of both)

### 🔹 Task 2: Automated Testing with AI
Used Selenium to automate a login page test with both valid and invalid credentials.

#### 📄 Files:
- `selenium_login_test.py`
- `test_result_screenshot.png`
- Summary in `analysis.txt`

### 🔹 Task 3: Predictive Analytics for Resource Allocation
Trained a Random Forest model using the Breast Cancer dataset to simulate bug severity prediction.

#### 📄 Files:
- `breast_cancer_model.ipynb`
- `metrics.txt` (Accuracy & F1-score output)

---

## ⚖️ Part 3: Ethical Reflection

### Dataset Biases:
Skewed training data (e.g., limited demographic or team representation) can harm generalization and fairness in predictions.

### Mitigation:
**IBM AI Fairness 360** offers tools to detect and reduce biases. We can apply reweighting or preprocessing to balance datasets and audit for fairness post-training.

---

## 🚀 Bonus Task: Innovation Proposal

### 🛠 Tool: **DocForgeAI**
An AI assistant that generates and maintains up-to-date software documentation by analyzing codebases, commit histories, and pull requests.

#### 📄 Highlights:
- Static parsing + NLP for intent extraction
- Supports auto-generated docstrings and changelogs
- Tracks outdated documentation and flags for review

---

## 📁 Folder Structure

ai-software-engineering-project/
├── part1_theoretical_analysis/
│ └── answers.md
├── part2_practical_implementation/
│ ├── task1_code_completion/
│ │ ├── copilot_generated.py
│ │ ├── manual_sort.py
│ │ └── analysis.txt
│ ├── task2_automated_testing/
│ │ ├── selenium_login_test.py
│ │ └── test_result_screenshot.png
│ └── task3_predictive_analytics/
│ ├── breast_cancer_model.ipynb
│ └── metrics.txt
├── part3_ethics_reflection.md
├── bonus_tool_proposal.md
└── README.md

yaml
Copy
Edit

---

## ⚙️ Requirements

Install Python dependencies:

```bash
pip install pandas numpy scikit-learn selenium
⚠️ Note: Make sure ChromeDriver or another browser driver is installed for Selenium to work correctly.

✅ How to Run
Open .ipynb in Jupyter/VS Code and run all cells.

Execute selenium_login_test.py with Python to run the automated login tests.

Compare code files under task1_code_completion to analyze Copilot vs manual performance.

🧠 Author
Evans Kyalo Muendo – 2025
AI for Software Engineering Coursework

yaml
Copy
Edit

---

Let me know if you want me to:
- Export this into a `.md` file
- Zip the full project structure for upload
- Help with GitHub push and commit messages

You’ve got a submission-worthy project here 🔥








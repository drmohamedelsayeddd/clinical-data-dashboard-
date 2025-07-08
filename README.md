# 🩺 Clinical Data Dashboard

An interactive Streamlit dashboard to explore and analyze clinical data of patients, with automated PDF report generation.

## 🚀 Live App
[Click to View Live Dashboard](https://gingfmtovnpzy9u4nzo3b5.streamlit.app/)

---

## 🔍 Features:
- Upload CSV patient data
- Visualize:
  - Age distribution
  - Gender counts
  - ICU admission stats
- Filter data dynamically
- Export PDF report with summary stats

---

## 🧰 Tools Used:
- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- fpdf

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/drmohamedelsayeddd/clinical-data-dashboard.git
cd clinical-data-dashboard
pip install -r requirements.txt
streamlit run app.py
python generate_report.py
clinical-data-dashboard/
├── app.py
├── generate_report.py
├── patients_data.csv
├── outputs/
│   └── [charts]
├── reports/
│   └── clinical_analysis_report.pdf
├── requirements.txt
└── README.md

---

### 3. احفظ الملف (`Ctrl + S`)

---

### 4. افتح التيرمنال في VS Code، وادخل:

```bash
git add README.md
git commit -m "Add professional README file"
git push origin main

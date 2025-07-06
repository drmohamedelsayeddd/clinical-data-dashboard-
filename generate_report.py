from fpdf import FPDF
from datetime import datetime
import os

# تأكد إن مجلد reports موجود
os.makedirs("reports", exist_ok=True)

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Clinical Data Analysis Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

# أنشئ ملف PDF جديد
pdf = PDFReport()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# بيانات العنوان
pdf.set_font("Arial", "", 12)
pdf.cell(0, 10, f"Prepared by: Dr. Mohamed Hawary", ln=True)
pdf.cell(0, 10, f"Date: {datetime.today().strftime('%Y-%m-%d')}", ln=True)
pdf.ln(10)

# ملاحظات أساسية
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Key Observations:", ln=True)
pdf.set_font("Arial", "", 11)
observations = [
    "- Most ICU admissions occur in diabetic patients.",
    "- Higher temperatures are linked with mortality.",
    "- Age distribution skews toward older adults.",
    "- There is a correlation between age and ICU admission."
]
for obs in observations:
    pdf.cell(0, 10, obs, ln=True)
pdf.ln(10)

# صور التحليل (تأكد إنها محفوظة في مجلد outputs)
image_files = [
    ("outputs/age_distribution.png", "Age Distribution"),
    ("outputs/icu_vs_diabetes.png", "ICU vs Diabetes"),
    ("outputs/temp_vs_death.png", "Temperature vs Death"),
    ("outputs/correlation_heatmap.png", "Correlation Heatmap")
]

for path, title in image_files:
    if os.path.exists(path):
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, title, ln=True)
        pdf.image(path, w=170)
        pdf.ln(10)
    else:
        pdf.cell(0, 10, f"[Missing Image] {title} - {path}", ln=True)

# حفظ التقرير
pdf.output("reports/clinical_analysis_report.pdf")

print(" PDF Report Generated Successfully!")

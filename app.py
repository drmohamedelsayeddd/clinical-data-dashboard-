# -------------------------
# app.py - Clinical Data Dashboard
# -------------------------

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# إنشاء فولدر لحفظ الصور
os.makedirs("outputs", exist_ok=True)

# إعداد شكل الصفحة
st.set_page_config(page_title="Clinical Data Dashboard", layout="wide")

# عنوان رئيسي
st.title("🩺 Clinical Data Dashboard")

# تحميل البيانات من الملف
@st.cache_data
def load_data():
    df = pd.read_csv("full_patients_data.csv")
    return df

df = load_data()

# ✅ فلاتر في الشريط الجانبي
st.sidebar.header("🔍 Filter Data")

min_age = int(df["Age"].min())
max_age = int(df["Age"].max())
age_filter = st.sidebar.slider("Age", min_value=min_age, max_value=max_age, value=(min_age, max_age))

gender_filter = st.sidebar.multiselect("Gender", options=df["Gender"].unique(), default=df["Gender"].unique())
diabetes_filter = st.sidebar.multiselect("Diabetes", options=df["Diabetes"].unique(), default=df["Diabetes"].unique())

# تطبيق الفلاتر على الداتا
filtered_df = df[
    (df["Age"] >= age_filter[0]) &
    (df["Age"] <= age_filter[1]) &
    (df["Gender"].isin(gender_filter)) &
    (df["Diabetes"].isin(diabetes_filter))
]

# ✅ عرض البيانات
st.subheader("📄 Filtered Patient Data")
st.dataframe(filtered_df, use_container_width=True)

# ✅ Age Distribution
st.subheader("📊 Age Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(filtered_df["Age"], bins=20, kde=True, ax=ax1)
fig1.savefig("outputs/age_distribution.png")
st.pyplot(fig1)

# ✅ ICU Admissions vs Diabetes
st.subheader("🏥 ICU Admissions by Diabetes")
fig2, ax2 = plt.subplots()
sns.countplot(data=filtered_df, x="ICU_Admitted", hue="Diabetes", ax=ax2)
fig2.savefig("outputs/icu_vs_diabetes.png")
st.pyplot(fig2)

# ✅ Temperature vs Death
st.subheader("🌡️ Temperature vs Death")
fig3, ax3 = plt.subplots()
sns.boxplot(data=filtered_df, x="Death", y="Temp", ax=ax3)
fig3.savefig("outputs/temp_vs_death.png")
st.pyplot(fig3)

# ✅ Correlation Heatmap
st.subheader("🧠 Correlation Heatmap")
fig4, ax4 = plt.subplots()
corr = filtered_df.select_dtypes(include="number").corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax4)
fig4.savefig("outputs/correlation_heatmap.png")
st.pyplot(fig4)

# ✅ رسالة ختامية
st.markdown("---")
st.success("✅ Dashboard Generated Successfully!")
# ✅ Histogram of Age
st.subheader("📊 Histogram - Age Distribution")
fig_hist, ax_hist = plt.subplots()
sns.histplot(filtered_df["Age"], bins=20, kde=True, ax=ax_hist, color="skyblue")
st.pyplot(fig_hist)
# ✅ Line Chart - Number of Patients by Age
st.subheader("📈 Line Chart - Patients by Age")
age_counts = filtered_df["Age"].value_counts().sort_index()
fig_line, ax_line = plt.subplots()
ax_line.plot(age_counts.index, age_counts.values, marker='o', linestyle='-', color='green')
ax_line.set_xlabel("Age")
ax_line.set_ylabel("Number of Patients")
st.pyplot(fig_line)
# ✅ Pie Chart - Gender Distribution
st.subheader("🧁 Pie Chart - Gender Distribution")
gender_counts = filtered_df["Gender"].value_counts()
fig_pie, ax_pie = plt.subplots()
ax_pie.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", startangle=90, colors=["#ff9999", "#66b3ff"])
ax_pie.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig_pie)

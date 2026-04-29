<div align="center">

<!-- BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=AI%20Resume%20Analyzer&fontSize=48&fontColor=ffffff&animation=twinkling&fontAlignY=35&desc=Intelligent%20Resume%20Analysis%20Powered%20by%20NLP%20%26%20Machine%20Learning&descSize=16&descAlignY=55" width="100%"/>

<!-- BADGES ROW 1 -->
<p>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/NLP-spaCy%20%7C%20NLTK-09A3D5?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
</p>

<!-- BADGES ROW 2 -->
<p>
  <img src="https://img.shields.io/github/stars/BurukalaManiReethika/ai-resume-analyzer2?style=for-the-badge&color=gold&logo=github"/>
  <img src="https://img.shields.io/github/forks/BurukalaManiReethika/ai-resume-analyzer2?style=for-the-badge&color=blue&logo=github"/>
  <img src="https://img.shields.io/github/issues/BurukalaManiReethika/ai-resume-analyzer2?style=for-the-badge&color=red&logo=github"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

<!-- QUICK LINKS -->
<p>
  <a href="#-demo"><strong>🎥 Demo</strong></a> •
  <a href="#-features"><strong>✨ Features</strong></a> •
  <a href="#-tech-stack"><strong>🛠️ Tech Stack</strong></a> •
  <a href="#-installation"><strong>🚀 Installation</strong></a> •
  <a href="#-usage"><strong>📖 Usage</strong></a> •
  <a href="#-contributing"><strong>🤝 Contributing</strong></a>
</p>

<br/>

> **🎯 A smart, AI-driven resume analysis platform that parses resumes using Natural Language Processing, extracts key skills, maps candidates to career domains, and delivers personalized recommendations — empowering job seekers to land their dream roles.**

<br/>

</div>

---

## 📸 Demo

<div align="center">

| Upload Resume | Analysis Dashboard | Skill Recommendations |
|:---:|:---:|:---:|
| ![Upload]() | ![Dashboard]() | ![Skills]() |
| *Drag & drop PDF upload* | *Real-time NLP analysis* | *Personalized course suggestions* |

> 💡 **[Live Demo](#)** · **[Watch Video Walkthrough](#)**

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔍 Smart Resume Parsing
- Extracts personal info, education, experience, and skills from PDF resumes
- Supports multi-page, multi-format resumes
- Powered by `pyresparser` + `spaCy` NLP pipelines

### 📊 AI-Powered Analysis
- Resume strength scoring (Beginner / Intermediate / Expert)
- Domain/sector classification using keyword clustering
- Missing skills detection and gap analysis

### 🎯 Career Recommendations
- Role-matched skill suggestions
- Curated YouTube courses & online learning resources
- Resume writing tips tailored per level

</td>
<td width="50%">

### 📈 Interactive Analytics Dashboard
- Visual insights for applicants and admins
- Pie charts, bar graphs, and trend data
- Historical analysis tracking over time

### 🔐 Dual-Mode Interface
- **User Mode** — Upload, analyze, and improve your resume
- **Admin Mode** — Monitor all users, export data, view analytics

### 💾 Persistent Data Storage
- MySQL database integration
- Session history and progress tracking
- Export reports as CSV

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|:---:|:---|
| **Frontend** | Streamlit, HTML/CSS |
| **Backend** | Python 3.9+ |
| **NLP Engine** | spaCy, NLTK, pyresparser |
| **Database** | MySQL |
| **PDF Parsing** | pdfminer3, PyPDF2 |
| **Visualization** | Plotly, Matplotlib |
| **Recommendation** | Keyword Matching + Sector Clustering |

</div>

---

## 📁 Project Structure

```
ai-resume-analyzer2/
│
├── 📄 App.py                    # Main Streamlit application entry point
├── 📂 Uploaded_Resumes/         # Temporary storage for uploaded PDFs
├── 📂 assets/                   # Images, logos, and static resources
│   └── logo.png
├── 📂 courses/                  # Course recommendation data
│   └── courses.py
├── 📂 database/                 # MySQL schema and connection logic
│   └── db_setup.sql
├── 📄 requirements.txt          # Python dependencies
└── 📄 README.md
```

---

## 🚀 Installation

### Prerequisites

Make sure you have the following installed:

- Python `3.9+`
- MySQL Server `8.0+`
- pip `22+`

### Step-by-Step Setup

**1. Clone the repository**

```bash
git clone https://github.com/BurukalaManiReethika/ai-resume-analyzer2.git
cd ai-resume-analyzer2
```

**2. Create and activate a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Download spaCy language model**

```bash
python -m spacy download en_core_web_sm
```

**5. Configure your MySQL database**

```sql
CREATE DATABASE cv_db;
```

Then update the database credentials inside `App.py`:

```python
connection = pymysql.connect(
    host='localhost',
    user='YOUR_USERNAME',      # ← update this
    password='YOUR_PASSWORD',  # ← update this
    db='cv_db'
)
```

**6. Launch the application**

```bash
streamlit run App.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 📖 Usage

### 👤 User Mode

| Step | Action |
|:---:|:---|
| 1 | Open the app and select **User** from the sidebar |
| 2 | Enter your name and email |
| 3 | Upload your resume in **PDF format** |
| 4 | Instantly view your parsed data, resume score, and recommendations |
| 5 | Explore suggested skills, courses, and career tips |

### 🔑 Admin Mode

```
Default credentials:
  Username: admin
  Password: admin@resume-analyzer
```

> ⚠️ **Change credentials before deploying to production!**

In Admin Mode you can:
- View all uploaded resumes and parsed data
- Access analytics: user count, experience level distribution, skills heatmap
- Download the full user data table as CSV

---

## 📊 How It Works

```
                    ┌──────────────────────┐
                    │     Upload Resume     │
                    │       (PDF)           │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │    PDF Text Extract   │
                    │  pdfminer3 / PyPDF2   │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │    NLP Processing     │
                    │  spaCy + pyresparser  │
                    │  (Name, Email, Skills │
                    │   Education, etc.)    │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
   ┌──────────▼──────┐ ┌───────▼──────┐ ┌──────▼──────────┐
   │  Resume Scoring  │ │ Domain/Role  │ │  Skill Gap &    │
   │  (Beginner /     │ │ Prediction   │ │  Course Reco-   │
   │  Intermediate /  │ │ (Clustering) │ │  mmendations    │
   │  Expert)         │ └──────────────┘ └─────────────────┘
   └──────────────────┘
              │
   ┌──────────▼───────────┐
   │   Store in MySQL DB   │
   │   Display Dashboard   │
   └───────────────────────┘
```

---

## 🔮 Roadmap

- [x] PDF resume parsing and NLP extraction
- [x] Skill recommendations and course suggestions
- [x] Admin analytics dashboard
- [x] MySQL data persistence
- [ ] 🔄 DOCX resume support
- [ ] 🤖 LLM-based resume rewriting (GPT / Gemini integration)
- [ ] 📧 Email report delivery
- [ ] 🌐 Cloud deployment (Heroku / Render / AWS)
- [ ] 🔗 LinkedIn job scraping integration
- [ ] 📱 Mobile-responsive UI overhaul

---

## 🤝 Contributing

Contributions are what make the open-source community thrive. Any contribution you make is **greatly appreciated**!

```bash
# 1. Fork the Project
# 2. Create your Feature Branch
git checkout -b feature/AmazingFeature

# 3. Commit your Changes
git commit -m 'Add some AmazingFeature'

# 4. Push to the Branch
git push origin feature/AmazingFeature

# 5. Open a Pull Request
```

Please read our **[Contributing Guidelines](CONTRIBUTING.md)** before submitting a PR.

---

## 🐛 Known Issues & Troubleshooting

<details>
<summary><strong>❌ <code>pyresparser</code> installation fails</strong></summary>

```bash
pip install pyresparser --no-deps
pip install docopt==0.6.2
```
</details>

<details>
<summary><strong>❌ spaCy model not found</strong></summary>

```bash
python -m spacy download en_core_web_sm
# If still failing:
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1.tar.gz
```
</details>

<details>
<summary><strong>❌ MySQL connection refused</strong></summary>

Make sure MySQL is running and the credentials in `App.py` match your local setup. Confirm the `cv_db` database exists.
</details>

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

## 👩‍💻 Author

<div align="center">

<img src="https://avatars.githubusercontent.com/BurukalaManiReethika" width="100px" style="border-radius:50%"/>

### Burukala Mani Reethika

*AI & ML Enthusiast | Final Year Student*

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BurukalaManiReethika)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](#)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](#)

</div>

---

## 🌟 Show Your Support

If this project helped you, please consider giving it a ⭐ — it means the world and helps others discover the project!

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=BurukalaManiReethika/ai-resume-analyzer2&type=Date)](https://star-history.com/#BurukalaManiReethika/ai-resume-analyzer2)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

*Built with ❤️ by Burukala Mani Reethika*

</div>

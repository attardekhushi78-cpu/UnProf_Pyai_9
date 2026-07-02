<a id="top"></a>

# 🌌 ScholarOps Intermediate Software & Text AI Portfolio

### A unified repository tracking daily implementation milestones across intermediate Python software engineering, automated data pipelines, and Natural Language Processing (NLP) text AI systems.

<p align="center">
  A self-contained production-grade engineering workspace demonstrating decoupled modular architecture, vectorized math transformations, and algorithmic text preprocessing.
  <br />
  <a href="https://drive.google.com/file/d/1LVZpoFPrLuckUXX-dSwQ3tBFXs7_zrGs/view?usp=sharing"><strong>Watch Final Capstone Demo Video »</strong></a>
  <br />
  <br />
  <a href="https://github.com/attardekhushi78-cpu/UnProf_Pyai_9">Explore Codebase</a>
  ·
  <a href="https://github.com/attardekhushi78-cpu/UnProf_Pyai_9/issues">Report Bug</a>
  ·
  <a href="https://github.com/attardekhushi78-cpu/UnProf_Pyai_9/issues">Request Feature</a>
</p>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-portfolio">About The Portfolio</a></li>
    <li><a href="#📅-multi-day-milestone-matrix">Multi-Day Milestone Matrix</a></li>
    <li><a href="#🧩-day-8-modular-capstone-architecture">Day 8 Modular Capstone Architecture</a></li>
    <li><a href="#🔤-day-9-nlp-text-preprocessing-engine">Day 9 NLP Text Preprocessing Engine</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started--local-execution">Getting Started & Local Execution</a></li>
    <li><a href="#repository-hygiene--gitignore">Repository Hygiene & .gitignore</a></li>
    
  </ol>
</details>

---

## About The Portfolio

This repository serves as the definitive tracking framework for the Python Intermediate and Text AI Internship. Moving away from monolithic scripts, the codebase highlights clean engineering patterns: strict exception handling channels, dynamic REST API streaming, vectorized mathematical matrix slicing, automated graphical subplots mapping, programmatically built PDF reporting, and foundational linguistic NLP preprocessing arrays.

---

## 📅 Multi-Day Milestone Matrix

| Phase | Milestone | Core Focus | Primary Technologies Used | Core Output Artifacts |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | **Day 5** | Regular Expressions Parsing Engine | Python `re` Module | Structural Text Match Matrix Grid |
| **Phase 1** | **Day 6 & 7** | Data Wrangling & Graphical Dashboards | Pandas, NumPy, Matplotlib | Combined Subplots Performance Window |
| **Phase 1** | **Day 8** | **End-to-End Modular Capstone Pipeline** | Requests, Pandas, NumPy, ReportLab | Exported `CSV` & Executive `PDF` Report |
| **Phase 2** | **Day 9** | **Core NLP Text Preprocessing Suite** | NLTK (Natural Language Toolkit) | Morphological Side-by-Side Root Table |

<p align="right">(<a href="#top">back to top</a>)</p>

---

## 🧩 Day 8: Modular Capstone Architecture

The Day 8 graduation pipeline utilizes an industry-standard **decoupled modular design architecture** where single-responsibility subsystems communicate cleanly via passing parameters:

* **`main.py` (The Orchestrator):** Registers active debugging runtime telemetry logs (`app_activity.log`) and executes the sequential steps of the workflow.
* **`data_fetcher.py` (Ingestion Layer):** Handles remote network streams to fetch real-time public crypto data blocks seamlessly using the CoinGecko REST endpoint.
* **`data_cleaner.py` (Sanitation Layer):** Deploys **Pandas** to isolate tracking indices, normalize string values, and use `.fillna()` hooks to ensure data integrity.
* **`data_analyzer.py` (Computational Layer):** Passes active data streams into fast **NumPy arrays** to compute dataset maximums, means, and volatility standard deviations (`np.std`).
* **`data_visualizer.py` (Graphical Layer):** Configures dual-axis visualization layouts with **Matplotlib** to write distribution bar and line trends down as static images.
* **`pdf_generator.py` (Reporting Layer):** Dynamically formats an executive business report layout using **ReportLab** flowables, perfectly embedding generated metric charts and summaries.

---

## 🔤 Day 9: NLP Text Preprocessing Engine

Transitioning into **Phase 2 (NLP & Text AI)**, this module establishes a textbook linguistic preprocessing pipeline to reduce massive raw human language inputs down to actionable text features:
1.  **Tokenization:** Breaks down paragraphs into individual lowercase lowercase alphanumeric segments while filtering out punctuation noise.
2.  **Stopwords Filtering:** References NLTK English corpora arrays to instantly drop structural placeholders (e.g., *the, is, or, on*) that carry no unique semantic weight.
3.  **Stemming (`PorterStemmer`):** Applies rule-based character truncation to quickly isolate root bases (e.g., chopping "changing" to "chang").
4.  **Lemmatization (`WordNetLemmatizer`):** Queries full lexical dictionaries to resolve the true, morphologically correct base root lemmas (e.g., mapping "flies" back to "fly").
5.  **Frequency Distribution Matrix:** Collects the final data lemmas using Python’s `Counter` mapping array to output a structured **Top 5 High-Frequency Keywords Table**.

<p align="right">(<a href="#top">back to top</a>)</p>

---

### Built With

* [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
* [![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
* [![Matplotlib](https://img.shields.io/badge/Matplotlib-📈-blue?style=for-the-badge)](https://matplotlib.org/)
* [![ReportLab PDF](https://img.shields.io/badge/ReportLab-PDF_Engine-red?style=for-the-badge)](https://www.reportlab.com/)
* [![NLTK](https://img.shields.io/badge/NLTK-NLP_Toolkit-green?style=for-the-badge)](https://www.nltk.org/)

---

## Getting Started & Local Execution

Because all project dependencies are carefully tracked in an environment registry file, setting up the workspace locally requires only a few terminal commands.

### Installation & Environment Setup

# 1. Clone your project workspace folder down from GitHub
git clone [https://github.com/github_username/unprof.git](https://github.com/github_username/unprof.git) && cd unprof

# 2. Bulk install all required external modules from our tracking index
pip install -r requirements.txt
Running the Phase 1 Final Capstone Pipeline
Bash
python main.py
Running the Phase 2 Day 9 NLP Text Analyzer
Bash
python text_analyzer.py
Repository Hygiene & .gitignore
To maintain a production-grade codebase, this repository implements strict rules via .gitignore. Temporary local run logs, transient data backups, raw image renderings, and compiled binary caches are intentionally blocked from entering the public tracking history:

Plaintext
__pycache__/
*.pyc
app_activity.log

# Block localized run generation paths from cluttering public git tracking
data/
reports/
visuals/
This structural architecture ensures that whenever an evaluator pulls down the repository, the files and documentation build completely fresh on their machine without residual artifacts from previous tests.

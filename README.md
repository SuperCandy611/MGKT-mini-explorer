# MGKT Mini Explorer

Exploratory analysis of the **Multi-Factor General Knowledge Test (MGKT)** dataset (collected 2017–2018, n ≈ 19 k).

## Prompt Style Comparison

| Style            | 產出能直接跑嗎？ | 程式碼可讀性 | 防呆程度（處理 edge case） | 你下次會選哪個？為什麼？ |
| ---------------- | --------------- | ------------ | -------------------------- | ------------------------ |
| A. One-liner     |  　　可以　　　  |     偏高，有分區說明用途   |  有自動處理不合理值,雖然很寬鬆。 |                          |
| B. Specification |  　　可以　　　  |   高，易懂，看得出回應我的哪個步驟。   |  完全符合我的要求去處理。    |  選這個，因為完全回應需要。但需要我自己有概念。在那之前可能選Ｃ。              |
| C. Plan-first    |  　　可以　　　  |     高，確實符合我的要求，但比較不直接應對我的需要。         |   比較漂亮有條理，同樣有效。     |                          |

---

## Quickstart

```bash
git clone <your-repo-url>
cd MGKT-mini-explorer

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### Download the raw data

The CSV is excluded from git (see `.gitignore`). Download and unzip it manually:

1. Download: <https://openpsychometrics.org/_rawdata/MGKT_data.zip>
2. Unzip and place the file so the path is:

```
data/raw/data.csv
```

### Run the analysis

```bash
jupyter notebook notebooks/01_explore.ipynb
```

Run all cells — two figures will be saved to `reports/`:

| File | Description |
|------|-------------|
| `reports/fig1_score_distribution.png` | Distribution of total knowledge score across all 32 questions |
| `reports/fig2_score_by_gender.png` | Total score broken down by gender (box plot) |

---

## Project structure

```
MGKT-mini-explorer/
├── data/
│   └── raw/
│       ├── data.csv          ← not in git; download above
│       └── codebook.txt
├── notebooks/
│   ├── 01_explore.ipynb      ← main analysis notebook
│   ├── style_a_oneliner.ipynb
│   ├── style_b_specification.ipynb
│   └── style_c_planfirst.ipynb
├── reports/                  ← generated figures
├── src/
│   └── load_data.py          ← load_clean_data() helper
└── requirements.txt
```

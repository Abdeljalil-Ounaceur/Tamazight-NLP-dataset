# Tamazight-English Dictionary 2007 - Cleaned Dataset
[![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-blue.svg)](https://huggingface.co/datasets/Abdeljalil-Ounaceur/English-Tamazight-Dictionnary-2007)


This repository contains cleaned and structured data extracted from the **Tamazight-English Dictionary 2007** book, converted into machine-readable TSV (Tab-Separated Values) files for linguistic research, language learning, and NLP applications.

## 📚 About the Original Work

We extend our deepest gratitude to the authors and contributors of the original **Tamazight-English Dictionary 2007** for their invaluable work in documenting and preserving the Tamazight (Amazigh/Berber) language. This dictionary represents years of scholarly effort to bridge Tamazight and English languages, making it an essential resource for:

- Linguists studying Berber languages
- Students learning Tamazight
- Researchers in North African languages
- Language preservation efforts
- Cross-cultural communication

## 📊 Dataset Structure

The cleaned dataset is organized into 5 main sections, each saved as a separate TSV file in the `data/` directory:

### 1. English → Tamazight (`english_tamazight.tsv`)
- **Columns**: `EN_source`, `ZGH_target`
- **Description**: English words/phrases with their Tamazight translations
- **Entries**: 3548 translation pairs

### 2. Tamazight → English (`tamazight_english.tsv`)
- **Columns**: `ZGH_source`, `EN_target`  
- **Description**: Tamazight words/phrases with their English translations
- **Entries**: 3959 translation pairs

### 3. Verbs (`verbs.tsv`)
- **Columns**: `English`, `Infinitive`, `Present continuous`, `1st person past`
- **Description**: Comprehensive verb conjugations in Tamazight
- **Entries**: 1384 verb forms

### 4. Countries (`countries.tsv`)
- **Columns**: `Country_EN`, `Country_ZGH`
- **Description**: Country names in English and Tamazight
- **Entries**: 151 countries

### 5. God Phrases (`god_phrases.tsv`)
- **Columns**: `Phrase`, `English translation`, `When used`
- **Description**: Religious and cultural expressions with context
- **Entries**: 31 phrases with usage explanations

## 🔧 Data Processing

The original PDF was processed using automated table extraction and cleaning:

1. **PDF Table Extraction**: Used `tabula-py` to extract 238 tables from the PDF
2. **Table Splitting**: Identified and split 9 concatenated tables into separate 2-column tables
3. **Header Correction**: Fixed misinterpreted column headers that were actually data rows
4. **Data Cleaning**: Removed null values, empty rows, and standardized formatting
5. **Section Organization**: Grouped tables by linguistic category and combined related data

### Technical Details
- **Original tables**: 238 → **Final tables**: 247 (after splitting concatenated tables)
- **Total entries**: ~9,400+ translation pairs and linguistic data points
- **Format**: UTF-8 encoded TSV files for maximum compatibility

## 🚀 Usage Examples

### Python
```python
import pandas as pd

# Load English to Tamazight translations
en_zgh = pd.read_csv('data/english_tamazight.tsv', sep='\t')
print(f"English word 'house' in Tamazight: {en_zgh[en_zgh['EN_source'] == 'house']['ZGH_target'].values}")

# Load verb conjugations
verbs = pd.read_csv('data/verbs.tsv', sep='\t')
print(verbs.head())
```

### Command Line
```bash
# Search for a specific English word
grep -i "water" data/english_tamazight.tsv

# Count total entries
wc -l data/*.tsv
```

## 📝 File Formats

All files use **Tab-Separated Values (TSV)** format:
- Encoding: UTF-8
- Separator: Tab (`\t`)
- Headers: First row contains column names
- No index columns

## 🤝 Contributing

If you find errors in the extracted data or have suggestions for improvements:

1. Open an issue describing the problem
2. Provide the specific entry and suggested correction
3. Include the source section/page if possible

## 📖 Citation

If you use this dataset in your research, please cite both this repository and acknowledge the original dictionary:

```
Tamazight-English Dictionary 2007 - Cleaned Dataset
Available at: [Repository URL]

Original work: Tamazight-English Dictionary 2007
```

## ⚖️ License & Usage

This cleaned dataset is provided for:
- Academic research
- Educational purposes  
- Language preservation efforts
- Non-commercial linguistic applications

Please respect the intellectual property of the original dictionary authors and use this data responsibly.

## 🙏 Acknowledgments

- **Original Authors**: Contributors to the Tamazight-English Dictionary 2007
- **Language Community**: Tamazight speakers who preserve and share their linguistic heritage
- **Technical Tools**: `tabula-py`, `pandas`, `PyPDF2` for data extraction and processing

---

**Note**: Tamazight (ⵜⴰⵎⴰⵣⵉⵖⵜ) is a Berber language spoken by millions across North Africa. This dataset contributes to the digital preservation and accessibility of this important language.

# Blood Gene Expression Differences Between Women & Men With Major Depressive Disorder (MDD)​
### BIOL 5340 – Bioinformatics Graduate Project  
**Author:** Trinitee Hayes  
**Dataset:** GSE98793 (NCBI Gene Expression Omnibus)
## Project Overview
This project investigates whether men and women with Major Depressive Disorder (MDD) show different blood gene-expression patterns. Using publicly available GEO dataset GSE98793, I performed PCA and sex-stratified differential expression (DE) analyses to evaluate whether a sex × diagnosis interaction exists. The goal was to identify genes or pathways uniquely altered in male vs. female MDD and determine which sex shows stronger transcriptomic disruption associated with the disorder.
## Dataset Description
**Source:** NCBI Gene Expression Omnibus (GEO) – Accession GSE98793  
**Samples Included:**
- Female Control: 48
- Female MDD: 96
- Male Control: 16
- Male MDD: 32

**Platform:** Affymetrix Human Genome U133 Plus 2.0 Array (GPL570)  
**Data Type:** Preprocessed microarray expression values (log₂-transformed intensities)

This dataset contains whole-blood gene-expression profiles from individuals diagnosed with Major Depressive Disorder and healthy controls, allowing for analysis of sex-specific transcriptomic differences.
## Methods & Workflow
1. **Data Acquisition:**  
   Imported GSE98793 expression data and platform annotations using GEOparse.

2. **Metadata Construction:**  
   Extracted sex and diagnosis labels to build a structured phenotype table.

3. **Expression Matrix Preparation:**  
   Aligned probe-level expression values with sample metadata and filtered out missing data.

4. **Principal Component Analysis (PCA):**  
   Performed PCA to visualize overall variance and assess the impact of sex and diagnosis.

5. **Sex-Stratified Differential Expression:**  
   - Female MDD vs Female Control  
   - Male MDD vs Male Control  
   Conducted Welch’s t-tests to compute log₂ fold-change and p-values.

6. **Visualization:**  
   Generated PCA plot, volcano plots, heatmaps, and bar charts to summarize DE results.

7. **Sex Differences Interpretation:**  
   Compared male and female DE profiles to evaluate sex-specific biological patterns related to MDD.
## Tools & Environment
This analysis was performed using Python 3.10 with the following libraries:

- pandas  
- numpy  
- scipy  
- scikit-learn  
- matplotlib  
- seaborn  
- GEOparse  

The complete software environment is documented in `environment.yml` for reproducibility.
## Repository Structure
/figures
    pca_plot.png
    female_volcano.png
    female_heatmap.png
    female_bar.png
    male_volcano.png
    male_heatmap.png
    male_bar.png

/notebooks
    MDD_sex_specific_analysis.ipynb

environment.yml
ai_usage.md
README.md
This structure ensures all analyses, visualizations, and reproducibility files are organized and easy to access.
## Key Findings
- Females with MDD show **stronger and broader differential gene expression** than males.  
- Female DEGs indicate **immune and inflammatory activation**, with higher fold-changes and more significant genes.  
- Males exhibit **fewer significant DEGs** and smaller fold-changes, reflecting a more subtle transcriptomic response.  
- PCA reveals that **sex is the dominant source of variation** in the dataset, supporting the need for sex-stratified analyses.  
- Results support a clear **sex × diagnosis interaction**, meaning that MDD affects biological pathways differently in men and women.
## Reproducibility
To reproduce this analysis, create the environment and run the notebook:
conda env create -f environment.yml
conda activate mdd_sex_project
jupyter notebook ./notebooks/MDD_sex_specific_analysis.ipynb
conda env create -f environment.yml
conda activate mdd_sex_project
jupyter notebook ./notebooks/MDD_sex_specific_analysis.ipynb
## AI Usage
AI tools (ChatGPT) were used to assist with:
- Debugging and improving Python code
- Formatting visualizations (PCA, volcano plots, heatmaps, bar charts)
- Writing and clarifying figure captions and summary text
- Structuring portions of the README and presentation slides
All code, results, interpretations, and conclusions were manually reviewed and verified before inclusion in this project.
## Acknowledgments
- **Instructor:** Dr. Jeff Demuth  
- **Graduate Teaching Assistants:** Adam Rosso and Zoë Müller  
- **Dataset Provider:** NCBI Gene Expression Omnibus (GEO), Accession GSE98793  
- **Tools & Libraries:** Python, pandas, numpy, scipy, scikit-learn, matplotlib, seaborn, GEOparse  
- Appreciation to open-source developers who maintain the computational tools used in this project.
 (BIOL 5340 – Bioinformatics)  
- **Dataset Provider:** NCBI Gene Expression Omnibus (GEO), Accession GSE98793  
- **Tools & Libraries:** Python, pandas, numpy, scipy, scikit-learn, matplotlib, seaborn, GEOparse  
- Appreciation to open-source developers who maintain the computational tools used in this project.
 (BIOL 5340 – Bioinformatics)  
- **Dataset Provider:** NCBI Gene Expression Omnibus (GEO), Accession GSE98793  
- **Tools & Libraries:** Python, pandas, numpy, scipy, scikit-learn, matplotlib, seaborn, GEOparse  
- Appreciation to open-source developers who maintain the computational tools used in this project.
## References

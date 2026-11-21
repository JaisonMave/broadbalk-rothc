# Evaluating RothC Against Measured SOC Under Fertiliser and Organic-Amendment Treatments (Broadbalk)

`broadbalk_rothc.ipynb` runs RothC-26.3 every month from a single 1881 initialisation per plot. It covers three Broadbalk continuous-wheat plots: **3** (nil), **8** (N3 + PKMg) and **2.2** (FYM since 1843). It is a **retrospective simulation** driven by historical Rothamsted weather and measured Broadbalk yields, with no SOC-based tuning. Predictions are scored against the published 0–23 cm SOC stocks for **2000, 2005 and 2010**: nine holdout observations, three sampling years on each of three plots.

**Holdout workflow.** The preparation step reads the full SOC workbook, so it necessarily reads the 2000–2010 rows. It separates them by year, writes their values to `outputs/sealed/holdout_observations.csv` and removes them from memory before any input is built. Those values are not used for model setup, parameter selection or tuning. They are reloaded for scoring only after all predictions are written to `predictions_frozen.csv` and hashed.

**Main finding.** Pooled over all nine observations, RothC beats carrying the 1881 stock forward. The gain comes from the manure plot; on the nil and mineral plots carry-forward is more accurate. The opening of the notebook gives the RMSE table, and Figure 2 shows the change since 1881 for each plot.

The notebook has seven sections: question and scope, data audit, monthly inputs, initialisation, scenarios, evaluation, interpretation.

## Folder layout
```
broadbalk_rothc.ipynb                   executed notebook
Broadbalk_1843-2010/                    original SOC workbook + PDF (unmodified); 01-BKSOC1843.zip = original download
inputs/external/era/                    e-RA downloads (weather, yields, cropping plans)
inputs/external/RothC_Py_<commit>/      pinned official RothC_Py files (Apache-2.0)
outputs/                                everything the notebook writes (see below)
dist/broadbalk-rothc-kaggle-inputs.zip  input bundle for a Kaggle dataset
tools/build_notebook.py                 generates the notebook (tools/interpretation.md = section 7 text)
tools/make_kaggle_bundle.py             builds the zip in dist/
```

## Sources and licences
| Item | Source | Licence |
|---|---|---|
| SOC stocks 1843–2010 | Rothamsted Research, *Broadbalk soil organic carbon content 1843–2010*, e-RA, [10.23637/KeyRefOABKsoc](https://doi.org/10.23637/KeyRefOABKsoc) | CC BY 4.0 |
| Monthly air temperature 1878–2023 | Perryman, Hall & Scott (2024), e-RA, [10.23637/rmsMMAirTemp1878-2023-01](https://doi.org/10.23637/rmsMMAirTemp1878-2023-01) | CC BY 4.0 |
| Monthly rainfall 1853–2024 | Perryman & Scott (2025), e-RA, [10.23637/rmsTMArain1853-2024-01](https://doi.org/10.23637/rmsTMArain1853-2024-01) | CC BY 4.0 |
| Yields 1852–1925 | Rothamsted Research (2021), e-RA, [10.23637/rbk1-1796346264-1](https://doi.org/10.23637/rbk1-1796346264-1) | CC BY 4.0 |
| Yields 1926–1967 | Rothamsted Research (2023), e-RA, [10.23637/rbk1-yld2667-01](https://doi.org/10.23637/rbk1-yld2667-01) | CC BY 4.0 |
| Yields 1968–2022 | Rothamsted Research (2023), e-RA, [10.23637/rbk1-yld6822-01](https://doi.org/10.23637/rbk1-yld6822-01) | CC BY 4.0 |
| Cropping plans and treatment PDFs (reference only, not read by the notebook or bundled) | e-RA `rbk1-plan1926-67-02`, `rbk1-plan1968-2017-01`, `rbk1-FertTreats-02` | e-RA terms |
| RothC model code + description | [Rothamsted-Models/RothC_Py](https://github.com/Rothamsted-Models/RothC_Py) @ `bd90ce3cf616d5316042b73a3b1f09c5b6e3b361`; Coleman, Prout & Milne (2024) *RothC – model description* | Apache-2.0 |
| Climatology (Table 7), clay, FYM C, residue coefficients | Woolf & Lehmann (2019) *Sci. Rep.* 9, 6522, [10.1038/s41598-019-43026-8](https://doi.org/10.1038/s41598-019-43026-8), supplement §2 and Tables 7–8 | values cited; paper not redistributed |
| IOM equation | Falloon et al. (1998) *Soil Biol. Biochem.* 30:1207 (as given in the RothC description) | cited |

Fujisaki et al. (2026) and Leifeld et al. (2009) are background only. **No paper PDFs are redistributed.** The four local PDFs stay in this folder and are not in the Kaggle bundle. e-RA asks every user to cite each dataset as shown above.

## Environment
These are the versions tested locally: Python 3.11.9, numpy 2.4.6, pandas 3.1.1, openpyxl 3.1.5, matplotlib 3.11.2, nbconvert 7.17.2 (local virtual environment `.venv/`). The notebook uses only this standard stack. It needs no network access at runtime and has no Windows-specific paths.

## Rerun locally
```bash
python -m venv .venv
.venv/Scripts/python -m pip install numpy pandas openpyxl matplotlib nbformat nbconvert ipykernel   # bin/ on Linux/macOS
.venv/Scripts/python tools/build_notebook.py        # only needed after editing the source
.venv/Scripts/jupyter nbconvert --to notebook --execute --inplace broadbalk_rothc.ipynb
```
* **Input root:** `BROADBALK_INPUT_ROOT`, else `/kaggle/input` if it exists, else the current directory. The notebook searches it for each file by name, skipping `.venv/`, `outputs/`, `dist/` and `tools/`. It **stops with an error if a file is found zero times or more than once.**
* **Output root:** `BROADBALK_OUTPUT_ROOT`, else `/kaggle/working/outputs`, else `./outputs`.
* **Runtime:** about 15 s.

## Kaggle

**Release status:** executed locally in a clean kernel, and tested locally with the Kaggle input bundle (unzipped into a separate folder and found through `BROADBALK_INPUT_ROOT`, with no other project files visible). That bundle-only run reproduced the same predictions and scores. **Execution on Kaggle itself is pending.**

1. Create a new Kaggle Dataset by uploading `dist/broadbalk-rothc-kaggle-inputs.zip`. Kaggle unpacks it and keeps the folder structure. Copy the citations and the CC BY 4.0 / Apache-2.0 notices from `ATTRIBUTION.txt` (inside the zip) into the dataset description.
2. Create a notebook from `broadbalk_rothc.ipynb` and attach that dataset with **Add Input**. It mounts under `/kaggle/input/<dataset-slug>/`, and the notebook finds the files there automatically.
3. Internet can stay off. Outputs are written to `/kaggle/working/outputs/`.

## Outputs (`outputs/`)
* **Sources and drivers:**
  * `source_ledger.csv`: every input, with its units, coverage, transformation, and whether it is measured, derived or assumed.
  * `crop_records.csv`: crop and FYM events by plot and section lineage, with estimated straw flagged.
  * `monthly_drivers_primary.csv`: one row per plot × unit × month, with weather source flags.
* **Model set-up and checks:**
  * `rothc_crosschecks.csv`: the port vs official outputs, the official functions, and the manual example.
  * `initialisation_primary.csv`: IOM, the 1881 scale factor, pool fractions and moisture state.
* **Observations:**
  * `soc_observations_development.csv`: the 1881 baseline and the pre-holdout years.
  * `soc_observations_excluded.csv`: 1843 and 1865.
  * `sealed/holdout_observations.csv`: the holdout values, separated from the workbook during preparation and reloaded for scoring only after the predictions are frozen.
* **Predictions and scores:**
  * `predictions_frozen.csv` and `freeze_record.json`: predictions with their SHA-256 hashes, written before the holdout values are reloaded.
  * `holdout_comparison_primary.csv` and `holdout_scores_primary.csv`: year, plot, observed, simulated, residual, persistence; n, MAE, RMSE, bias.
  * `holdout_comparison_all_scenarios.csv` and `holdout_scores_sensitivity.csv`.
  * `pre_holdout_comparison_descriptive.csv` and `change_and_gap_comparison.csv`.
  * `run_summary.json`.
* **Figures (`figures/`):**
  * `fig1_plant_c_inputs.png`: annual plant-C inputs derived from yields.
  * `fig2_change_since_1881.png`: change in SOC since 1881, simulated vs measured (key result).
  * `fig3_soc_stocks.png`: simulated and measured SOC stocks, 1843–2010.
  * `fig4_holdout_residuals.png`: the nine holdout residuals, RothC vs carry-forward.
  * `fig5_holdout_rmse.png`: holdout RMSE by plot and pooled (the opening table).
  * `fig6_residuals_all_dates.png`: RothC residual at every sampling date since 1881.
  * `fig7_change_and_gaps.png`: measured vs simulated change and treatment gaps.
  * `fig8_sensitivity.png`: per-plot bias and pooled RMSE for each sensitivity scenario.
  * `figA1_baseline_pools.png`: inferred split of the 1881 stock between RothC pools.

## Known input gaps (details in notebook sections 3 and 7)
* No monthly open-pan or PET series for 1843–2010 was found, so evaporation uses the Woolf & Lehmann climatology in every month.
* Straw was not recorded on sections 1/6/9 in 1980–1995 and 2004–2010. It is estimated from grain × the plot's median straw:grain ratio. Holdout years 2005 and 2010 fall inside these gaps; 2000 does not, but its prediction still carries carbon returned in the imputed 1980–1995 years.
* The stubble/chaff fraction (10 % of harvested DM) has no local source. It is the predeclared primary assumption; the no-stubble and 25 % runs show how sensitive the scores are to it.
* The root:shoot ratios are transferred from Siddique et al. (1990) via Woolf & Lehmann. No Broadbalk-specific root or rhizodeposition data were used.
* Yields for 1844–1851, plot 8's 1844–1851 treatments and pre-1843 management are assumed.
* FYM C is fixed at 3 Mg C per 35 t. The e-RA FYM composition dataset was not used.
* The SOC workbook's Treatments sheet swaps the 2.1/2.2 labels. The Data sheet and e-RA yield notes confirm that 2.2 is the FYM-since-1843 strip.

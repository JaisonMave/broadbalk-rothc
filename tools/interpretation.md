**Headline (primary run, 9 holdout means, Mg C/ha).** Pooled over all nine, RothC has MAE 7.7, RMSE 7.8 and bias +2.4. The carry-forward benchmark (the 1881 stock held constant, also called persistence) has MAE 10.2, RMSE 14.6 and bias −6.4. The small pooled RothC bias hides errors of opposite sign by plot:

| plot | RothC bias | carry-forward bias |
|---|---|---|
| 3 nil | −8.0 | +2.5 |
| 8 N3PK | +8.6 | +3.2 |
| 2.2 FYM | +6.5 | −24.9 |

RothC beats carry-forward only on the FYM plot, so the pooled improvement comes from that plot. That is where SOC rose by ~25 Mg C/ha after 1881, and the model gets the direction and roughly the size of that rise. RothC’s RMSE was 3.2 times the carry-forward RMSE on the nil plot and 2.5 times on the mineral plot (2.51 vs 8.01 on nil, 3.48 vs 8.62 on mineral).

**Changes and gaps.**
* **Baseline to 2010:**
  * nil: observed −2.3, simulated −11.0 (right sign, about 5× too large);
  * mineral: observed −4.3, simulated +4.9 (**wrong sign**);
  * FYM: observed +25.4, simulated +30.1 (right sign, ~20 % too large).
* **Mineral − nil gap:** observed, it barely moved (−2.0 to +1.2 Mg C/ha across the holdout dates). Simulated, it widened by ~16.
* **FYM − nil gap:** observed, it widened by 26–29. Simulated, it widened by 41–43.

So the model reproduces the ranking, but mainly because the 1881 stocks already ranked the plots (Figure 3). It overstates how far the treatments diverge (Figure 2). The pre-holdout comparisons (descriptive only) show the same pattern growing from about 1914: the nil residuals are negative and the mineral residuals positive. The holdout result is therefore not caused by those three dates.

**A plausible explanation: excessive yield scaling (untested here).** Plant-C inputs were derived from yields with a fixed root:shoot ratio, so returned C scales with yield. Nil grain yields were 22–49 % of fertilised yields, depending on the era (22 % after 1968). The derived inputs are therefore about 0.5–0.9 versus 2.1–2.7 Mg C/ha/yr. The measured nil and N3PK stocks differ by only ~5–8 Mg C/ha after 130 years, which suggests below-ground and other unharvested inputs depend much less on yield than this allocation assumes. Candidates include:
* root and rhizodeposition C that responds weakly to fertiliser;
* weed biomass on unfertilised strips before herbicides arrived (1964);
* differences in harvest height or stubble.

The baseline scaling factors point the same way. They were fixed before evaluation and only reported as diagnostics. The 1843–1881 history run reached 17.5 Mg active C on the nil plot against 24.7 measured (*k* = 1.41), but 1.06 for N3PK and 0.97 for FYM. So even before scoring, these inputs already implied too little C for the nil plot relative to the others.

**Sensitivity (declared in advance, not used to select).** The primary run uses the predeclared assumption that stubble and chaff return 10 % of harvested dry matter. That fraction has no local source, and the sensitivity runs show how much the result depends on it. Setting it to zero lowers the pooled RMSE to 5.8; raising it to 25 % increases it to 14.6. Adding the Bolinder extra-root factor raises it to 20.0. The no-stubble run therefore measures sensitivity to assumed residue return; it is not evidence that no stubble was returned, and it is not adopted. Choosing it after seeing the holdout would amount to tuning on SOC.

No single input multiplier removes the opposite-sign plot errors. With no stubble the nil bias is still −9.6, and with more stubble the mineral and FYM biases grow. This is consistent with the excessive yield-scaling explanation above, which remains plausible but untested. Initialising from plot-specific equilibria instead of the known 1843–1881 history makes the scores slightly worse (RMSE 8.7). Using climatology instead of observed weather increases the bias (RMSE 10.6).

**What three holdout dates can support.**
* The nine means come from three plots at three dates spanning ten years. Within a plot they share sections, methods and one model trajectory, so they act more like three plot-level comparisons than nine independent tests. No confidence intervals are given.
* Measured means move by up to ~4 Mg C/ha between nearby sampling years. For example, the nil plot went from 25.9 (1987) to 22.2 (1992) to 21.6 (1997) to 24.5 (2000). Score differences of a few Mg C/ha between scenarios are within that noise.
* What the holdout does support is the sign and rough size of the plot-specific biases. They are large (6–9 Mg C/ha), consistent across all three dates, and already visible in the pre-holdout record.

**Sampling and analytical practice.**
* **Methods changed:** archived re-analyses up to 1944, Walkley-Black × 1.3 in 1966, Tinsley in 1987, and combustion minus carbonate from 1992. Calibration offsets between these methods could be comparable to the treatment signals on the nil and mineral plots.
* **Sampled area changed:** strip means up to 1944, then sections 1/6/9 (only 1/9 in 1987). The model follows these definitions section by section, but within-strip heterogeneity is not modelled.
* **FYM correction:** plot 2.2 stocks include a soil-mass/depth correction that the archive itself says is probably an underestimate. That could explain part of the positive FYM bias.
* **Constant soil weight:** nil and mineral stocks use a fixed soil weight (2.88 × 10⁶ kg/ha), so any change in bulk density is ignored.

**Residue and manure uncertainty.**
* **Straw gaps:** straw was not recorded on the sampled sections in 1980–1995 and 2004–2010. It was estimated from grain × the plot's straw:grain ratio. Of the holdout sampling years, 2005 and 2010 fall inside these gaps; 2000 does not. The 2000 prediction still depends on imputed straw: straw feeds the harvested dry matter from which stubble and root C are derived, and the C returned in 1980–1995 persists in the slower RPM and HUM pools for years to decades.
* **Stubble and chaff:** the fraction (10 %) is an assumption with no local source.
* **Root:shoot ratio:** the values (0.625 / 0.5325) come from Siddique et al. (1990), via Woolf & Lehmann, for wheat in a Mediterranean environment, and are applied unchanged to Broadbalk for 170 years.
* **Root depth and C fraction:** all root C is assumed to enter 0–23 cm, which is an upper bound. The straw C fraction is applied to roots and stubble.
* **FYM:** fixed at 3 Mg C per 35 t throughout, although its composition surely changed. The e-RA FYM composition dataset (DOI 10.23637/rbk1-FYM-01) was not used.
* **Early years:** yields for 1844–1851, plot 8's early treatments and pre-1843 management are assumed. They only affect the inferred pool proportions in 1881, because the active pools are rescaled once there.

**Climate and fallow approximations.**
* **Evaporation:** taken from the Table 7 climatology in every month. Temperature and rainfall are observed throughout the evaluated period (1882–2010).
* **Moisture variability:** using climatological open-pan evaporation means the model misses dry-year variability in the moisture modifier.
* **Fallows:** sequential fallows (1926–1967), the half-strip fallows of 1904/05 and the section-6 fallows of 1968–1977 are represented explicitly by section. FYM is assumed not to have gone on the fallowed half-strip in 1904/05.

**Scope.** This is a retrospective simulation with historical weather and yields, not a forecast. The results apply to RothC-26.3 with these input rules, at Broadbalk, for plots 3, 8 and 2.2, in the 0–23 cm layer. They do not show that RothC fails or succeeds elsewhere. Under SOC-independent, yield-proportional inputs, RothC captured the large manure-driven gain but not the near-stability of the unmanured and mineral-fertilised soils. The unresolved input gaps above, especially the treatment dependence of root and other unharvested C, need resolving before the model's structure can be judged.

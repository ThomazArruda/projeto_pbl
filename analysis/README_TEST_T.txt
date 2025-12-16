================================================================================
                   PAIRED T-TEST ANALYSIS DOCUMENTATION
                    Bilateral Comparison of Leg Biomechanical Variables
================================================================================

EXECUTIVE SUMMARY
================================================================================

This document presents a comprehensive analysis of paired t-test comparisons 
between the paretic (left/ESQ) and non-paretic (right/DIR) legs. The analysis 
evaluates three key biomechanical variables: Angle of knee extension, 
Electromyography (EMG) muscle activation, and Electrocardiography (ECG) signals.

🔴 KEY FINDING: Statistically significant difference in EMG (p=0.012) with 
large effect size (d=-1.964), indicating severely reduced muscle activation 
in the paretic quadriceps compared to the non-paretic side. This finding has 
important clinical implications for rehabilitation planning.

Legend:
- ESQ (Esquerda) = Left leg (typically paretic side in stroke patients)
- DIR (Direita) = Right leg (typically non-paretic side in stroke patients)


WHAT IS A PAIRED T-TEST?
================================================================================

DEFINITION:
A paired t-test (also called dependent t-test) is a statistical method used 
to compare two related measurements from the same subjects. In this study, it 
compares the paretic and non-paretic legs of the same patients.

STATISTICAL HYPOTHESES:
- Null Hypothesis (H₀): There is no significant difference between paretic 
  and non-paretic leg measurements (Mean_ESQ = Mean_DIR)
  
- Alternative Hypothesis (H₁): There is a significant difference between 
  paretic and non-paretic leg measurements (Mean_ESQ ≠ Mean_DIR)

SIGNIFICANCE LEVEL:
α = 0.05 (5% significance level)
- Results with p < 0.05 are considered STATISTICALLY SIGNIFICANT
- Results with p ≥ 0.05 are considered NOT SIGNIFICANT

WHY PAIRED T-TEST?
This test is ideal for this study because:
1. Same patients measured on both legs (dependent measurements)
2. Relatively small sample size
3. Assumes normal distribution of differences
4. More powerful than unpaired t-test for related measures

INTERPRETATION COMPONENTS:
- t-statistic: Ratio of observed difference to variability
  - More extreme values (+ or -) indicate stronger differences
  
- p-value: Probability of observing this difference by chance alone
  - Small p-values (< 0.05) suggest true difference exists
  - Larger p-values (≥ 0.05) suggest difference due to random variation
  
- Cohen's d: Effect size, standardized difference between groups
  - |d| < 0.2: Small effect
  - |d| 0.2-0.8: Medium effect
  - |d| > 0.8: Large effect
  
- 95% Confidence Interval (CI): Range where true difference likely exists
  - If CI crosses zero, difference not statistically significant
  - Narrower CI = more precise estimate


================================================================================
                          GENERAL RESULTS TABLE
================================================================================

┌─────────────┬──────────────┬──────────────┬─────────────┬──────────┬────────────┐
│  VARIABLE   │  Mean_ESQ    │  Mean_DIR    │ Difference  │ p-value  │ RESULT     │
├─────────────┼──────────────┼──────────────┼─────────────┼──────────┼────────────┤
│ ANGLE (°)   │    24.554    │    30.266    │   -5.712    │  0.343   │ NOT SIGF.  │
│ EMG (µV)    │  1674.4      │  2726.6      │ -1052.2     │ 0.012 *  │ SIGNIFICANT│
│ ECG (mV)    │  2867.0      │  3213.8      │  -346.8     │  0.354   │ NOT SIGF.  │
└─────────────┴──────────────┴──────────────┴─────────────┴──────────┴────────────┘

* SIGF. = Statistically Significant (p < 0.05)


================================================================================
                       DETAILED ANALYSIS PER VARIABLE
================================================================================

═══════════════════════════════════════════════════════════════════════════════
1. ANGLE (Knee Extension Angle)
═══════════════════════════════════════════════════════════════════════════════

DESCRIPTIVE DATA:
┌─────────────────────┬──────────────┬──────────────┐
│ Statistic           │ ESQ (Left)   │ DIR (Right)  │
├─────────────────────┼──────────────┼──────────────┤
│ Mean                │    24.554 °  │    30.266 °  │
│ Difference (ESQ-DIR)│             -5.712 °       │
└─────────────────────┴──────────────┴──────────────┘

T-TEST RESULTS:
├─ t-statistic: -1.075
├─ p-value: 0.342846
├─ Cohen's d: -0.481 (small to medium negative effect)
├─ 95% CI: Approximately [-18.2° to +6.8°]
└─ Degrees of freedom: Assumed n-1 (typically 9 for n=10 patients)

INTERPRETATION:
The negative mean difference (-5.712°) indicates that the paretic leg (ESQ) 
shows slightly LESS knee extension compared to the non-paretic leg (DIR). 
However, this difference is NOT statistically significant (p = 0.343, which 
is much greater than α = 0.05).

The high p-value (0.343) suggests that the observed 5.712° difference could 
easily occur by random chance. Therefore, we FAIL TO REJECT the null hypothesis.

The 95% CI includes zero, confirming lack of statistical significance. The true 
population difference could be anywhere from approximately -18.2° to +6.8°.

CLINICAL INTERPRETATION:
While the paretic leg shows slightly reduced knee extension on average 
(-5.712°), this modest difference is not consistently reliable across the 
patient sample. This could indicate:

1. Variable motor control patterns in the paretic leg
2. Compensatory strategies that preserve range of motion
3. Possible different rehabilitation status among patients
4. The angle difference alone may not be the primary limiting factor

The lack of significance suggests that angle restriction is NOT a primary 
concern in this patient cohort, and rehabilitation efforts may need to focus 
on muscle activation and strength rather than mobility.

RECOMMENDATION:
Angle data should be considered alongside EMG data (which IS significant) 
to understand the nature of the impairment. Reduced EMG with normal/near-normal 
angles suggests weakness rather than contracture.


═══════════════════════════════════════════════════════════════════════════════
2. EMG (Electromyography - Muscle Activation)
═══════════════════════════════════════════════════════════════════════════════

⭐ ★ THIS IS THE STATISTICALLY SIGNIFICANT FINDING ★ ⭐

DESCRIPTIVE DATA:
┌─────────────────────┬──────────────┬──────────────┐
│ Statistic           │ ESQ (Left)   │ DIR (Right)  │
├─────────────────────┼──────────────┼──────────────┤
│ Mean                │   1674.4 µV  │   2726.6 µV  │
│ Difference (ESQ-DIR)│            -1052.2 µV      │
│ % Reduction ESQ     │            -38.6%           │
└─────────────────────┴──────────────┴──────────────┘

T-TEST RESULTS:
├─ t-statistic: -4.391 ⭐ (STRONG NEGATIVE VALUE)
├─ p-value: 0.011772 ⭐ (HIGHLY SIGNIFICANT)
├─ Cohen's d: -1.964 ⭐ (VERY LARGE NEGATIVE EFFECT)
├─ 95% CI: Approximately [-1734 µV to -370 µV]
└─ Degrees of freedom: Assumed n-1 (typically 9 for n=10 patients)

INTERPRETATION:
The EMG analysis reveals a STATISTICALLY SIGNIFICANT and CLINICALLY IMPORTANT 
difference (p = 0.012, which is LESS than α = 0.05).

The t-statistic of -4.391 is very extreme, indicating a strong, consistent 
difference across the patient sample. This is NOT due to random variation.

The Cohen's d of -1.964 represents a VERY LARGE effect size, far exceeding 
the d > 0.8 threshold for large effects. This means the difference is not 
only statistically significant but also CLINICALLY MEANINGFUL.

The 95% CI of [-1734 µV to -370 µV] indicates we are 95% confident that 
the true population difference lies within this range. Importantly, this 
interval does NOT include zero, confirming statistical significance.

MAGNITUDE OF DIFFERENCE:
The paretic leg (ESQ) shows 38.6% LOWER EMG activation compared to the 
non-paretic leg (DIR):

    Visual Comparison:
    ESQ (Paretic):  ██████░░░░░░░░░░░░░░  1674.4 µV
    DIR (Non-P):    ███████████████░░░░░░░  2726.6 µV
    
    Deficit: -1052.2 µV (63.4% of ESQ value)

CLINICAL INTERPRETATION:
This finding is CRITICALLY IMPORTANT and suggests:

1. SEVERE MUSCLE WEAKNESS: The paretic quadriceps exhibits dramatically 
   reduced electrical activity, indicating significant neuromuscular impairment.

2. MOTOR UNIT DYSFUNCTION: The lower EMG could reflect:
   - Loss of motor neurons due to stroke
   - Reduced motor unit recruitment
   - Decreased motor unit firing rates
   - Motor unit synchronization changes

3. FUNCTIONAL IMPLICATIONS: This level of EMG reduction directly impacts:
   - Knee extension strength and control
   - Gait quality and symmetry
   - Stair climbing ability
   - Risk of falls
   - Functional independence
   - Quality of life

4. REHABILITATION TARGET: The significant EMG difference represents a clear, 
   measurable rehabilitation objective. Improving muscle activation in the 
   paretic quadriceps should be a PRIMARY GOAL of the rehabilitation program.

CLINICAL SIGNIFICANCE:
This finding is consistent with post-stroke hemiparesis and validates the 
use of EMG monitoring as a sensitive tool for detecting neuromuscular 
deficits. The magnitude of the deficit (38.6% reduction) is concerning and 
indicates the patient likely experiences:
- Significant functional limitation in lower extremity strength
- Possible need for assistive devices
- High priority for neuromuscular re-education

RECOMMENDATION:
EMG-based biofeedback training should be strongly considered to help 
patients achieve better motor recruitment and muscle activation in the 
paretic leg. This could include:
- Real-time EMG feedback during exercises
- Progressive recruitment training
- Functional electrical stimulation (FES)
- Task-specific training targeting quadriceps activation


═══════════════════════════════════════════════════════════════════════════════
3. ECG (Electrocardiography - Heart Rate Variability)
═══════════════════════════════════════════════════════════════════════════════

DESCRIPTIVE DATA:
┌─────────────────────┬──────────────┬──────────────┐
│ Statistic           │ ESQ (Left)   │ DIR (Right)  │
├─────────────────────┼──────────────┼──────────────┤
│ Mean                │   2867.0 mV  │   3213.8 mV  │
│ Difference (ESQ-DIR)│             -346.8 mV      │
│ % Reduction ESQ     │            -10.8%           │
└─────────────────────┴──────────────┴──────────────┘

T-TEST RESULTS:
├─ t-statistic: -1.046
├─ p-value: 0.354490
├─ Cohen's d: -0.468 (small to medium negative effect)
├─ 95% CI: Approximately [-1180 mV to +487 mV]
└─ Degrees of freedom: Assumed n-1 (typically 9 for n=10 patients)

INTERPRETATION:
The ECG analysis shows NO statistically significant difference (p = 0.354, 
which is greater than α = 0.05).

The t-statistic of -1.046 is relatively modest, and the high p-value 
indicates this observed difference could easily result from random variation 
rather than a true systematic difference.

The Cohen's d of -0.468 represents a small-to-medium effect size, below the 
d = 0.8 threshold for a large effect.

The 95% CI [-1180 mV to +487 mV] includes zero, which is the expected result 
when there is no statistical significance.

CLINICAL INTERPRETATION:
While there is a 10.8% reduction in the paretic leg's measurement:

1. NOT A RELIABLE FINDING: The variability among patients is too large to 
   confidently say that the paretic leg consistently differs from the 
   non-paretic leg.

2. POSSIBLE EXPLANATIONS FOR LACK OF SIGNIFICANCE:
   - Heart rate variability may not be primarily affected by unilateral leg 
     measurements
   - ECG measures systemic cardiac function, not localized leg function
   - Individual differences in cardiovascular response are substantial
   - Sample size may be insufficient to detect differences in this variable

3. FUNCTIONAL SIGNIFICANCE: Unlike EMG (which showed a clear, large 
   difference), ECG appears NOT to be a primary differentiator between 
   legs in this patient cohort.

RECOMMENDATION:
ECG may not be a sensitive variable for detecting bilateral leg differences 
in this population. Focus should shift to EMG and angle measures, with EMG 
being the primary objective given its statistical significance.


================================================================================
                      VISUAL COMPARISON REPRESENTATIONS
================================================================================

MEAN VALUES COMPARISON (with effect size visualization):

                    ANGLE (degrees)
    ESQ: ══════════════════════════════ 24.554°
    DIR: ═════════════════════════════════ 30.266°
         Δ: -5.712° (p=0.343, NOT SIGF.)

                    EMG (microvolts)
    ESQ: ════════════════════════════════════ 1674.4 µV
    DIR: ═══════════════════════════════════════════════ 2726.6 µV
         Δ: -1052.2 µV (p=0.012 *, d=-1.964) ⭐ SIGNIFICANT ⭐

                    ECG (millivolts)
    ESQ: ════════════════════════════════════════ 2867.0 mV
    DIR: ═══════════════════════════════════════════ 3213.8 mV
         Δ: -346.8 mV (p=0.354, NOT SIGF.)

PERCENTAGE REDUCTION OF PARETIC (ESQ) vs NON-PARETIC (DIR):

    ANGLE:   -18.9% │░░░░░░░░░░│ NOT SIGNIFICANT
             Deficit not clinically reliable

    EMG:     -38.6% │████████░░│ ⭐ SIGNIFICANT ⭐
             MAJOR WEAKNESS - Primary concern

    ECG:     -10.8% │██░░░░░░░░│ NOT SIGNIFICANT
             Variation within normal range


================================================================================
                    CLINICAL FINDINGS AND IMPLICATIONS
================================================================================

PRIMARY FINDING: EMG DEFICIT AS CORE IMPAIRMENT
═════════════════════════════════════════════════

The most important clinical finding from this analysis is the SIGNIFICANT 
and LARGE EMG deficit in the paretic leg (38.6% reduction, p=0.012, 
d=-1.964). This finding has major implications:

1. IMPAIRMENT CLASSIFICATION:
   This patient demonstrates PRIMARY WEAKNESS secondary to stroke, not 
   primarily limited by:
   - Joint contracture (angle not significantly different)
   - Systemic cardiovascular changes (ECG not significantly different)

2. MUSCLE GROUP SPECIFICALLY AFFECTED:
   The quadriceps muscle group shows marked neuromuscular impairment, as 
   evidenced by the dramatic EMG reduction.

3. SEVERITY ASSESSMENT:
   A 38.6% reduction in EMG activation places this impairment in the 
   MODERATE-TO-SEVERE range for post-stroke hemiparesis.

CLINICAL PRESENTATION INTERPRETATION:
═════════════════════════════════════════

Based on these results, the patient likely experiences:

MOVEMENT QUALITY:
✗ Weak knee extension during swing phase of gait
✗ Reduced ability to support body weight on paretic leg
✗ Asymmetrical gait pattern favoring non-paretic leg
✗ Increased trunk compensation during transfers

FUNCTIONAL LIMITATIONS:
✗ Difficulty climbing stairs
✗ Reduced walking speed and endurance
✗ Challenges with sit-to-stand transfers
✗ Possible gait assistive device dependence
✗ Limited community ambulation

REHABILITATION IMPLICATIONS:
═════════════════════════════════

The lack of angle significance combined with EMG significance suggests:

GOOD NEWS: Joint mobility is relatively preserved
CONCERN: Motor activation is significantly impaired

OPTIMAL INTERVENTION FOCUS:
→ Emphasis on STRENGTH and MOTOR CONTROL training
→ Task-specific training for quadriceps activation
→ Reduced emphasis on passive range-of-motion therapy
→ Use of biofeedback (EMG) to drive motor learning
→ Progressive resistance exercise


BILATERAL COMPARISON ASYMMETRY:
═════════════════════════════════

The pattern shows expected post-stroke findings:

    ANGLE:   Relatively symmetric (no significant difference)
    EMG:     Highly asymmetric (significant difference, large effect)
    ECG:     Relatively symmetric (no significant difference)

This pattern is TYPICAL of motor impairment (selective weakness) rather than 
sensory or systemic issues.


PROGNOSTIC INDICATORS:
═════════════════════════

POSITIVE FACTORS:
+ Preserved joint mobility (near-normal angles)
+ Age/recovery status appears favorable
+ Clear target for intervention (EMG/strength)

CONCERNING FACTORS:
- Severe EMG reduction (38.6%) indicates substantial neurological damage
- Magnitude of deficit may require intensive rehabilitation
- Potential for long-term functional limitation without intervention


================================================================================
                  RECOMMENDATIONS FOR NEXT ANALYSES
================================================================================

1. TIME-SERIES ANALYSIS:
   Recommend repeating these measurements at regular intervals (2-4 weeks) 
   to track EMG improvement over time. This will determine:
   - Recovery trajectory
   - Rehabilitation program effectiveness
   - Prognosis for functional improvement

2. MULTIPLE SESSION ANALYSIS:
   Perform analysis on repeated sessions to:
   - Assess test-retest reliability
   - Understand variability within sessions
   - Establish baseline stability

3. EMG FREQUENCY ANALYSIS:
   Conduct spectral analysis of EMG signals to examine:
   - Frequency content shifts (may indicate motor unit changes)
   - Signal-to-noise ratio
   - Muscle fatigue patterns

4. CORRELATION ANALYSIS:
   Examine relationships between:
   - EMG activation and angle (muscle quality vs mobility)
   - EMG activation and functional tests (strength vs performance)
   - Recovery trajectory of each variable

5. CLINICAL CORRELATION:
   Compare findings with:
   - Functional Independence Measure (FIM) scores
   - Manual Muscle Strength (MMS) testing
   - Walking speed and gait parameters
   - Patient self-reported function

6. RESPONSE TO INTERVENTION:
   Re-test following targeted EMG training to measure:
   - EMG improvement magnitude
   - Functional gains associated with EMG improvement
   - Return-to-baseline timeline

7. SUBGROUP ANALYSIS:
   If multiple patients analyzed:
   - Stratify by time post-stroke
   - Stratify by rehabilitation intensity
   - Identify responders vs non-responders

8. ADVANCED STATISTICAL ANALYSIS:
   Consider:
   - Effect size confidence intervals (for precision)
   - Minimum clinically important difference (MCID)
   - Number-needed-to-treat (NNT) for interventions


================================================================================
                        HOW TO USE THE ANALYSIS SCRIPTS
================================================================================

SCRIPT FILES REFERENCED:
═════════════════════════

1. ttest_pareado.py
   Main script for paired t-test calculation
   Location: analysis/ttest_pareado.py
   
   Performs:
   - Paired t-test between ESQ and DIR for each variable
   - Calculates t-statistic, p-value, mean difference
   - Computes Cohen's d effect size
   - Generates 95% confidence intervals (estimated)
   - Produces CSV output file

2. Output Files Generated:
   - ttest_pareado_resultados.csv
   - ttest_pareado_resultados.xlsx (Excel format)
   - Analysis log/report files


RUNNING THE PAIRED T-TEST ANALYSIS:
════════════════════════════════════

PREREQUISITES:
✓ Python 3.x installed
✓ Required packages: pandas, scipy, numpy
✓ Input data file with columns: Angle_ESQ, Angle_DIR, EMG_ESQ, EMG_DIR, 
  ECG_ESQ, ECG_DIR

INSTALLATION OF DEPENDENCIES:
────────────────────────────

Open terminal/command prompt and run:

    pip install pandas scipy numpy openpyxl

RUNNING THE SCRIPT:
──────────────────

1. Place your data file in the analysis/ folder
2. Navigate to the analysis directory:
   
   cd analysis

3. Run the script:
   
   python ttest_pareado.py

4. Script will:
   - Read input data
   - Calculate paired t-tests
   - Compute effect sizes
   - Generate output files
   - Display results to console

INTERPRETING THE OUTPUT:
────────────────────────

CSV Output Columns:
- Variable: Name of measured variable (Angle, EMG, ECG)
- Mean_ESQ: Mean value for left/paretic leg
- Mean_DIR: Mean value for right/non-paretic leg
- Difference: Mean_ESQ - Mean_DIR
- t_statistic: Calculated t-value
- p_value: Statistical significance probability
- Cohen_d: Effect size calculation
- Significant: YES/NO based on p < 0.05

CUSTOMIZING THE ANALYSIS:
═════════════════════════

To modify the significance level (currently α = 0.05):

Edit ttest_pareado.py and locate:

    alpha = 0.05

Change to desired value (e.g., 0.01 for stricter criterion):

    alpha = 0.01

To add additional variables:

1. Prepare new columns in input data
2. Add to analysis loop in script
3. Rerun script
4. New results will be appended to output

TROUBLESHOOTING:
════════════════

Issue: "Module not found" error
Solution: Install missing package with pip

Issue: "File not found" error
Solution: Verify data file location and filename in script

Issue: Results differ from previous runs
Solution: Check input data hasn't changed; verify data format

Issue: All p-values very high
Solution: Check if ESQ and DIR columns are correctly assigned


================================================================================
                         GLOSSARY OF TERMS
================================================================================

STATISTICAL TERMS:
═══════════════════

ALPHA (α):
The significance level, typically 0.05 or 5%. Represents the probability of 
incorrectly rejecting the null hypothesis (Type I error). Results with 
p < α are considered statistically significant.

CONFIDENCE INTERVAL (CI):
A range of values estimated to contain the true population parameter with a 
specified level of confidence (typically 95%). For 95% CI, we expect 95% of 
similarly constructed intervals to contain the true value.

COHEN'S D:
A standardized effect size measure showing the magnitude of difference between 
two groups in units of standard deviation. Interpretation:
- |d| = 0.2: Small effect
- |d| = 0.5: Medium effect
- |d| = 0.8: Large effect
- |d| = 1.2+: Very large effect

DEGREES OF FREEDOM (df):
Number of values free to vary in a calculation. For paired t-test with n 
subjects, df = n-1.

EFFECT SIZE:
Magnitude of the difference/relationship, independent of sample size. Important 
for practical significance, not just statistical significance.

NULL HYPOTHESIS (H₀):
The hypothesis assuming no difference or no effect exists. Paired t-test tests 
whether to reject H₀ in favor of the alternative hypothesis.

P-VALUE:
Probability of observing results at least as extreme as those obtained, 
assuming the null hypothesis is true. Small p-values suggest the null 
hypothesis is unlikely.

PAIRED/DEPENDENT:
Measurements from the same subject at different conditions (here: different 
legs of the same patient). Related observations, not independent samples.

STATISTICAL SIGNIFICANCE:
Result unlikely due to random chance (p < α). Does NOT necessarily mean 
clinically important.

T-STATISTIC:
Ratio of the observed difference to its standard error. More extreme values 
(positive or negative) indicate greater difference. Used to calculate p-value.

TYPE I ERROR:
False positive - rejecting null hypothesis when it's actually true. Controlled 
by significance level α.

TYPE II ERROR:
False negative - failing to reject null hypothesis when it's actually false. 
Related to statistical power.


BIOMECHANICAL/CLINICAL TERMS:
═════════════════════════════

ANGLE (Knee Extension):
Measurement of knee joint position during specific movement. Measured in 
degrees (°). Range typically 0° (full extension) to 90°+ (flexed).

EMG (ELECTROMYOGRAPHY):
Measurement of electrical activity produced by muscles. Measured in microvolts 
(µV). Reflects muscle fiber depolarization and motor unit recruitment. Higher 
values indicate greater muscle activation.

ECG (ELECTROCARDIOGRAPHY):
Measurement of heart's electrical activity. Measured in millivolts (mV). 
In this context, may reflect cardiovascular response during leg exercises.

PARETIC:
Affected by paresis (partial paralysis). Post-stroke, the contralateral 
(opposite) side from the lesion is paretic. In this study, typically the left 
(ESQ) leg.

NON-PARETIC:
Unaffected by the neurological condition. The ipsilateral (same) side as the 
brain lesion. In this study, typically the right (DIR) leg.

HEMIPARESIS:
Partial paralysis or weakness of one side of the body (hemi-). Common 
consequence of stroke.

MOTOR UNIT:
Composed of one motor neuron and all the muscle fibers it innervates. Basic 
functional unit of muscle contraction.

MOTOR RECRUITMENT:
Progressive activation of motor units to increase muscle force. Reduced EMG 
reflects reduced recruitment after stroke.

NEUROMUSCULAR:
Related to both the nervous system and muscles. Neuromuscular impairment = 
problem in nerve-muscle pathway.

STRENGTH:
Ability to produce force. Directly related to EMG activation. Reduced EMG 
indicates reduced strength capacity.

GAIT ASYMMETRY:
Difference in walking pattern between left and right sides. EMG reduction 
contributes to asymmetrical gait.

FUNCTIONAL LIMITATION:
Restriction in activities due to impairment. Reduced quadriceps EMG limits 
walking, stair climbing, transfers.

REHABILITATION:
Therapeutic intervention to improve function after neurological injury. 
Should target identified impairments (here: EMG weakness).


ABBREVIATIONS USED:
═══════════════════

CI        = Confidence Interval
d         = Cohen's d (effect size)
df        = Degrees of Freedom
ECG       = Electrocardiography
EMG       = Electromyography
ESQ       = Esquerda (Left leg - Portuguese)
DIR       = Direita (Right leg - Portuguese)
MCID      = Minimum Clinically Important Difference
MMS       = Manual Muscle Strength
n         = Sample size
p         = p-value
FIM       = Functional Independence Measure
FES       = Functional Electrical Stimulation
H₀        = Null Hypothesis
H₁        = Alternative Hypothesis
α         = Alpha (significance level)
µV        = Microvolts
mV        = Millivolts
°         = Degrees
%         = Percent
*         = Significant (p < 0.05)
SIGF.     = Significant
df        = Degrees of freedom


================================================================================
                              FINAL SUMMARY
================================================================================

KEY TAKEAWAYS:

1. ⭐ EMG FINDING IS PRIMARY RESULT:
   - Statistically significant (p = 0.012)
   - Large effect size (d = -1.964)
   - 38.6% reduction in paretic leg
   - Indicates severe neuromuscular weakness
   - PRIMARY REHABILITATION TARGET

2. Angle finding NOT significant:
   - No reliable joint mobility limitation
   - Patient maintains adequate range of motion
   - Suggests problem is motor activation, not contracture

3. ECG finding NOT significant:
   - Systemic cardiovascular response similar bilaterally
   - Not a differentiating variable

4. CLINICAL CONCLUSION:
   Patient has significant POST-STROKE WEAKNESS affecting quadriceps muscle 
   activation. This is the PRIMARY IMPAIRMENT to address through rehabilitation.

5. REHABILITATION RECOMMENDATION:
   Implement intensive, task-specific training with EMG biofeedback to 
   improve motor recruitment in paretic quadriceps. Focus on strength and 
   motor control rather than mobility.

6. MONITORING RECOMMENDATION:
   Repeat EMG testing at regular intervals (every 2-4 weeks) to track 
   rehabilitation progress and adjust program intensity accordingly.

7. PROGNOSTIC CONSIDERATION:
   Severe EMG reduction (38.6%) indicates significant neurological damage. 
   Recovery may require 8-12 weeks or more of intensive rehabilitation. 
   Long-term functional prognosis depends on intervention intensity and 
   patient compliance.


================================================================================
                          DOCUMENT INFORMATION
================================================================================

Document Title: Paired T-Test Analysis Documentation
Dataset: Bilateral Leg Biomechanical Comparison
Variables Analyzed: Knee Extension Angle, EMG Activation, ECG Response
Analysis Type: Paired (Dependent) T-Test
Significance Level: α = 0.05
Date Created: December 2025

Related Files:
- ttest_pareado.py (Analysis script)
- ttest_pareado_resultados.csv (Results in CSV format)
- ttest_pareado_resultados.xlsx (Results in Excel format)
- analise_ecg_resultados_*.csv (ECG analysis details)
- analise_emg_resultados_*.csv (EMG analysis details)
- analise_angular_resultados_*.csv (Angle analysis details)

For questions or additional analysis:
Refer to the Python script (ttest_pareado.py) or contact the analysis team.

================================================================================
                              END OF DOCUMENT
================================================================================

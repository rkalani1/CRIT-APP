# Originality / copyright risk audit — Chapters 15–28

**Auditor role:** Free educational GitHub Pages originality check  
**Target:** `C:\Users\rkala\CRIT-APP\docs\curriculum\` files `15-` ... `28-`  
**Date:** 2026-07-13  
**Scope:** Dense read of openings, worked examples, tables/checklists, summaries; flag paste-risk vs original teaching.

## Verdict summary

| Level | Count | Chapters |
|-------|------:|----------|
| HIGH (pre-fix) | 2 | 25 (Users' Guides residue + near-verbatim instrument phrasing); 28 (file corruption blocking safe review — not paste, but unusable) |
| HIGH (post-fix) | 0 | — |
| MEDIUM | 4 | 17 (thin stub), 24 (tripartite clone of classic EBM skeleton), 15 (long original checklist — watch future paste), residual structural echo in 25 |
| LOW | many | Shared methods vocabulary only (Hill, Wilson–Jungner, LOCF/MCAR, fragility index, Table 2 fallacy, etc.) |
| SAFE / pass | majority body text | Synthetic trials, Web Edition frames, original stroke teaching tables |

**No commercial textbook abstracts, permission language, journal boilerplate, paper result tables, or full CONSORT/TRIPOD/GRADE instrument dumps were found in ch15–28.**

---

## Chapter-by-chapter

### 15 — Journal Club Architecture and Teaching Critical Appraisal
- **Risk:** LOW–MEDIUM  
- **Notes:** Long original pedagogical architecture (roles, agenda, disagreement protocol). Red-flag super-checklist is **original teaching scaffold**, not a CONSORT/TRIPOD item dump. Fictional late-window EVT run-of-show with synthetic counts.  
- **Watch:** Checklist is long; future edits must not paste publisher instruments.

### 16 — Paper Autopsies: Integrated Worked Critiques
- **Risk:** SAFE  
- **Notes:** Explicitly fictional papers (CLEAR-PATH, REHAB-FIRST, RapidLVO-Net, DUAL-SAFE, EPI-PREDICT). Synthetic numbers; original autopsy template. Strong originality posture.

### 17 — Disease Frequency and Association
- **Risk:** MEDIUM (thin stub)  
- **Notes:** Short (~800 words) but **original** Web Edition teaching with synthetic 2×2 and RD/RR/OR. Not paste; risk is *temptation to paste later* to bulk it up. Expand only with original prose.

### 18 — Causation Frameworks, Bias, and Inference
- **Risk:** LOW  
- **Notes:** Counterfactuals, causal pies, structural bias, Hill viewpoints as *questions*—standard methods taught in original stroke-framed prose. No instrument dump.

### 19 — Inference, Estimation, and the Architecture of Uncertainty
- **Risk:** SAFE / LOW  
- **Notes:** Original “estimation culture” teaching; manual SE/CI derivation on synthetic mortality data. Methods terms only.

### 20 — Regression and Survival Literacy
- **Risk:** LOW  
- **Notes:** Linear/logistic/Cox literacy; Table 2 fallacy explained in original stroke examples. Named methods, not handbook excerpt.

### 21 — Interaction, Effect Modification, and Standardization
- **Risk:** SAFE / LOW  
- **Notes:** Additive vs multiplicative scales with synthetic DAPT strata table; original teaching checklist.

### 22 — Screening, Early Detection, and Overdiagnosis
- **Risk:** LOW  
- **Notes:** Lead-time / length-time / overdiagnosis taught with neurovascular cases. Wilson and Jungner **named by criteria role only** (not a full reproduced WHO instrument). Natural-frequency PPV example is original teaching arithmetic.

### 23 — Clinical Reasoning, Dual Process, and Cognitive Bias
- **Risk:** SAFE / LOW  
- **Notes:** Large original chapter; dual-process + bias taxonomy fused to stroke code workflow and journal club design. Worked mimic case is synthetic teaching narrative. Shared cognitive-bias *names* only (public domain teaching lexicon).

### 24 — Appraising Therapy and Harm Questions
- **Risk:** MEDIUM → LOW after light rewrite  
- **Notes:** Classic validity / results / applicability skeleton (public-domain EBM pedagogy) was labeled “Tripartite Framework” in a way that echoes commercial handbook branding patterns. Body text was original stroke teaching (PROBE, composites, observational harm).  
- **Fix applied:** Retitled/reframed as “Three gates for therapy and harm papers” with CRIT-APP language (no commercial brand; no instrument dump).

### 25 — Appraising Diagnosis and Prognosis Papers
- **Risk:** HIGH → LOW after rewrite  
- **Findings (pre-fix):**
  - Residual “Users' Guides / Medical Literature” branding fragments and/or near-verbatim diagnostic/prognostic *question stems* characteristic of that commercial series (also reflected in repo history: `ORIGINALITY.md`, old nav title, scanner rules in `scripts/deep_originality_scan.py`).
  - Exact classic three-question formula and section titles matching commercial handbook templates.
- **Not found:** Full checklist instrument dumps, abstracts, permission notices.
- **Fix applied (in-place):** Full rewrite of framing and question stems into original CRIT-APP “three gates” (trustworthiness → effect extraction → local actionability); preserved stroke-specific worked examples with synthetic LRs/risk strata; explicit non-reprint banner language.

### 26 — Systematic Reviews and Clinical Prediction Rules
- **Risk:** LOW  
- **Notes:** Original teaching on publication bias, fixed vs random effects, CPR lifecycle (derivation/validation/impact). ABCD2 used as named clinical example, not a reproduced instrument table.

### 27 — Missing Data, Multiplicity, Interim Analyses, and Fragility
- **Risk:** LOW  
- **Notes:** MCAR/MAR/MNAR, LOCF critique, fragility index, interim stopping—methods literacy in original stroke prose. “Garden of forking paths” used as concept label only.

### 28 — Systems of Care, Policy, and Patient Communication
- **Risk:** HIGH (integrity) → SAFE after restore  
- **Findings (pre-fix):** Body text was **character-split** (one glyph per line, ~9k lines), empty learning objectives—unreviewable and unpublishable. Reconstructable prose was original teaching (de-implementation, transportability, metrics/Goodhart, absolute-risk SDM), not an external paste.
- **Fix applied:** Rebuilt clean chapter from reconstructed original prose; added learning objectives, operational checklists, systems memo template, summary, and practice—all original teaching packaging.

---

## Fixes documented this audit

| File | Action |
|------|--------|
| `docs/curriculum/25-appraising-diagnosis-and-prognosis-papers.md` | Rewrote branded / near-verbatim handbook stems into original CRIT-APP three-gate architecture |
| `docs/curriculum/24-appraising-therapy-and-harm-questions.md` | Removed “Tripartite Framework” handbook-echo heading; reframed as three gates |
| `docs/curriculum/28-chapter-28-systems-of-care-policy-and-patient-communication.md` | Restored from character corruption; expanded scaffolding without external paste |

---

## Residual risks (not paste, but monitor)

1. **Ch17 thin** — expand only with original Web Edition text.  
2. **Ch15 long checklists** — keep original; never drop in CONSORT/TRIPOD/GRADE full item lists.  
3. **Nav / scanner hygiene** — Historical Users' Guides title/path may linger in old scanner rules (`scripts/deep_originality_scan.py`); keep site nav pointed at `25-appraising-diagnosis-and-prognosis-papers.md` only.  
4. **Shared EBM pedagogy** — Validity/results/applicability as *ideas* are not copyrightable; avoid commercial series titles, taglines, and instrument wording.

## Method note

This audit is expert dense-read + pattern scan (branding, instruments, permission, corruption). It cannot certify absolute legal zero-risk against all training-data echo; it does clear clear paste signatures and the highest-risk handbook branding residue in this range.

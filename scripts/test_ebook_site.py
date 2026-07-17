#!/usr/bin/env python3
"""Structural tests for open-source ebook site (CRIT-APP or ML)."""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path


def load_root() -> Path:
    return Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()


ROOT = load_root()


class EbookSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = ROOT
        cls.docs = cls.root / "docs"
        cls.yml = (cls.root / "mkdocs.yml").read_text(encoding="utf-8")

    def test_product_is_open_source_ebook(self) -> None:
        index = (self.docs / "index.md").read_text(encoding="utf-8")
        blob = self.yml + "\n" + index
        self.assertRegex(blob, r"(?i)open-source ebook")
        self.assertNotRegex(self.yml, r"(?i)Web Edition")
        m = re.search(r"^site_name:\s*(.+)$", self.yml, re.M)
        self.assertIsNotNone(m)
        self.assertNotIn("Web Edition", m.group(1))

    def test_no_meta_nav_entries(self) -> None:
        for pat in [
            r"How to use",
            r"Update protocol",
            r"Originality",
            r"About &",
            r"About originality",
            r"navigation\.tabs",
        ]:
            self.assertIsNone(
                re.search(pat, self.yml),
                f"forbidden nav/chrome pattern still present: {pat}",
            )

    def test_nav_is_intro_plus_book(self) -> None:
        self.assertIn("Introduction: index.md", self.yml)
        self.assertIn("Book:", self.yml)
        self.assertIn("curriculum/", self.yml)

    def test_landing_is_brief(self) -> None:
        index = (self.docs / "index.md").read_text(encoding="utf-8")
        self.assertIn("ebook-hero", index)
        self.assertIn("chapter-list", index)
        self.assertNotIn("how-to-use.md", index)
        self.assertNotIn("about.md", index)
        self.assertNotIn("update-protocol.md", index)
        self.assertLess(len(index), 12000)

    def test_raw_html_routes_target_rendered_pages(self) -> None:
        index = (self.docs / "index.md").read_text(encoding="utf-8")
        raw_hrefs = re.findall(r"<a\b[^>]*\bhref=[\"']([^\"']+)", index, re.I)
        bad = [href for href in raw_hrefs if href.split("#", 1)[0].endswith(".md")]
        self.assertEqual(bad, [], f"raw HTML links bypass MkDocs rewriting: {bad}")

    def test_source_link_does_not_trigger_release_api_poll(self) -> None:
        index = (self.docs / "index.md").read_text(encoding="utf-8")
        self.assertNotRegex(self.yml, r"(?m)^repo_url:")
        self.assertRegex(index, r"https://github\.com/rkalani1/(?:CRIT-APP|ML)")

    def test_chapters_exist(self) -> None:
        ch = [
            p
            for p in (self.docs / "curriculum").glob("*.md")
            if p.name != "index.md" and "how-to-use" not in p.name
        ]
        self.assertGreaterEqual(len(ch), 10)

    def test_chapters_do_not_include_learning_objectives(self) -> None:
        label = (
            r"objectives?|"
            r"(?:(?:key\s+)?learning|chapter)\s+(?:objectives?|goals?|outcomes?)|"
            r"what\s+(?:you(?:['’]ll|\s+will))\s+learn|"
            r"after\s+(?:reading\s+)?this\s+chapter|"
            r"by\s+the\s+end\s+of\s+this\s+chapter"
        )
        numbered = r"(?:\d+(?:\.\d+)*[.)]?\s+)?"
        atx_heading = re.compile(
            rf"^\s{{0,3}}#{{1,6}}\s+{numbered}(?:{label})\s*[:—–-]?\s*#*\s*$",
            re.IGNORECASE | re.MULTILINE,
        )
        setext_heading = re.compile(
            rf"^\s*{numbered}(?:{label})\s*[:—–-]?\s*\n\s*(?:=+|-+)\s*$",
            re.IGNORECASE | re.MULTILINE,
        )
        html_heading = re.compile(r"<h[1-6]\b[^>]*>(.*?)</h[1-6]>", re.IGNORECASE | re.DOTALL)
        label_only = re.compile(
            rf"^\s*{numbered}(?:{label})\s*[:—–-]?\s*$",
            re.IGNORECASE,
        )
        objective_prose = re.compile(
            r"\b(?:"
            r"you(?:\s+will|['’]ll)\s+(?:learn|understand|be\s+able\s+to|compute|observe|practice|inspect|possess)|"
            r"by\s+the\s+end\s+of\s+(?:this|the)\s+chapter|"
            r"(?:the\s+)?(?:goal|objective)\s+of\s+this\s+chapter|"
            r"this\s+chapter\s+(?:will\s+)?(?:teach(?:es)?|equip(?:s)?|train(?:s)?|"
            r"give(?:s)?\s+(?:you|readers?|neurologists?)|dissect)|"
            r"(?:mastering|masters)\s+this\s+chapter"
            r")\b",
            re.IGNORECASE,
        )
        offenders = []
        for path in sorted((self.docs / "curriculum").glob("*.md")):
            text = path.read_text(encoding="utf-8")
            raw_html_objective = any(
                label_only.fullmatch(re.sub(r"<[^>]+>", " ", match).strip())
                for match in html_heading.findall(text)
            )
            if (
                atx_heading.search(text)
                or setext_heading.search(text)
                or raw_html_objective
                or objective_prose.search(text)
            ):
                offenders.append(path.name)
        self.assertEqual(
            offenders,
            [],
            f"learning-objective headings or promises should not appear in chapters: {offenders}",
        )

    def test_css_ebook_system(self) -> None:
        css = (self.docs / "stylesheets" / "extra.css").read_text(encoding="utf-8")
        self.assertIn("ebook-hero", css)
        self.assertIn("chapter-list", css)
        self.assertTrue(
            "Cormorant" in css or "serif" in css.lower() or "ebook" in css
        )

    def test_meta_pages_not_in_docs_root(self) -> None:
        for name in ("about.md", "how-to-use.md", "update-protocol.md", "ORIGINALITY.md"):
            self.assertFalse(
                (self.docs / name).exists(),
                f"{name} should not be public docs root",
            )

    def test_css_responsive_and_print(self) -> None:
        css = (self.docs / "stylesheets" / "extra.css").read_text(encoding="utf-8")
        self.assertIn("@media print", css)
        self.assertTrue(
            "max-width: 768px" in css or "max-width:768px" in css,
            "tablet breakpoint missing",
        )
        self.assertTrue(
            "max-width: 480px" in css or "max-width:480px" in css,
            "phone breakpoint missing",
        )
        self.assertIn(".md-header", css)
        self.assertIn("display: none", css)
        self.assertIn("prefers-reduced-motion", css)
        self.assertIn('.md-header__button[role="button"]:focus-visible', css)
        controls = (self.docs / "javascripts" / "header-controls.js").read_text(encoding="utf-8")
        self.assertIn("javascripts/header-controls.js", self.yml)
        self.assertIn("keydown", controls)
        self.assertIn("aria-expanded", controls)
        self.assertIn("button.md-code__button", controls)
        self.assertIn("Copy code to clipboard", controls)

    def test_navigation_labels_are_not_truncated(self) -> None:
        nav = self.yml.split("nav:", 1)[-1]
        self.assertNotIn("...", nav)
        self.assertNotIn("…", nav)

    def test_figure_density_and_asset_integrity(self) -> None:
        image_re = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")
        chapters = sorted((self.docs / "curriculum").glob("*.md"))
        for chapter in chapters:
            refs = image_re.findall(chapter.read_text(encoding="utf-8"))
            self.assertLessEqual(len(refs), 20, f"{chapter.name} has {len(refs)} raster figures")
            for ref in refs:
                if re.match(r"(?:https?:)?//", ref):
                    continue
                target = (chapter.parent / ref).resolve()
                self.assertTrue(target.is_file(), f"{chapter.name} has missing image {ref}")
        assets = [
            path
            for path in (self.docs / "assets" / "figures").rglob("*")
            if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".svg"}
        ]
        self.assertLessEqual(len(assets), 300, f"figure asset ceiling exceeded: {len(assets)}")
        size = sum(path.stat().st_size for path in assets)
        self.assertLessEqual(size, 25 * 1024 * 1024, f"figure assets total {size / 1024 / 1024:.2f} MiB")

        source_blob = "\n".join(
            path.read_text(encoding="utf-8", errors="replace")
            for suffix in ("*.md", "*.css")
            for path in self.docs.rglob(suffix)
        )
        orphan_assets = [path.name for path in assets if path.name not in source_blob]
        self.assertEqual(
            orphan_assets,
            [],
            f"unreferenced figure assets should not ship: {orphan_assets}",
        )

    def test_no_densifier_residue(self) -> None:
        bad_names = []
        for path in (self.docs / "assets" / "figures").glob("*"):
            if re.search(r"(?i)(?:^|_)cycle\d{3,}(?:_|$)", path.name):
                bad_names.append(path.name)
            if re.match(r"(?i)^cycle[123]", path.name):
                bad_names.append(path.name)
        self.assertEqual(bad_names, [], f"continuous densifier assets remain: {bad_names[:5]}")

    def test_retired_mutators_are_absent(self) -> None:
        retired = {
            "build_ebook_site.py", "build_web_edition.py", "build_from_docx.py",
            "expand_chapters.py", "wire_unused_figures.py", "embed_figures.py",
            "render_concept_figures.py", "cycle2_caption_art.py", "deep_originality_scan.py",
        }
        present = sorted(path.name for path in (self.root / "scripts").glob("*.py") if path.name in retired)
        self.assertEqual(present, [], f"retired destructive mutators remain: {present}")

    def test_evidence_register_is_explicitly_bounded(self) -> None:
        register = self.docs / "evidence-register.md"
        self.assertTrue(register.is_file(), "evidence register missing")
        text = register.read_text(encoding="utf-8")
        self.assertGreaterEqual(text.count("Primary-source spot-check 2026-07-15"), 10)
        self.assertIn("needs confirmation", text)
        self.assertIn("assets/figures/manifest.json", text)

    def test_known_content_regressions_stay_fixed(self) -> None:
        chapters = {
            path.name: path.read_text(encoding="utf-8")
            for path in (self.docs / "curriculum").glob("*.md")
        }
        blob = "\n".join(chapters.values())
        if self.root.name.upper() == "CRIT-APP":
            for false_claim in (
                "RRR) is constant across different baseline risk groups",
                "assume RR roughly equals HR",
                "OR = 11.4",
                "Absolute effects are causally identifiable",
                "## Advanced Application in Clinical Practice",
                "Precision is essentially infinite",
                "will result in a cumulative risk reduction that is much smaller than 30%",
                "which invariably exaggerate the perceived efficacy",
                "HR of 0.50 reduces the treated rate",
                "hazard ratios) are generally more transportable",
                "unambiguous net benefit",
                "mathematically stable across diverse populations",
                "Three synthetic paper autopsies sit in the appendix",
                "statistical theory guarantees that one of them",
                "virtually guarantees a false positive",
                "guaranteeing exchangeability at baseline",
                "answer initiation-policy questions without bias",
                "mathematically stable across varying baseline risks",
                "absolute gold standard of synthesis",
                "initial observational proof for mechanical thrombectomy",
                "You must treat 25 patients to prevent one event",
                "Exactly 50 patients must be treated",
                "mathematically guarantees a spurious association",
                "The trial is definitively negative",
                "mathematically trivial to declare non-inferiority",
                "A Per-Protocol analysis is mandatory",
                "guaranteed neurocognitive and psychiatric toxicities",
                "Internal validation proves only",
                "The absolute risks are trustworthy",
                "formally consider palliation",
                "It consists of four elements: the target population",
                "all variables in the adjustment set were measured strictly prior to the index time and are true baseline common causes",
                "irrevocably destroys causal inference",
                "This inflates both sensitivity and specificity.",
                "while conditionally isolating the effects from modeled covariates",
                "an absolute minimum of 10 to 20 outcome events per candidate predictor variable",
                "A literature search restricted to PubMed and English-language publications guarantees selection bias",
                "Adaptive platform trials utilize response-adaptive randomization and continuous arm-dropping",
                "Spectrum bias in training guarantees prevalence shift in deployment",
                "single-center provenance guarantees that the model has overfit",
                "fabricated by methodological incompetence",
                "PROs require strict blinding",
                "Follow-up completeness exceeds 95%",
                "Analysis strictly Intention-to-Treat",
                "Reference standard is a true gold standard",
                "biases the effect upward",
                "interaction test proving the treatment effect differs",
                "HR of 0.72 is a mathematical artifact",
                "survival estimates will be downwardly biased",
                "drug works only on one scale",
                "true interaction between etiology and therapeutic response will be attenuated",
                "neutralizing the compositional variance",
                "current guidance favors dual antiplatelet therapy over thrombolysis",
                "estimates the pragmatic effectiveness",
                "per-protocol and as-treated analyses estimate biological efficacy",
                "drug will falsely appear to cause higher rates",
                "In stroke trials, MNAR is highly prevalent",
                "alpha-spending techniques like Bonferroni or Hochberg",
                "Spin is the clinical translation of p-hacking",
                "So about (A−B) are helped",
                "four non-overlapping domains",
                "from a internally valid study",
                "the false-positive rate will explode",
                "the 30 false negatives are a massive undercount",
                "If the primary outcome is negative, the trial is negative",
                "guarantees the deployment of ineffective or harmful technology",
                "The model will fail completely",
                "guarantees high accuracy",
                "performance silently and predictably degrades",
                "will perform poorly in 2026",
                "requires geographically distinct cohorts to prove",
                "AUPRC is the mandatory discriminative metric",
                "assume the PPV is unusable",
                "Label fidelity is the ceiling of algorithm performance",
                "An algorithm cannot logically exceed the reliability",
                "Clinical heterogeneity inevitably introduces statistical heterogeneity",
            ):
                self.assertNotIn(false_claim, blob)
            self.assertNotRegex(blob, r"(?m)^[ \t]*\d+\.[ \t]+\d+\.")
            self.assertNotRegex(blob, r"(?m)^(?:ightarrow|eq)\b")
            self.assertFalse(
                any(ord(char) < 32 and char not in "\n\r\t" for char in blob),
                "curriculum contains embedded control characters",
            )
            self.assertIn("10/418", chapters["12-effect-sizes-absolute-benefit-nnt-and-clinical-importance.md"])
            self.assertIn("an HR is not a risk ratio", blob)
            self.assertIn("not automatically causally identified or transportable", blob)
            self.assertIn("Five synthetic paper autopsies appear in this chapter", blob)
            self.assertIn("O/E = 270/240 = 1.125", blob)
            self.assertIn("Aalen–Johansen cumulative incidence", blob)
            self.assertIn("from 0.25 to 0.40 gives a 0.15 absolute increase", blob)
            self.assertIn("Crude risk for Early DOAC = 450 / 6,000 = 7.5%", blob)
            self.assertIn("21.25% - 7.5% = 13.75%", blob)
            self.assertIn("Risk Difference (RD) = 0.440 − 0.320 = 0.120", blob)
            self.assertIn("0.80 / (160/850) = 4.25", blob)
            self.assertIn("40 events among 200 control participants and 22 among 200 treatment participants", blob)
            self.assertIn("25 of 200 and p = 0.0572", blob)
            self.assertIn("conventionally reported as 17 people", blob)
        elif self.root.name.upper() == "ML":
            self.assertNotIn("ml_concept_", blob)
            for false_claim in (
                "positive definite (a local minimum)",
                "rolling downhill is guaranteed to find it",
                "correction matters only for the first tens of steps",
                "PSI ≳ 0.2 is a material alarm",
                "rule of thumb often near 0.2-0.4",
            ):
                self.assertNotIn(false_claim, blob)
            math = chapters["00-mathematical-foundations-for-machine-learning.md"]
            self.assertIn("∇f(1, 1) = (6, 4) ≠ 𝟎", math)
            self.assertIn("therefore is not a local minimum", math)
            self.assertIn("Convergence of gradient descent is a separate result", math)

    def test_no_figure_concept_admonitions(self) -> None:
        hits = 0
        for p in (self.docs / "curriculum").glob("*.md"):
            hits += p.read_text(encoding="utf-8", errors="replace").count(
                "Figure concept (text diagram)"
            )
        self.assertEqual(hits, 0, f"leftover text-diagram callouts: {hits}")

    def test_no_filename_only_figure_captions(self) -> None:
        generic = re.compile(
            r"^\s*\*(?:Teaching graphic|Teaching figure)\s*\([^)]*\."
            r"(?:png|svg|jpe?g|webp)\)\.\*\s*$",
            re.IGNORECASE | re.MULTILINE,
        )
        offenders = [
            path.name
            for path in sorted((self.docs / "curriculum").glob("*.md"))
            if generic.search(path.read_text(encoding="utf-8", errors="replace"))
        ]
        self.assertEqual(offenders, [], f"filename-only figure captions: {offenders}")

    def test_math_verify_script_passes(self) -> None:
        import subprocess

        script = self.root / "scripts" / "verify_math_examples.py"
        self.assertTrue(script.exists(), "verify_math_examples.py missing")
        r = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True,
            text=True,
            cwd=str(self.root),
        )
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("ALL_PASS", r.stdout)

    def test_accuracy_figures_match_their_asserted_source_data(self) -> None:
        import subprocess

        if self.root.name.upper() != "CRIT-APP":
            self.skipTest("accuracy-critical SVG generator is specific to CRIT-APP")
        script = self.root / "scripts" / "regenerate_accuracy_figures.py"
        self.assertTrue(script.exists(), "regenerate_accuracy_figures.py missing")
        result = subprocess.run(
            [sys.executable, str(script), "--check"],
            capture_output=True,
            text=True,
            cwd=str(self.root),
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("ACCURACY_FIGURES_OK 3", result.stdout)


if __name__ == "__main__":
    # Preserve path arg for setUpClass via module-level ROOT
    args = [sys.argv[0]]
    unittest.main(argv=args, verbosity=2)

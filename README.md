# Critical Appraisal for Neurologists

**Open-source ebook** — a free reading site that teaches stroke-aware critical appraisal of clinical evidence.

- **Read it:** https://rkalani1.github.io/CRIT-APP/
- **Machine-readable index:** https://rkalani1.github.io/CRIT-APP/llms.txt
- **ML & AI companion:** https://rkalani1.github.io/ML/

## What this is

Twenty-eight short chapters that move a published claim to a defensible bedside
decision: match the question to the design, translate effects into absolute
terms, and carry uncertainty through to action. Worked numerical examples are
synthetic unless a specific trial or guideline is named. Selected
high-consequence quantitative claims have documented primary-source checks in the
[evidence register](https://rkalani1.github.io/CRIT-APP/evidence-register.html),
which is explicitly bounded — not a claim of full-book peer review.

Educational only — not medical advice, not local policy, not institutional endorsement.

- [Publication standards and disclosures](https://rkalani1.github.io/CRIT-APP/publication-standards.html)

## Build locally

Use Python 3.12:

```bash
python -m pip install --require-hashes -r requirements.lock
mkdocs serve
```

The full release gates and contribution standards are in
[CONTRIBUTING.md](CONTRIBUTING.md).

## Cite

Citation metadata lives in [`CITATION.cff`](CITATION.cff); GitHub renders a
"Cite this repository" button from it.

## License

Publisher-controlled book material is offered under CC BY 4.0 only to the
extent the publisher controls the relevant rights; site software is ISC.
Third-party components retain their own licenses. See [LICENSE](LICENSE) and
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

AI tools assisted development; the human maintainer selected, revised, reviewed,
and decided what to publish. Current figure hashes and repository-origin
records are maintained in `_meta/asset-rights-register.json`. These measures
support traceability but are not a legal opinion or a guarantee of
non-infringement. The bounded checks and residual human confirmations are
recorded in
[`_meta/PUBLICATION_REVIEW_2026-07-30.md`](_meta/PUBLICATION_REVIEW_2026-07-30.md).

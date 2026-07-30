# Vendored webfont provenance

Reviewed: **30 July 2026**

These WOFF2 files were introduced by Rizwan Kalani in repository commit
`5add11faf25f0ac23c8b5a8719f9779cad47d910` on 18 July 2026. The commit records
that they replaced this Google Fonts CSS request:

```text
https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Source+Sans+3:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,500;0,8..60,600;0,8..60,700;1,8..60,500&display=swap
```

The files were not edited after retrieval in this repository. The Google Fonts
delivery path may subset or convert upstream fonts, so “not edited after
retrieval” does not mean byte-identical to an upstream desktop/source release.
The files retain embedded copyright and license metadata and are redistributed
under SIL Open Font License 1.1. Copyright notices and the full license are in
`OFL-1.1.txt`.

## Exact inventory

| Files | SHA-256 | Embedded metadata |
| --- | --- | --- |
| `jetbrains-mono-400-normal.woff2`, `jetbrains-mono-500-normal.woff2` | `83c005d49d8a6a50474c73a5a36ac0468076e9c4a29da7bdb14995d80560a5be` | JetBrains Mono 2.211; variable `wght` 400–800; copyright 2020 JetBrains Mono Project Authors |
| `source-sans-3-400-normal.woff2`, `source-sans-3-500-normal.woff2`, `source-sans-3-600-normal.woff2`, `source-sans-3-700-normal.woff2` | `7a19a7027e125257d310c6dbd78ae3a30b5ea1e3794d60b12bb28227a003bfda` | Source Sans 3 3.052; variable `wght` 200–900; © 2023 Adobe; Reserved Font Name “Source” |
| `source-sans-3-400-italic.woff2` | `3c230c03425a2866e4b57954f3173fc149dba2634e9ee32c681b41d96c7f06fe` | Source Sans 3 3.052 italic; © 2023 Adobe; Reserved Font Name “Source” |
| `source-serif-4-500-normal.woff2`, `source-serif-4-600-normal.woff2`, `source-serif-4-700-normal.woff2` | `f2ea9c12d2fe9bd3a9589b02ad2c0909da88f30938c91adc838c4f4098f9f9e0` | Source Serif 4 4.004; variable `wght` 200–900 and `opsz` 8–60; © 2014–2021 Adobe; Reserved Font Name “Source” |
| `source-serif-4-500-italic.woff2` | `5d19e19e67eced3e86c69d52ffaf4eedcc7366abdf0b4882391cab799641ceb6` | Source Serif 4 4.004 italic; variable `opsz` 8–60; © 2014–2021 Adobe; Reserved Font Name “Source” |

Several weight-labeled paths intentionally contain the same variable-font
bytes. The CSS maps those shared files to the requested weights; the duplicate
paths are retained to avoid changing published asset URLs during this release.

## Verification

Embedded names, versions, copyrights, weights, and axes were read with
FontTools. Hashes are checked by `scripts/check_publication_safety.py`.
Redistribution rights and conditions come from the fonts' OFL notices; no
trademark endorsement is asserted.

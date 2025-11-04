# NIST 800-53 (Rev. 5) Controls — Starter (Official Text Excerpts)

This package includes a **starter CSV** of selected NIST 800-53 Rev. 5 controls and enhancements (with **family header rows**) using official control language.
It is designed to bootstrap your **NIST CSF ↔ 800-53 mapping** GitHub repository.

> ⚠️ Do not commit sensitive data. This starter uses public, official control statements excerpted from NIST SP 800-53 Rev. 5.

## Files
- `nist-800-53-controls-with-enhancements.csv` — Starter list with selected controls and enhancements across AC, AU, CM, IR, CP, PM, and PT families. Includes **FAMILY_HEADER** rows for readability.
- (You will add your CSF mapping files next.)

## Suggested Repo Structure
```
nist-csf-80053-mapping/
├─ nist-800-53-controls-with-enhancements.csv
├─ mapping.csv              # your CSF→800-53 crosswalk
├─ README.md
└─ docs/
```

## How to Use
1. **Create a GitHub repo** named `nist-csf-80053-mapping` (Public suggested).
2. **Upload** this CSV and your mapping files.
3. **Link by Control_ID** in your mapping (e.g., `ID.AM-01 → CM-8(7)` if applicable).
4. **Extend the CSV** by adding more controls from NIST SP 800-53 Rev. 5 as needed.
5. Optional: Use GitHub Issues to track review or evidence for any control.

## Family Header Rows
- Rows with `Row_Type = FAMILY_HEADER` are provided for readability in spreadsheets.
- When importing to databases or BI tools, you can filter out header rows.

## Source
- NIST Special Publication 800-53, Revision 5 — *Security and Privacy Controls for Information Systems and Organizations*.
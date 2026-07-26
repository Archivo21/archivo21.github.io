# Migration Map

**Prepared:** 2026-07-26  
**Source repository:** `Archivo21/anhqv-ts2-preservation-project`

The website is an institutional front door. The ANHQV-TS2 repository remains the canonical research and evidence repository.

| Source | Website use | Canonical location |
|---|---|---|
| Root `README.md` | Home project card and `/projects/anhqv-ts2/` | ANHQV-TS2 root |
| `RECRUITMENT.md` | `/contribute/` and reference snapshot | ANHQV-TS2 root |
| `CONTRIBUTING.md` | Contribution principles and reference snapshot | ANHQV-TS2 root |
| `NOTICE.md` and `LICENSE` | `/rights/`, root site notice, and reference snapshot | ANHQV-TS2 root |
| `CITATION.cff` | Reference snapshot only | ANHQV-TS2 root |
| EXP001 `README.md` and `Notes.md` | `/research/exp001/` and reference snapshot | `02 Field Reports/EXP001 - Two Click Foundations/` |
| `Attribution.md` | `/provenance/` and full local reference copy | Intended `00 Project/Attribution.md` |
| Archivo 21 contributor archive | `/about/`, `/provenance/`, and full local reference copy | `Archive/Contributor Archives/archivo-21.md` |

## Deliberately not migrated

- the complete numbered ANHQV-TS2 directory tree;
- raw or locally held video files;
- third-party ANHQV or Sims assets;
- private finance records;
- incomplete interview transcripts;
- source-site mirrors or archival captures without permission;
- duplicate copies of every governance and field-report file.

## Before committing

The online ANHQV-TS2 repository was missing several hidden or locally retained files during this preparation. Add the user's newer versions before commit where they supersede these snapshots. In particular, compare:

- `.gitignore` and `.gitattributes`;
- `.github/ISSUE_TEMPLATE/` and pull-request template;
- `00 Project/Attribution.md`;
- any corrected release, roadmap, changelog, citation, or contact file.

Do not silently edit the reference snapshots after migration. Replace the snapshot and update its source date instead.

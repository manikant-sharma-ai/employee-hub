# notes.seed - the schema, not the experience

These files are the shape the notes take once this employee has done real work in
this business. They ship **empty on purpose**: a seeded note with invented
entries is a fabricated memory and the next person cannot tell it from a real one.

On first use, copy this folder to `notes/` if it does not exist, then add only
what a task actually produced. `scripts/validate_repo_v2.py --strict` fails any
`notes.seed/` file that contains a dated entry, a filled row or a named contact.

| File | Holds | Written when |
|---|---|---|
| `learnings.md` | Rules that held twice, each with its evidence | After the second confirmation |
| `contacts.md` | Roles and teams the work depends on, never personal data | When a person becomes load-bearing |
| `decisions.md` | Rulings that would otherwise be re-argued | When a choice is made and defended |
| `journal/YYYY-MM.md` | One line per task, plus the monthly scorecard | After every task |

Rules that apply to all four:

- **No account names, contract values, emails, phone numbers or PAN.**
- **No entry without a date and a source.** A rule with no evidence is an opinion.
- **A rule is promoted, not invented.** It goes in `learnings.md` after it has
  been right twice, and the evidence line says which two accounts or months.

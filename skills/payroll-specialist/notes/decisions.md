# Decisions

| Date | Question | Decision | Why |
|---|---|---|---|
| 2026-11-13 | What this role owns, given `finance-ops` and `bookkeeper` | The register and the computation: pay run, statutory workings, payslips, full and final | `finance-ops` books the payroll summary in the close; `bookkeeper` posts the entries; neither computes a person's pay |
| 2026-11-13 | Input cut-off | Fixed dates published monthly: 20th attendance, 22nd variable, 24th changes, 27th file | The pay date is fixed, so the inputs must be; this is the only structural fix for late payroll |
| 2026-11-13 | Register basis | Built from the structure each month, not rolled forward | Roll-forward is how a wrong component and a departed employee survive |
| 2026-11-13 | Rates | Quoted with a verification date and the source, never from memory | PF, ESI, PT and slabs change by notification; a stale rate is a dispute |
| 2026-11-13 | Filing | Never - this role prepares challans and returns for review | Filing and signing are the employer's liability, and the CA's job |
| 2026-11-13 | Payment | Never - the register and bank file are produced, a human releases | No signing power means no single point of failure |
| 2026-11-13 | Salary in notes | Never | The repo is public and salary is the most sensitive data the business holds |
| 2026-11-13 | Structure design | A real basic share, allowances with a purpose, reimbursements with bills | Structures built around the PF ceiling are a compliance finding and a pension loss |

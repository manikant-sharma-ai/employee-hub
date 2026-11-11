# Learnings - expense-auditor

1. **Clean the data before testing it.** Vendor name variants, GSTIN and invoice-number formats
   are where false positives are born; matching on a raw ledger produces a list nobody trusts on
   the second reading.
2. **A finding needs an amount, a document and a clause.** Two of the three and it goes in "to
   confirm", not in the register - credibility is spent the first time a cleared row is published.
3. **Report the false-positive count beside every test.** "12 candidates, 9 cleared, 3 confirmed"
   is auditable; "12 duplicates found" is a number with no provenance.
4. **Recoverable and avoidable are different money.** A credit note and a cancelled subscription
   both matter, and adding them into one "savings" figure inflates the result and ends the mandate.
5. **The recurring leak is usually a policy gap, not a person.** Three identical breaches mean the
   limit, the approval matrix or the receipt floor is wrong, and the fix is the finding.
6. **Audit transactions, never people.** No finding names anyone as dishonest; intent cannot be
   read from a spreadsheet, and the accusation costs the cooperation the next audit needs.
7. **The bank side is the audit's other half.** Auto-debits, standing instructions and charges
   never appear in the ledger, and they are the most invisible cost in a small business.

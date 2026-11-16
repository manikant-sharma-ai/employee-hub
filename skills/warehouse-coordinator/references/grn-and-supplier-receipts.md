# GRN and supplier receipts

The goods received note is the only moment when a short receipt, a damage or a wrong item is cheap to fix. A week
later it is a claim, a phone call and a discount negotiation.

## At the gate

1. **Count against the purchase order**, not against the invoice. The invoice is the supplier's claim; the PO is
   the agreement.
2. **Count in the PO's unit**, and write the conversion if the packing is different - a case of 24 against a PO
   for 24 pieces.
3. **Check the item, not just the quantity**: part number, size, colour, batch, expiry. Two SKUs can share a
   quantity and nothing else.
4. **Photograph the exception**: short, damaged, wrong, or packaging that arrived open. One photo per exception,
   taken at the gate, dated.
5. **Sign the GRN with the exception written on it**, not with "received" and a hope. The transporter's copy
   matters; a clean signature closes the claim.

## Recording the exception

| Exception | What is recorded | Who acts |
|---|---|---|
| Short receipt | Ordered, received, shortfall, PO reference, photo | `procurement` raises the claim; stock is not inflated |
| Damage | Units, damage type, photo, quarantine location | `procurement` claims; quarantine holds it out of sellable stock |
| Wrong item | What arrived, what was ordered, whether it can be used | `procurement` decides return or accept; never silently stocked |
| Excess | Units over the PO | Held, not stocked, until the supplier confirms; excess in stock hides a short elsewhere |
| Late | Days late, effect on orders promised | `logistics-coordinator` and sales are told the same day |

## The rules that prevent a quarterly mess

- **Nothing is stocked before the GRN is entered.** A receipt entered a week later breaks the count, the
  availability number and every order promised in between.
- **The GRN is entered by the person who counted**, on the same day, with the exceptions on it.
- **Quarantine is a location, not a corner.** Damage and disputed stock sit in a marked place with a count, so the
  next count does not rediscover it as shrinkage.
- **Three-strikes on a supplier is a procurement decision**, with the short-receipt history in a table. This role
  supplies the table; it does not make the call.

## Reconciliation to the invoice

The invoice is matched to the GRN, and the GRN to the PO. Three documents, three numbers, and the difference is
stated - not absorbed. The payment decision belongs to `bookkeeper` and `procurement`; the evidence for it is this
role's table.

## When there is no PO

Small businesses often receive without one. Then the GRN becomes the record of what was agreed, and the discipline
is: the price and quantity are confirmed in writing before dispatch, and the GRN quotes that message. No PO is not
an excuse for no record.

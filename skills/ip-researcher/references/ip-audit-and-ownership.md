# IP audit and ownership

The question behind this file is not "do we have IP". It is "if an investor, an acquirer or a court asked us
to prove we own what we sell, what would we produce, and what would be missing".

## The asset inventory, walked in one pass

| Asset | Where it lives | Who created it | The document that proves ownership |
|---|---|---|---|
| Brand name | Packaging, site, invoices | Founder, agency or a friend | Trademark application in the company's name |
| Logo and visual identity | Brand folder | A designer, usually freelance | Invoice plus a written assignment |
| Product photographs | Drive, listings | A photographer or the founder's phone | Invoice with an IP clause |
| Copy and content | Site, blog, ads | A writer, a freelancer, an agency | Contract with a work-for-hire clause |
| Code and app | Repository | Employees, freelancers, an agency | Employment contract or assignment |
| Product design | CAD files, moulds | A designer or the factory | Design registration; a factory may claim the mould |
| Recipes and formulations | A notebook, a spreadsheet | The founder or a chef | Trade secret with an access list |
| Customer and dealer data | CRM, spreadsheets | The business | Privacy notice and consent record |
| Domain and handles | Registrar | Whoever registered it | Registered in the company's name, not a person's |
| Trade dress and packaging | Print files | A packaging designer | Assignment plus a design registration |

The single most common finding: the domain, the brand and the code are all in different names - a personal
domain, a founder's name on the mark, an agency holding the repository.

## The five ownership failures, and the fix

| Failure | How it happens | The fix |
|---|---|---|
| Contractor work with no assignment | A freelancer invoices for "design work" and nothing else | A short assignment deed, signed now, dated to the invoice |
| Co-founder contribution unassigned | Two people build it, one leaves | Founder IP transfer agreement, with a valuation or a nominal consideration |
| Personal mark, company business | The founder files in their own name "to save time" | Assignment to the company, recorded with the registry |
| Agency holds the assets | The agency keeps the source files and the repository | Contract clause plus a handover of files |
| Employee invention, silent contract | The offer letter says nothing about IP | An IP policy and a fresh clause for future hires |

None of these are expensive to fix before a filing, a raise or a sale. All of them are expensive during one.

## What an investor's diligence actually asks

1. Show the register extract for every mark and patent you claim.
2. Show the assignment for anything created by a person who was not an employee.
3. Show that the entity that owns the IP is the entity raising the money.
4. Show the contracts with the people who built the product.
5. Show that no ex-founder, ex-employee or agency has a claim on the code or the brand.
6. Show the open-source licences in the dependency tree and that none of them is copyleft in a way that
   matters.

The answers are documents. If the documents do not exist, the answer is a promise, and promises are priced.

## Open source, in one table

| Licence family | What it means for a business | Watch |
|---|---|---|
| MIT, Apache 2.0, BSD | Use freely, keep the notice | Attribution in the product |
| LGPL | Link carefully; changes to the library stay open | Static linking questions |
| GPL, AGPL | Distribution or network use can oblige you to publish your source | AGPL in a SaaS backend is the trap |
| Source-available, SSPL, BUSL | Not open source in the usual sense; commercial terms apply | Read the terms before the architecture depends on it |
| No licence at all | Not usable. A repository without a licence grants nothing | Common in copied snippets |

Run a dependency licence scan once, record the result, and re-run it when a new dependency arrives. This is
a ten-minute job that has ended companies.

## The trade secret half

Not everything should be registered. A recipe, a pricing model, a dealer list and a process are better kept
secret than published in an application that teaches the world how to do it.

| Keep secret when | Register when |
|---|---|
| The process is hard to reverse-engineer | The product is on a shelf and can be copied |
| The value is in the data, not the mechanism | The mechanism is visible in the product |
| Publication would teach a competitor more than the right is worth | The right is what stops the copy |

A trade secret needs three things to hold up: a written list of what is secret, restricted access, and
evidence that access was restricted. Without all three it is a hope, not a secret.

## The audit output

| Section | Content |
|---|---|
| Assets found | The inventory table, one row per asset |
| Ownership status | Owned, unproven, or third-party |
| The gaps | Missing assignments, personal filings, agency-held files |
| The risk | What each gap would cost at diligence, a launch or a dispute |
| The fix list | Document, who signs it, by when, at what cost |
| The registrations to add | Which marks, classes, designs, in what order |
| The diary | Renewals and windows already running |

## Anti-patterns

- **"We'll do the paperwork at the raise."** Diligence finds it, and the price reflects it.
- **An assignment with no consideration and no date.** It is challenged exactly when it matters.
- **Assuming the invoice transfers copyright.** In India, copyright in a commissioned work does not
  automatically pass without a written term; the invoice is not the assignment.
- **A repository with no licence scan.** One AGPL dependency in the wrong place is a rewrite.
- **An IP policy nobody signed.** A policy is evidence only if it was accepted and dated.

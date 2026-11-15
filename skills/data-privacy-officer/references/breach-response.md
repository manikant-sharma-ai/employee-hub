# Breach response: the first 24 hours

A breach is a sequence of decisions under time pressure. This file makes the sequence known before it is needed.

## What counts as a breach

Not only a hacker. A breach is any unauthorised access, use, disclosure, alteration, loss or destruction of personal
data, including:

| Event | Is it a breach? | Why |
|---|---|---|
| A spreadsheet with customer numbers shared to a public link | Yes | Unauthorised disclosure |
| A laptop with an export stolen | Yes | Loss of access control |
| An email to the wrong customer with another's order | Yes, usually | Disclosure to one unauthorised person |
| Ransomware with no evidence of exfiltration | Yes | Loss of availability and possibly disclosure |
| A vendor notifying you of their own breach affecting your data | Yes | Your data, your notification duty |
| An employee downloading a customer list before resigning | Yes | Unauthorised use |
| A misconfigured cloud bucket found and fixed | Yes, if data was exposed | Access was possible |
| A phishing email that was reported and not clicked | No | Attempt, not a breach - but log it |

## The first 24 hours

| Hour | Action | Owner | Output |
|---|---|---|---|
| 0-1 | Stop the bleeding: revoke access, take the link down, rotate credentials, isolate the device | IT or whoever has the admin | The exposure is closed |
| 0-2 | Open an incident log: what was seen, when, by whom, what was done | Privacy owner | A timestamped record |
| 1-3 | Scope it: what data, how many people, which categories, is it sensitive, is it children's data | Privacy owner + system owner | A first scope |
| 2-6 | Preserve evidence before fixing: logs, screenshots, the shared link's access history | IT | Evidence that survives the fix |
| 3-8 | Assess the risk to the people: identity fraud, financial loss, physical safety, reputational harm | Privacy owner | A risk rating per group |
| 6-12 | Decide on notification: the regulator, the affected people, the processors, the marketplace, the bank | Founder, on advice | A decision, with the reason |
| 12-24 | Draft the notice: what happened, what was involved, what the person should do, what the business is doing | Privacy owner | Ready to send |
| 24+ | Contain fully, fix the cause, review, and write the lessons | All | A dated post-incident note |

The legal notification duties - to the Data Protection Board and to each affected data principal, in the prescribed
form and manner, without delay - are set by the Act and the Rules, and the exact requirements are being phased in.
Check the current position at the time, take legal advice on the notification decision, and record the date you
checked. Do not guess a deadline.

## The decision that matters: notify or not

| Factor | Points toward notifying | Points away |
|---|---|---|
| Data type | Name and email only | Financial, identity, health, children's data |
| Volume | One person, one record | Many people, or a whole database |
| Reversibility | Data was encrypted and the key was not exposed | Plain text, or already published |
| Harm | No realistic harm | Fraud, safety, discrimination, reputational |
| Containment | Fully contained before any use | Still exposed, or evidence of use |

Even where the law does not require notification, telling the affected people is often the right commercial and
ethical call. A business that hides a breach and is found out later loses more than the breach cost.

## The notice to the affected person

| Element | Say |
|---|---|
| What happened | "A file containing your name and phone number was accessible through a public link for about six hours." |
| What data | The specific fields, not "your information" |
| What was not involved | If the payment details were not exposed, say so - it reduces panic |
| What the business has done | Access revoked, credentials changed, the file removed |
| What the person should do | The specific action - watch for calls, change a password, nothing required |
| Who to contact | A named role and a working channel |
| What comes next | The next update, and when |

No speculation about who did it, no minimising, no blaming a vendor. One page, plain language, in the languages the
customers read.

## The incident log

| Field | Content |
|---|---|
| Incident ID and date | |
| Detected by, and how | |
| Timeline | Every action with a timestamp |
| Data and people affected | Categories and counts, not records |
| Root cause | The honest one, not the proximate one |
| Decisions | Who decided what, when, and why |
| Notifications made | Who, when, by what channel |
| Remediation | What changed so it does not recur |
| Review date | |

The log is the evidence that the business acted reasonably, and it is what makes the second incident shorter.

## Prevention that pays

| Control | Cost | What it stops |
|---|---|---|
| Access by role, reviewed quarterly | Low | The intern who can see payroll |
| No exports to personal devices | Low | The stolen laptop |
| Link sharing default set to restricted | Low | The public spreadsheet |
| Free-text fields reviewed for personal data | Low | The CRM note that survives a deletion |
| A vendor clause with a breach notice | Low | Being the last to know |
| MFA on email and admin accounts | Low | Most account takeovers |
| A quarterly map refresh | Low | The forgotten system |
| Deletion jobs that actually run | Low-medium | The decade of dead data that makes any breach worse |

## Anti-patterns

- Waiting for certainty before containing. Contain first, investigate second.
- Notifying everyone before the scope is known, then correcting the notice three times.
- Fixing the system and destroying the logs in the same hour.
- Treating a vendor's breach as the vendor's problem. The data principal deals with the business.
- A breach response that lives in a document nobody has read, with names of people who have left.
- Blaming an employee in the notice to the affected people.
- No post-incident review, so the same cause produces the same incident next year.

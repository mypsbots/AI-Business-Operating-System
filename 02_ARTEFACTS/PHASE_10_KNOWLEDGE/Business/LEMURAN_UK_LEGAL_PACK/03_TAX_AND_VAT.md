---
id: LEMURAN-UK-03
title: "HMRC, Corporation Tax, VAT and payroll"
document_type: "Knowledge Article"
owner: "Lemuran director — assignment pending"
status: Draft for human review
classification: Internal
version: 1.1.0
updated: "2026-10-10"
created: "2026-10-09"
verified_on: "2026-10-09"
jurisdiction: United Kingdom
legal_advice_status: Decision support; not a legal opinion
---

# HMRC, Corporation Tax, VAT and payroll

Company-wide scope: apply this reference to Lemuran Ltd’s corporate/internal matters, all services and engagements, and every current or future product as relevant. FAQai.app examples do not limit applicability. See [the Legal Team Charter](20_LEGAL_TEAM_CHARTER.md).

## Scope and owner

Accountant owns tax interpretation and return review; director approves filings and payment. Skills reconcile source ledgers and prepare calculations; they do not infer tax liability from revenue alone. Sources T01–T06 and C02/C04.

## Corporation Tax and accounts — LAW / CONDITIONAL LAW

Confirm trading/active status and tell HMRC when required; check the active-company registration process rather than assuming Companies House registration completes all HMRC setup. Track accounting periods separately from financial years: a Corporation Tax period cannot exceed 12 months, so first accounts may require two returns. Normal payment is nine months and one day after period end; a return is normally due 12 months after period end. Large-company instalments and exceptional periods require separate treatment. [HMRC return obligations](https://www.gov.uk/guidance/company-tax-return-obligations).

The main Corporation Tax rate is 25%; the small-profits rate is 19% for qualifying profits up to £50,000; marginal relief can apply between £50,000 and £250,000. Thresholds adjust for associated companies and short periods, with further eligibility rules. Do not calculate 19% on the first band and 25% only on the excess as if these were personal income-tax bands. [HMRC rates](https://www.gov.uk/corporation-tax-rates).

Reconcile subscriptions, deferred/prepaid income, refunds, payment-processor fees, agency deposits, accrued costs, foreign exchange and bad debts. R&D relief is not automatic because software uses AI; obtain technical eligibility and current filing/notification advice. Payroll, dividends and director loans are distinct tax treatments.

## VAT decision tree

1. Identify contracting entity and establishment; customer country and business/consumer status; actual supply; platform/merchant-of-record role; tax point and currency.
2. Classify automated digital service versus materially human-delivered consultancy. A SaaS-plus-services bundle may need separate or composite-supply analysis.
3. Apply place-of-supply rules and exceptions. B2B services generally follow the customer and B2C generally the supplier, but electronic services and other exceptions change the result. Out-of-scope is not zero-rated. [VAT Notice 741A](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a).
4. Aggregate relevant taxable turnover across FAQai.app and agency activities of the same entity. Include relevant imported reverse-charge services in the registration assessment; overseas model/API/cloud purchases can matter.
5. Assess registration, rate, reverse charge, customer evidence, invoice requirements, return and record duties. Validate foreign VAT/GST/sales tax independently of UK registration.

For a UK-established business, compulsory registration normally arises when taxable turnover exceeds **£90,000** over the rolling last 12 months, or is expected to exceed that amount in the next 30 days alone. The historic test generally requires registration within 30 days of the month end; effective date is the first day of the second month after threshold crossing. The forward test has a different effective date, starting when the expectation arose. Exceptions and non-established-business rules differ. [VAT registration](https://www.gov.uk/register-for-vat).

## Product-specific checks

| Scenario | Required analysis; not a final tax conclusion |
|---|---|
| UK customer purchases FAQai.app | Taxable nature, VAT registration and invoice/consumer price presentation |
| EU business buys SaaS or agency work | Business/location evidence, place of supply, reverse charge and any exceptions |
| EU consumer buys automated SaaS | Destination VAT and possible non-Union OSS; no assumption that UK £90k threshold exempts foreign sales |
| US/India customer | State/country nexus, digital-service classification, withholding and local registration |
| Overseas AI API supplier invoices Lemuran | Imported-service reverse charge and threshold consequences |
| Merchant of record handles sales | Verify it is the actual seller and which taxes/records it handles; reconcile net settlements |

## PAYE and VAT operations

**CONDITIONAL LAW:** assess PAYE registration, real-time payroll reporting, National Insurance, benefits/expenses, workplace pensions and VAT digital-record/compatible-software duties where applicable. VAT return/payment dates depend on the account and scheme; do not hard-code quarterly dates. Use effective-date tables for annual payroll rates, not LLM memory. Reconcile filings with accepted receipts and bank settlement.

**POLICY:** monthly turnover review plus forecast alerts when a large contract is signed; proposed early warning at 80% of threshold is an internal buffer, not law. Calendar due-date alerts at 30/14/7/1 days are internal controls. No production tax-code change without accountant approval.

## Records, tests and acceptance

Retain relevant company financial/tax records normally six years from the end of the last financial year they relate to, longer for specified exceptions. Apply VAT, payroll and pension retention rules by category instead of using six years universally. [Company records](https://www.gov.uk/running-a-limited-company/company-and-accounting-records).

Test a £60k SaaS plus £35k agency UK-taxable rolling turnover: output must aggregate and flag registration assessment. Test £89k turnover plus a large expected 30-day supply: apply forward test separately. Test foreign SaaS with unknown B2B/B2C status: do not assign a tax code. Acceptance: reconciled inputs, dated rules, preparer/reviewer, exceptions and calculation provenance. Verified 2026-10-09.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-09 | Initial UK/Lemuran knowledge pack and implementation specification; draft for review. |

Revision 1.1.0 (2026-10-10): company-wide scope alignment; legal-source verification remains 2026-10-09.

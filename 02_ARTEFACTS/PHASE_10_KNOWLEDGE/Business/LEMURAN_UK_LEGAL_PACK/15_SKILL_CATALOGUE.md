---
id: LEMURAN-UK-15
title: "Machine-readable legal and compliance skill catalogue"
document_type: "Skill Catalogue"
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

# Machine-readable legal and compliance skill catalogue

## Purpose and inheritance

The following **25 capability specifications** cover the operating scope. They are not claims that 22 live skills have been installed. Every entry inherits the workflow, typed envelopes, guardrails and gate rules in [file 14](14_SKILL_IMPLEMENTATION_SPEC.md). All tests named here are defined in [file 16](16_TESTS_AND_ACCEPTANCE.md). Sources are in [file 11](11_AUTHORITY_REGISTER.md).

Use the JSON as the input manifest for a skill generator. Resolve functional inputs from verified facts and access-controlled records, not arbitrary tools selected by a retrieved page. Reviewers named by role must be assigned to actual people before execution.

```json
{
  "schema_version": "1.0.0",
  "pack_version": "1.1.0",
  "verified_on": "2026-10-09",
  "status": "draft_for_review",
  "common_contract": "14_SKILL_IMPLEMENTATION_SPEC.md",
  "common_approval_gates": [
    "G7 for any existing skill overwrite"
  ],
  "skills": [
    {
      "id": "LEMURAN-UK-GOVERNANCE",
      "name": "uk-company-governance",
      "description": "Reconcile company records, decisions and authority",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Director",
      "triggers": [
        "incorporation_change",
        "director_or_psc_change",
        "board_decision",
        "monthly_review"
      ],
      "required_inputs": [
        "company_master",
        "articles",
        "ownership_records",
        "authority_matrix"
      ],
      "outputs": [
        "governance_gap_report",
        "decision_draft",
        "authority_matrix"
      ],
      "knowledge_refs": [
        "02_COMPANY_GOVERNANCE.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "C01",
        "C05",
        "C06",
        "C07"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "Do not infer company identifiers or permit unlawful distributions"
      ],
      "approval_gates": [
        "G1"
      ],
      "acceptance_tests": [
        "director_is_also_psc_requires_separate_check"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-FILINGS",
      "name": "uk-companies-house-calendar",
      "description": "Prepare company filing calendar and review package",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Director / authorised filer",
      "triggers": [
        "year_end",
        "confirmation_review",
        "officer_change",
        "deadline_alert"
      ],
      "required_inputs": [
        "company_number",
        "incorporation_date",
        "periods",
        "register_deadlines",
        "filing_history"
      ],
      "outputs": [
        "filing_calendar",
        "reconciliation",
        "filing_review_package"
      ],
      "knowledge_refs": [
        "02_COMPANY_GOVERNANCE.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "C02",
        "C03",
        "C05"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "Separate first accounts, annual accounts, confirmation and role verification clocks"
      ],
      "approval_gates": [
        "G1"
      ],
      "acceptance_tests": [
        "dormant_company_still_needs_filing_assessment"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-TAX",
      "name": "uk-tax-and-payroll-review",
      "description": "Prepare accountant-reviewed tax and payroll obligations",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Accountant and director",
      "triggers": [
        "accounting_period_end",
        "payroll_event",
        "trading_start",
        "tax_change"
      ],
      "required_inputs": [
        "ledgers",
        "accounting_periods",
        "associated_companies",
        "payroll_facts"
      ],
      "outputs": [
        "tax_workpaper",
        "calendar",
        "accountant_questions"
      ],
      "knowledge_refs": [
        "03_TAX_AND_VAT.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "T01",
        "T04",
        "T05",
        "T06"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "No tax filing or final liability from unverified turnover alone"
      ],
      "approval_gates": [
        "G1"
      ],
      "acceptance_tests": [
        "short_period_adjusts_ct_thresholds"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-VAT",
      "name": "uk-vat-sales-classification",
      "description": "Assess VAT registration and sales/imported-service treatment",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Accountant",
      "triggers": [
        "monthly_turnover",
        "large_new_contract",
        "new_market",
        "supplier_invoice"
      ],
      "required_inputs": [
        "supply_type",
        "establishments",
        "customer_status",
        "ledger_12_months",
        "forecast_30_days",
        "imported_services"
      ],
      "outputs": [
        "vat_assessment",
        "threshold_alert",
        "invoice_review"
      ],
      "knowledge_refs": [
        "03_TAX_AND_VAT.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "T02",
        "T03"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "Aggregate service lines and distinguish out-of-scope from zero-rated"
      ],
      "approval_gates": [
        "G1"
      ],
      "acceptance_tests": [
        "saas_60k_agency_35k_aggregate"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-PRIVACY",
      "name": "uk-privacy-and-ico",
      "description": "Map processing roles, lawful basis, notices and ICO obligations",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Privacy lead",
      "triggers": [
        "new_product",
        "new_purpose",
        "vendor_change",
        "annual_fee_review"
      ],
      "required_inputs": [
        "data_map",
        "purpose_roles",
        "subjects",
        "categories",
        "fee_status",
        "notices"
      ],
      "outputs": [
        "ropa_draft",
        "privacy_gap_report",
        "notice_draft",
        "ico_fee_assessment"
      ],
      "knowledge_refs": [
        "04_PRIVACY_AND_TRANSFERS.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "P01",
        "P02",
        "P04",
        "P11"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "Small size and processor label are not blanket exemptions"
      ],
      "approval_gates": [
        "G2",
        "G3"
      ],
      "acceptance_tests": [
        "billing_controller_customer_content_processor_split"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-DPIA",
      "name": "uk-dpia-and-decision-safeguards",
      "description": "Assess high-risk processing and automated significant decisions",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Privacy lead / counsel / director",
      "triggers": [
        "new_ai_use",
        "sensitive_data",
        "children",
        "significant_decision",
        "material_change"
      ],
      "required_inputs": [
        "use_case",
        "data_map",
        "necessity",
        "alternatives",
        "human_role",
        "risk_evidence"
      ],
      "outputs": [
        "dpia_screen",
        "dpia_draft",
        "safeguard_plan",
        "consultation_assessment"
      ],
      "knowledge_refs": [
        "04_PRIVACY_AND_TRANSFERS.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "P01",
        "P03",
        "P05"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "Use amended ADM provisions; unresolved high risk needs escalation"
      ],
      "approval_gates": [
        "G3"
      ],
      "acceptance_tests": [
        "rubber_stamp_review_not_meaningful"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-RIGHTS",
      "name": "uk-data-rights-and-complaints",
      "description": "Prepare rights and data-protection complaint handling",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Privacy lead",
      "triggers": [
        "rights_request",
        "privacy_complaint"
      ],
      "required_inputs": [
        "received_at",
        "request_text",
        "identity_evidence",
        "role",
        "systems",
        "case_history"
      ],
      "outputs": [
        "case_classification",
        "separate_deadlines",
        "response_draft",
        "search_log"
      ],
      "knowledge_refs": [
        "04_PRIVACY_AND_TRANSFERS.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "P06",
        "P08"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "No unsupported refusal or deadline reset; separate complaint and SAR"
      ],
      "approval_gates": [
        "G4"
      ],
      "acceptance_tests": [
        "combined_sar_complaint_two_clocks"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-TRANSFERS",
      "name": "uk-data-transfer-review",
      "description": "Review suppliers, subprocessors and restricted transfers",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Privacy lead / counsel",
      "triggers": [
        "new_vendor",
        "new_region",
        "remote_support",
        "subprocessor_change"
      ],
      "required_inputs": [
        "legal_entities",
        "roles",
        "data_flows",
        "locations",
        "dpa",
        "mechanism",
        "assessment"
      ],
      "outputs": [
        "supplier_register",
        "transfer_assessment",
        "contract_gap_report"
      ],
      "knowledge_refs": [
        "04_PRIVACY_AND_TRANSFERS.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "P09",
        "P10",
        "P04"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "UK hosting does not exclude overseas access; no SCC-only UK approval"
      ],
      "approval_gates": [
        "G3"
      ],
      "acceptance_tests": [
        "us_support_on_uk_host_requires_analysis"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-PECR",
      "name": "uk-pecr-cookie-review",
      "description": "Assess tracking purposes, exceptions and consent enforcement",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Privacy lead / engineering",
      "triggers": [
        "new_tag",
        "banner_change",
        "analytics_change"
      ],
      "required_inputs": [
        "tag_inventory",
        "purposes",
        "vendors",
        "exception_evidence",
        "network_trace",
        "consent_flow"
      ],
      "outputs": [
        "tag_decisions",
        "cookie_notice_draft",
        "test_report"
      ],
      "knowledge_refs": [
        "05_PECR_AND_MARKETING.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "M01",
        "M04"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "Analytics is not automatically exempt; verify objection and all conditions"
      ],
      "approval_gates": [
        "G2",
        "G6"
      ],
      "acceptance_tests": [
        "statistics_without_objection_fails"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-MARKETING",
      "name": "uk-marketing-permission-review",
      "description": "Review campaign permissions, claims and suppression",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Marketing / privacy lead",
      "triggers": [
        "campaign_draft",
        "lead_import",
        "claim_change"
      ],
      "required_inputs": [
        "audience",
        "subscriber_type",
        "channel",
        "source",
        "consent",
        "suppression",
        "claim_evidence"
      ],
      "outputs": [
        "campaign_review",
        "claims_register",
        "remediation"
      ],
      "knowledge_refs": [
        "05_PECR_AND_MARKETING.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "M02",
        "M03",
        "K03"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "Public business email is not automatic consent; no unauthorised send"
      ],
      "approval_gates": [
        "G2"
      ],
      "acceptance_tests": [
        "sole_trader_not_corporate_subscriber"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-SAAS",
      "name": "uk-saas-contract-review",
      "description": "Draft/review SaaS orders, terms, DPA and SLA consistency",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Counsel / authorised signatory",
      "triggers": [
        "new_plan",
        "enterprise_order",
        "terms_change",
        "renewal"
      ],
      "required_inputs": [
        "customer_status",
        "order",
        "terms",
        "data_map",
        "security_capability",
        "supplier_terms",
        "insurance"
      ],
      "outputs": [
        "terms_draft",
        "deviation_register",
        "obligation_register"
      ],
      "knowledge_refs": [
        "06_CONTRACTS_AND_CONSUMERS.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "K01",
        "K02",
        "P04",
        "L04"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "No unsupported availability, ownership or no-training promise"
      ],
      "approval_gates": [
        "G2"
      ],
      "acceptance_tests": [
        "vendor_retention_conflict_blocks_promise"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-AGENCY",
      "name": "uk-agency-msa-sow",
      "description": "Draft/review agency MSA, SOW and change/acceptance records",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Project owner / signatory",
      "triggers": [
        "new_project",
        "scope_change",
        "milestone",
        "handover"
      ],
      "required_inputs": [
        "customer",
        "msa",
        "scope",
        "deliverables",
        "acceptance_tests",
        "price",
        "data_roles",
        "ip"
      ],
      "outputs": [
        "sow_draft",
        "change_order",
        "acceptance_record",
        "handover_checklist"
      ],
      "knowledge_refs": [
        "06_CONTRACTS_AND_CONSUMERS.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "P04",
        "IP01",
        "IP02",
        "K05"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "No automatic deemed acceptance or unapproved scope expansion"
      ],
      "approval_gates": [
        "G2"
      ],
      "acceptance_tests": [
        "missing_acceptance_criteria_needs_facts"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-CONSUMER",
      "name": "uk-consumer-sales-review",
      "description": "Check consumer price, cancellation, remedy and subscription flows",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Counsel / product owner",
      "triggers": [
        "consumer_launch",
        "checkout_change",
        "renewal",
        "refund_request"
      ],
      "required_inputs": [
        "customer_capacity",
        "supply_class",
        "checkout",
        "terms",
        "cancellation_flow",
        "pricing"
      ],
      "outputs": [
        "consumer_gap_report",
        "flow_tests",
        "terms_changes"
      ],
      "knowledge_refs": [
        "06_CONTRACTS_AND_CONSUMERS.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "K01",
        "K02",
        "K03",
        "K04",
        "L02",
        "L03"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "Do not apply B2B exclusions; future subscription rules remain dated watch"
      ],
      "approval_gates": [
        "G2",
        "G6"
      ],
      "acceptance_tests": [
        "consumer_no_refunds_clause_fails"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-IP",
      "name": "uk-ip-and-licensing",
      "description": "Assess rights chain and code, content, model/data licences",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Legal / engineering",
      "triggers": [
        "new_asset",
        "contractor_delivery",
        "oss_dependency",
        "crawl_source",
        "brand_launch"
      ],
      "required_inputs": [
        "asset_inventory",
        "authors",
        "assignments",
        "licences",
        "intended_use",
        "customer_promises"
      ],
      "outputs": [
        "rights_register",
        "licence_obligations",
        "assignment_gap_report"
      ],
      "knowledge_refs": [
        "07_IP_AND_AI_GOVERNANCE.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "IP01",
        "IP02",
        "IP03"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "Public content and paid contractor work do not establish ownership"
      ],
      "approval_gates": [
        "G2"
      ],
      "acceptance_tests": [
        "contractor_invoice_not_assignment"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-AI",
      "name": "uk-ai-risk-release",
      "description": "Prepare AI use-case classification, evaluation and release decision",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Product owner / counsel / privacy",
      "triggers": [
        "new_model",
        "new_tool",
        "new_use",
        "material_drift",
        "eu_launch"
      ],
      "required_inputs": [
        "intended_use",
        "users",
        "territories",
        "permissions",
        "evaluation_results",
        "data_roles"
      ],
      "outputs": [
        "ai_system_card",
        "risk_register",
        "release_review"
      ],
      "knowledge_refs": [
        "07_IP_AND_AI_GOVERNANCE.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "A01",
        "A02",
        "A03",
        "A04",
        "P03"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "Internal risk labels are not EU legal classification; no autonomous high-impact approval"
      ],
      "approval_gates": [
        "G3",
        "G6"
      ],
      "acceptance_tests": [
        "model_change_invalidates_related_tests"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-SECURITY",
      "name": "uk-security-and-incident",
      "description": "Assess security commitments and incident response",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Incident lead / privacy / director",
      "triggers": [
        "release",
        "security_event",
        "supplier_incident",
        "restore_test"
      ],
      "required_inputs": [
        "architecture",
        "controls",
        "logs_minimised",
        "awareness_time",
        "roles",
        "contracts",
        "impact"
      ],
      "outputs": [
        "security_schedule",
        "incident_record",
        "notification_drafts",
        "recovery_evidence"
      ],
      "knowledge_refs": [
        "08_SECURITY_PEOPLE_AND_INSURANCE.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "S01",
        "P07",
        "P01"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "Do not give processors a universal 72-hour grace period"
      ],
      "approval_gates": [
        "G4",
        "G6"
      ],
      "acceptance_tests": [
        "weekend_breach_clock_continues"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-PEOPLE",
      "name": "uk-people-contractor-compliance",
      "description": "Assess engagement status and onboarding/offboarding duties",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "HR / employment adviser / director",
      "triggers": [
        "hire",
        "contractor_start",
        "role_change",
        "exit"
      ],
      "required_inputs": [
        "working_practices",
        "jurisdictions",
        "status_evidence",
        "contract",
        "payroll",
        "ip",
        "access"
      ],
      "outputs": [
        "engagement_review",
        "onboarding_checklist",
        "offboarding_record"
      ],
      "knowledge_refs": [
        "08_SECURITY_PEOPLE_AND_INSURANCE.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "H01",
        "H02",
        "H05",
        "H06",
        "T06"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "No status conclusion from contract title; check phased reforms"
      ],
      "approval_gates": [
        "G5",
        "G6"
      ],
      "acceptance_tests": [
        "contractor_label_not_status_proof"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-INSURANCE",
      "name": "uk-insurance-commitment-review",
      "description": "Map legal/contract insurance needs against policy cover",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Director / broker",
      "triggers": [
        "hire",
        "renewal",
        "new_contract",
        "claim_circumstance"
      ],
      "required_inputs": [
        "staff_status",
        "policy_wording",
        "limits",
        "territories",
        "exclusions",
        "contract_requirements"
      ],
      "outputs": [
        "coverage_matrix",
        "broker_questions",
        "renewal_alert"
      ],
      "knowledge_refs": [
        "08_SECURITY_PEOPLE_AND_INSURANCE.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "H03",
        "H04"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "No inference of AI coverage or limited-company family exemption"
      ],
      "approval_gates": [
        "G5"
      ],
      "acceptance_tests": [
        "expired_policy_fails_customer_claim"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-INTERNATIONAL",
      "name": "uk-international-market-screen",
      "description": "Screen new territories for local law, taxes, transfers and sanctions",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Director / counsel / accountant",
      "triggers": [
        "new_country",
        "new_sector",
        "new_counterparty"
      ],
      "required_inputs": [
        "country",
        "customer_type",
        "use_case",
        "establishment",
        "data_flows",
        "ownership"
      ],
      "outputs": [
        "market_entry_checklist",
        "country_matrix",
        "specialist_referrals"
      ],
      "knowledge_refs": [
        "09_INTERNATIONAL_DISPUTES_AND_RECORDS.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "I01",
        "T03",
        "P09",
        "A03"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "UK pack cannot certify US/India compliance; flag local-law unknowns"
      ],
      "approval_gates": [
        "G2",
        "G3"
      ],
      "acceptance_tests": [
        "uk_law_clause_not_foreign_consumer_waiver"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-DISPUTES",
      "name": "uk-dispute-and-legal-hold",
      "description": "Triage disputes, preserve evidence and prepare response",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Counsel / authorised owner",
      "triggers": [
        "complaint",
        "claim",
        "regulator_letter",
        "payment_dispute"
      ],
      "required_inputs": [
        "received_document",
        "service_date",
        "contract",
        "facts",
        "forum",
        "insurance",
        "evidence_map"
      ],
      "outputs": [
        "case_record",
        "deadline_questions",
        "hold_draft",
        "response_draft"
      ],
      "knowledge_refs": [
        "09_INTERNATIONAL_DISPUTES_AND_RECORDS.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "K05",
        "P08",
        "L04"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "No admission, settlement or limitation assumption without review"
      ],
      "approval_gates": [
        "G4",
        "G5"
      ],
      "acceptance_tests": [
        "court_letter_urgent_not_normal_support"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-RETENTION",
      "name": "uk-records-retention",
      "description": "Create category-specific retention and deletion decisions",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Data owner / privacy / legal",
      "triggers": [
        "new_record_class",
        "expiry",
        "erasure",
        "hold_release"
      ],
      "required_inputs": [
        "inventory",
        "purpose",
        "law_contract",
        "retention_rules",
        "holds",
        "systems_backups"
      ],
      "outputs": [
        "retention_schedule",
        "deletion_candidates",
        "hold_review",
        "execution_evidence"
      ],
      "knowledge_refs": [
        "09_INTERNATIONAL_DISPUTES_AND_RECORDS.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "C04",
        "L05",
        "L06",
        "H06",
        "P01"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "No blanket six-year rule or deletion across a legal hold"
      ],
      "approval_gates": [
        "G6"
      ],
      "acceptance_tests": [
        "hold_blocks_only_scoped_deletion"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-MONITORING",
      "name": "uk-legal-source-monitor",
      "description": "Review primary-source changes and affected controls",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "additional territories only after scope review"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Compliance maintainer / counsel",
      "triggers": [
        "monthly_review",
        "authority_update",
        "source_stale"
      ],
      "required_inputs": [
        "source_register",
        "as_of_date",
        "current_text",
        "prior_version",
        "affected_controls"
      ],
      "outputs": [
        "change_log",
        "impact_assessment",
        "review_tasks"
      ],
      "knowledge_refs": [
        "10_OPERATIONS_AND_REVIEW.md",
        "11_AUTHORITY_REGISTER.md"
      ],
      "source_ids": [
        "C05",
        "H02",
        "K04",
        "IP03",
        "A03"
      ],
      "dependencies": [
        "validated_business_facts",
        "common_execution_contract"
      ],
      "workflow_ref": "14_SKILL_IMPLEMENTATION_SPEC.md",
      "guardrails": [
        "Consultation or expected date is not commenced law; no auto-publication"
      ],
      "approval_gates": [
        "G2"
      ],
      "acceptance_tests": [
        "proposal_not_binding_requirement"
      ],
      "verified_on": "2026-10-09",
      "review_triggers": [
        "relevant_law_change",
        "material_business_change",
        "before_sensitive_action"
      ],
      "scope_rule": "Apply according to matter facts; product-specific examples are non-exclusive."
    },
    {
      "id": "LEMURAN-UK-INTAKE",
      "name": "lemuran-legal-matter-intake",
      "description": "Triage company-wide legal matters and assign owners, deadlines and specialist routes",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "other jurisdictions after assessment"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Director / legal operations lead",
      "triggers": [
        "new_matter",
        "legal_notice",
        "business_change"
      ],
      "required_inputs": [
        "request",
        "entity_id",
        "scope_type",
        "received_at",
        "affected_scope_refs"
      ],
      "outputs": [
        "matter_register_entry",
        "triage",
        "deadline_alerts",
        "assigned_workflow"
      ],
      "knowledge_refs": [
        "20_LEGAL_TEAM_CHARTER.md",
        "14_SKILL_IMPLEMENTATION_SPEC.md"
      ],
      "source_ids": [],
      "obligation_class": "POLICY",
      "dependencies": [
        "common_execution_contract"
      ],
      "workflow_ref": "20_LEGAL_TEAM_CHARTER.md",
      "guardrails": [
        "Do not route every matter as a SaaS contract or imply an AI agent holds professional qualifications."
      ],
      "approval_gates": [
        "G4"
      ],
      "acceptance_tests": [
        "corporate_matter_without_product_routes"
      ],
      "verified_on": null,
      "updated_on": "2026-10-10",
      "review_triggers": [
        "organisational_change",
        "new_scope",
        "authority_change"
      ]
    },
    {
      "id": "LEMURAN-UK-PORTFOLIO",
      "name": "lemuran-product-service-legal-onboarding",
      "description": "Assess each new or changed product, service and engagement against company controls",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "other jurisdictions after assessment"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Product/service owner and legal lead",
      "triggers": [
        "new_product",
        "new_service",
        "new_engagement",
        "material_change",
        "retirement"
      ],
      "required_inputs": [
        "portfolio_record",
        "business_model",
        "countries",
        "customer_types",
        "data_map",
        "capabilities"
      ],
      "outputs": [
        "applicability_matrix",
        "legal_readiness_plan",
        "scope_specific_document_requirements"
      ],
      "knowledge_refs": [
        "20_LEGAL_TEAM_CHARTER.md",
        "14_SKILL_IMPLEMENTATION_SPEC.md"
      ],
      "source_ids": [],
      "obligation_class": "POLICY",
      "dependencies": [
        "common_execution_contract"
      ],
      "workflow_ref": "20_LEGAL_TEAM_CHARTER.md",
      "guardrails": [
        "Never copy another product approval or invent product facts; shared policies do not imply identical duties."
      ],
      "approval_gates": [
        "G2",
        "G3"
      ],
      "acceptance_tests": [
        "new_product_not_faqai_supported"
      ],
      "verified_on": null,
      "updated_on": "2026-10-10",
      "review_triggers": [
        "organisational_change",
        "new_scope",
        "authority_change"
      ]
    },
    {
      "id": "LEMURAN-UK-DOCUMENTS",
      "name": "lemuran-official-legal-document-control",
      "description": "Prepare, review, approve and track company legal documents and obligations",
      "version": "1.0.0",
      "status": "draft",
      "jurisdictions": [
        "UK",
        "other jurisdictions after assessment"
      ],
      "service_lines": [
        "corporate",
        "internal_operations",
        "all_current_and_future_products",
        "all_services_and_engagements"
      ],
      "owner_role": "Legal operations / authorised signatory",
      "triggers": [
        "document_request",
        "negotiation",
        "approval",
        "signature",
        "renewal",
        "supersession"
      ],
      "required_inputs": [
        "matter_id",
        "document_type",
        "entity_details",
        "scope_refs",
        "facts",
        "authority",
        "existing_versions"
      ],
      "outputs": [
        "controlled_draft",
        "review_package",
        "document_register",
        "obligation_entries"
      ],
      "knowledge_refs": [
        "20_LEGAL_TEAM_CHARTER.md",
        "14_SKILL_IMPLEMENTATION_SPEC.md"
      ],
      "source_ids": [],
      "obligation_class": "POLICY",
      "dependencies": [
        "common_execution_contract"
      ],
      "workflow_ref": "20_LEGAL_TEAM_CHARTER.md",
      "guardrails": [
        "Draft generation is not signature, filing, publication or proof of legal effectiveness."
      ],
      "approval_gates": [
        "G1",
        "G2",
        "G4"
      ],
      "acceptance_tests": [
        "changed_document_invalidates_release"
      ],
      "verified_on": null,
      "updated_on": "2026-10-10",
      "review_triggers": [
        "organisational_change",
        "new_scope",
        "authority_change"
      ]
    }
  ],
  "updated_on": "2026-10-10",
  "scope": "Lemuran Ltd company-wide legal and compliance function",
  "known_product_examples": [
    "FAQai.app"
  ],
  "common_required_inputs": [
    "matter_id",
    "entity_id",
    "scope_type",
    "affected_scope_refs"
  ]
}
```

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-09 | Initial UK/Lemuran knowledge pack and implementation specification; draft for review. |

Revision 1.1.0 (2026-10-10): company-wide scope alignment; legal-source verification remains 2026-10-09.

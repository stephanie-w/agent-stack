# Code Improvement Plan for [File/Module Name]

## Date: [YYYY-MM-DD]
## Reviewer: [Your Name/Agent Name]
## Target File/Module: [Path to File/Module]

---

## 1. Identified Issues

List specific issues found during the code review. Categorize them for clarity (e.g., Bug, Readability, Performance, Security, Maintainability).

### Example: Readability
- Line 123: Variable `x` is not descriptive; consider renaming to `customer_id`.
- Function `process_data` is too long; consider refactoring into smaller, single-responsibility functions.

### Example: Performance
- Line 45: Loop iterating over a database query result; consider batching or optimizing query.

---

## 2. Proposed Changes / Recommendations

For each identified issue, provide a concrete recommendation or proposed change.

### Example: Readability
- **Variable Renaming:** Rename `x` to `customer_id` in `get_user_info` function.
- **Refactoring `process_data`:**
    - Extract data loading into `_load_raw_data`.
    - Extract data transformation into `_transform_data`.
    - Extract data saving into `_save_processed_data`.

### Example: Performance
- **Optimize Query:** Rewrite the query in `fetch_all_records` to include necessary joins and filters to reduce the number of database calls.

---

## 3. Action Items

List actionable tasks based on the proposed changes. Assign priorities (High, Medium, Low) and estimated effort (Small, Medium, Large).

- [ ] **High / Small:** Rename `x` to `customer_id` in `get_user_info`.
- [ ] **Medium / Large:** Refactor `process_data` into three smaller functions: `_load_raw_data`, `_transform_data`, `_save_processed_data`.
- [ ] **High / Medium:** Optimize `fetch_all_records` query.

---

## 4. Discussion Points

Any questions, ambiguities, or areas requiring further discussion with the original author or team.

- Clarify expected behavior for negative input values in `calculate_discount`.
- Discuss the impact of performance optimization on deployment strategy.

---

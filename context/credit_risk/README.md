# Credit Risk - Context Library

**Domain:** Credit risk assessment, underwriting, and portfolio management

## 📂 What's Here

This folder contains business logic, gotchas, and tribal knowledge for credit risk analytics.

### Current Documentation

*Coming soon - contribute your knowledge!*

## 🎯 Common Use Cases

- Application risk scoring
- Underwriting decision logic
- Portfolio performance analysis
- Default prediction models
- Credit limit calculations

## 📝 Contributing

**To add knowledge to this library:**

1. Create a markdown file (e.g., `gotchas.md`, `underwriting_rules.md`)
2. Document business logic, edge cases, or query patterns
3. Open a PR with your additions
4. Once merged, AI agents have permanent context

### Example Contribution

**File:** `gotchas.md`

```markdown
## Application Status Field

- **Pre-2023:** `status` can be NULL (legacy data issue)
- **Post-2023:** `status` always populated
- **For queries:** Use `COALESCE(status, 'UNKNOWN')` for pre-2023 data
```

## 🔗 Related Resources

- [Strategy & Analytics dbt Models](../strategy_and_analytics/dbt/)
- Risk team documentation (add links)
- Compliance requirements (add links)

---

*This folder is owned and maintained by the Credit Risk team*

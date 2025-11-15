# Analytics Context Library

**What problem are you working on?**

This is a living knowledge base that gives AI agents complete context about your data stack, business logic, and tribal knowledge.

## 🗂️ Navigate by Domain

Choose the domain that matches your problem:

### [Strategy & Analytics](strategy_and_analytics/)
Auto-generated dbt model documentation + business logic
- **224 production models** from Snowflake
- Revenue, risk, marketing, customer support marts
- [Browse dbt models →](strategy_and_analytics/dbt/)

### [Credit Risk](credit_risk/)
Credit risk assessment, underwriting, portfolio management
- Application risk scoring logic
- Underwriting decision rules
- Portfolio performance analysis
- *Team-maintained documentation*

### [Practice Intelligence](practice_intelligence/)
Healthcare practice operations and provider analytics
- Provider scheduling logic
- Practice performance metrics
- Patient flow optimization
- *Team-maintained documentation*

### [RevOps](revops/)
Revenue operations and sales analytics
- Revenue recognition rules
- Sales pipeline definitions
- Customer lifecycle metrics
- *Team-maintained documentation*

---

## 💡 How to Use This Library

### For AI Agents
1. Start here: "What problem are you working on?"
2. Navigate to the relevant domain folder
3. Read the domain README for context pointers
4. Access specific documentation files

### For Analysts
- **Browse:** Navigate folders to find existing knowledge
- **Validate:** Check AI output against documented rules
- **Contribute:** Add your tribal knowledge via PR

### For Teams
- **Own your folder:** Maintain documentation for your domain
- **Document once:** AI uses your rules forever
- **Validate AI:** Against standards YOU wrote

---

## 📝 Contributing Knowledge

**To add to this library:**

1. Navigate to your team's domain folder
2. Create a markdown file documenting:
   - Business logic
   - Gotchas and edge cases
   - Common query patterns
   - Calculation methodologies
   - Data quality issues
3. Open a PR with your additions
4. Once merged, AI agents have permanent context

### Example Contribution

**File:** `credit_risk/gotchas.md`

```markdown
## Application Status Field

- **Pre-2023:** `status` can be NULL (legacy data issue)
- **Post-2023:** `status` always populated
- **For queries:** Use `COALESCE(status, 'UNKNOWN')` for pre-2023 data
```

AI now knows this forever. Every query follows this rule.

---

## 🏗️ Repository Structure

```
context/
├── README.md (you are here - "What problem are you working on?")
│
├── strategy_and_analytics/
│   └── dbt/                    Auto-synced from dbt Cloud
│       └── prod/               224 production models
│
├── credit_risk/                Team-maintained
│   └── README.md
│
├── practice_intelligence/      Team-maintained
│   └── README.md
│
└── revops/                     Team-maintained
    └── README.md
```

---

## 🎯 Why This Works

### For AI
- Complete context about data, business logic, gotchas
- Navigates via hierarchical READMEs
- No hallucinations about your data
- Accuracy improves as library grows

### For Teams
- Own their domain knowledge
- Validate AI against their own rules
- Contribute once, AI uses forever
- Knowledge preserved when people leave

### For New Hires
- Library = onboarding documentation
- AI + library = productive from week 1
- Learn institutional knowledge immediately

---

## 📊 Auto-Generated vs Manual

| Folder | Type | Update Method |
|--------|------|---------------|
| `strategy_and_analytics/dbt/` | Auto-generated | dbt Discovery API sync |
| `credit_risk/` | Manual | Team PRs |
| `practice_intelligence/` | Manual | Team PRs |
| `revops/` | Manual | Team PRs |

---

**Built with:** MCP (Model Context Protocol) | dbt Discovery API | GitHub

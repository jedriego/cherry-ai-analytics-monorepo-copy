# Analytics Context Library

**What problem are you working on?**

This is the navigation hub for AI agents and analysts to find relevant data context, business logic, and tribal knowledge.

## 🗺️ Browse by Domain

### [Strategy Analytics](strategy_analytics/)
- **Production dbt models** (224 models across 15 schemas)
- Revenue, risk, servicing, marketing, and support analytics
- Auto-generated from dbt Cloud Discovery API
- **Start here** for most analytics questions

## 🎯 How AI Agents Use This

1. **AI reads this README** → "What domain does this problem relate to?"
2. **Navigates to domain folder** → e.g., `strategy_analytics/`
3. **Reads domain README** → Finds relevant schemas (revenue_marts, risk_marts, etc.)
4. **Reads schema README** → Gets list of models grouped by tags
5. **Reads specific model.md** → Full schema, columns, dependencies, descriptions

**No vector search. No RAG. Just hierarchical file navigation.**

## 📚 How Humans Use This

1. **Browse on GitHub** → Click through folders to explore data models
2. **Search by keyword** → Use GitHub search for tags, column names, descriptions
3. **Contribute knowledge** → Add `gotchas.md`, `patterns.md` alongside models via PR

## ✍️ Contributing Business Logic

Found a data quirk? Document it next to the relevant schema:

```bash
# Example: Adding gotchas for revenue models
cd strategy_analytics/prod/revenue_marts/
nano gotchas.md  # Document edge cases, null handling, date ranges, etc.
git commit -m "Add revenue gotchas for Q4 reporting"
```

Once merged, AI agents have permanent context about your tribal knowledge.

## 🔄 How This Stays Fresh

- **dbt models**: Auto-updated weekly from dbt Cloud Discovery API
- **Business logic**: Teams contribute via PR
- **Automation**: `scripts/generate_context_folders.py` regenerates structure

---

*Navigate to a domain to get started →*

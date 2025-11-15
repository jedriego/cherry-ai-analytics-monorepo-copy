# Cherry AI Analytics Monorepo

**Living knowledge base + AI agent configuration for analytics teams**

## 🎯 What This Is

A **world-wide map of our analytics infrastructure** - giving AI agents complete context about your data stack.

This is an MVP demonstrating:
1. **Auto-generated documentation** - 224 dbt production models synchronized from dbt Cloud
2. **Problem-based navigation** - Hierarchical folder structure organized by domain
3. **Team-owned knowledge** - Each team maintains their own context folder

**No RAG. No vectors. Just hierarchical file navigation.**

---

## 🚀 Quick Start

### Initialize AI Access

**First, load the repository context in your AI tool:**

```
Open jedriego/cherry-ai-analytics-monorepo-copy using the github mcp server please
```

This gives the AI agent access to all context files and documentation.

### What's Working Now (MVP)

**Browse the knowledge base:**
1. Open `context/README.md` - Start with "What problem are you working on?"
2. Navigate to `context/strategy_and_analytics/dbt/prod/`
3. Explore 224 documented models across 15 schemas
4. Each model has full schema, columns, descriptions, lineage

**Regenerate documentation:**
```bash
rm -rf context/strategy_and_analytics
python scripts/how_to_update_dbt_metadata/update_dbt_metadata.py
python scripts/how_to_update_dbt_metadata/generate_context_folders.py
```

### What's Next (Full AI Integration)

**For AI-powered queries, you'll need:**
1. MCP configuration (Snowflake + GitHub access)
2. AI tool setup (Claude Code, Cursor, or Codex)
3. Polished context READMEs (currently MVP quality)

See `configs/` folder for MCP setup templates.

**The vision:** AI reads this context → generates accurate queries → you validate against documented rules

---

## 📁 What's Inside

```
cherry-ai-analytics-monorepo/
├── context/                    The knowledge library
│   ├── README.md              "What problem are you working on?"
│   │
│   ├── strategy_and_analytics/
│   │   └── dbt/               ✅ 224 auto-generated production models
│   │       └── prod/          Revenue, risk, marketing, support marts
│   │
│   ├── credit_risk/           Team-maintained (placeholder)
│   ├── practice_intelligence/ Team-maintained (placeholder)
│   └── revops/                Team-maintained (placeholder)
│
├── scripts/                    Repository automation
│   └── how_to_update_dbt_metadata/
│       ├── update_dbt_metadata.py      Fetch from dbt Cloud API
│       └── generate_context_folders.py  Build folder structure
│
└── configs/                    Pre-configured MCP setups
    └── (Snowflake + GitHub access)
```

---

## 🎬 The Demo

### What We Built

**Automated dbt → GitHub sync**
- Fetches all 1,265 models from dbt Cloud Discovery API
- Filters to 224 production models
- Generates hierarchical folder structure
- Each model gets full documentation (schema, columns, lineage, descriptions)
- Updates on-demand with one command

**Problem-based navigation structure**
- Root: "What problem are you working on?"
- Domains: strategy_and_analytics, credit_risk, practice_intelligence, revops
- Each domain has README guiding to relevant models

**The world-wide map:**
- `context/strategy_and_analytics/dbt/prod/` = Complete map of production data warehouse
- 15 schemas (revenue_marts, risk_marts, core_marts, etc.)
- 224 fully documented models
- AI agents can navigate this without hallucinating

---

## 🔄 How to Update

Regenerate the dbt documentation:

```bash
# Delete old structure
rm -rf context/strategy_and_analytics

# Fetch fresh metadata from dbt Cloud
python scripts/how_to_update_dbt_metadata/update_dbt_metadata.py

# Generate folder structure
python scripts/how_to_update_dbt_metadata/generate_context_folders.py
```

**Result:** Fresh documentation in `context/strategy_and_analytics/dbt/prod/`

---

## 💡 Why This Matters

### The Problem
- AI agents hallucinate about your data
- No context about business logic, gotchas, or data structure
- Teams don't trust AI output

### This Solution
- **Complete map** of your data warehouse (224 models)
- **Hierarchical navigation** - AI knows where to look
- **Auto-updated** - Always current with production
- **Team-owned** - Each domain maintains their knowledge

### The Validation Model
1. AI reads documented rules (from this repo)
2. AI generates code following those rules
3. Analyst validates against rules THEY (or their team) wrote
4. Trust = validating against YOUR documentation, not blind faith

---

## 📊 Current State

### ✅ What's Complete

**Phase 1: Auto-Generated Base**
- [x] dbt Cloud Discovery API integration
- [x] 224 production models documented
- [x] Hierarchical folder structure
- [x] Problem-based navigation READMEs
- [x] One-command regeneration workflow

### 🚧 What's Next

**Phase 2: Team Knowledge (Manual)**
- [ ] Teams add gotchas.md, business_logic.md to their folders
- [ ] Document edge cases, calculation methods, data quirks
- [ ] Build the tribal knowledge layer

**Phase 3: AI-Assisted Documentation**
- [ ] Capture Slack conversations automatically
- [ ] AI generates documentation from tribal knowledge
- [ ] 30-second human review → merge
- [ ] Make documentation a byproduct, not extra work

---

## 📝 How to Contribute Knowledge

### The Reality: Documentation is Hard

Let's be honest - asking people to write documentation rarely works. Everyone's too busy.

**The solution:** Make it a byproduct of existing work.

### Two Ways to Add Knowledge

#### 1. Auto-Generated (Zero Effort) ✅
- **dbt models** already handled
- Auto-syncs weekly from dbt Cloud
- You don't do anything

#### 2. AI-Assisted (30 seconds)
Capture tribal knowledge from Slack:

**The Flow:**
1. Expert explains something in Slack (normal work)
2. AI captures → generates documentation
3. You review (30 sec) → approve
4. Knowledge preserved forever

**Example:**

*Slack:* "Revenue is NULL for Q1 2023 because of billing migration. Use legacy_revenue table."

*AI generates PR:* Proper markdown with issue, cause, solution

*You:* "Looks good" → Merge

See [THOUGHTS.md](THOUGHTS.md) for why this scales.

### Traditional Way (Optional)

Power users can still PR directly:
1. Go to your team's folder (e.g., `context/credit_risk/`)
2. Create `gotchas.md` or `business_logic.md`
3. Document edge cases, calculations, quirks
4. Open PR → merge

---

## 🔗 Additional Documentation

- **[VISION.md](personal_thoughts/VISION.md)** - Task-based roadmap (5 phases to 75% adoption)
- **[THOUGHTS.md](personal_thoughts/THOUGHTS.md)** - Why AI-assisted documentation is the scalability unlock
- **[context/README.md](context/README.md)** - Entry point for problem-based navigation

---

## 🎯 The Vision (3 Months)

**Goal:** 18/24 people (75%) actively using AI workflows

**How:**
1. **Week 1-2:** Build MVP ✅ (YOU ARE HERE)
2. **Week 3-4:** Prove with your team
3. **Week 4+:** Champions multiply to other teams

**Success = Making this the single source of truth for analytics context**

---

**Built with:** MCP (Model Context Protocol) | dbt Discovery API | GitHub

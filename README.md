# Cherry AI Analytics Monorepo

**Living knowledge base + AI agent configuration for analytics teams**

## 🎯 The Vision

Deploy AI playbooks achieving **75% adoption** across technical teams (Analytics, Risk, RevOps) in 3 months.

**Target:** 18/24 people actively using AI workflows

## 🏗️ What This Is

A GitHub monorepo that gives AI agents complete context about your data stack, business logic, and tribal knowledge. Not just an AI tool—**a living knowledge base** that:

1. Captures institutional knowledge across teams
2. Makes AI agents accurate through hierarchical context
3. Enables validation against team-documented standards
4. Scales expertise across all analysts
5. Compounds value over time

**No RAG. No vectors. Just hierarchical file navigation via READMEs.**

## 📁 Repository Structure

```
cherry-ai-analytics-monorepo/
├── README.md (you are here)
├── VISION.md (detailed implementation plan)
│
├── configs/ (Pre-configured AI tool setups)
│   ├── README.md (setup instructions)
│   ├── claude-code-settings.json
│   ├── cursor-settings.json
│   ├── codex-settings.toml
│   └── snowflake_mcp_config.yaml
│
└── context/ (coming soon - the knowledge library)
    ├── README.md ("What problem are you working on?")
    ├── credit_risk/
    ├── practice_intelligence/
    ├── strategy_analytics/ (auto-generated from 1,200 dbt models)
    └── revops/
```

## 🚀 Quick Start

### For Analysts (10 minutes)

1. **Install AI tool:**
   - [Claude Code](https://code.claude.com) (CLI workflows)
   - [Cursor](https://cursor.sh) (IDE workflows)
   - Codex (enterprise)

2. **Configure Snowflake + GitHub access:**
   ```bash
   cd configs
   # Follow README.md setup instructions
   ```

3. **Start using:**
   ```
   "Show me top 10 customers by revenue"
   "Query the semantic view for Q4 metrics"
   "Search our dbt models for churn logic"
   ```

## 🧠 The Core Insight

**Teams maintain their GitHub section = Teams validate AI output against THEIR OWN documentation**

### Validation Flow

1. AI reads team's documented rules (e.g., `credit_risk/gotchas.md`)
2. AI generates code following those rules
3. Analyst validates output against the rules THEY wrote
4. If AI missed something → PR new rule → AI learns it forever

**The library becomes the validation checklist.**

Not "trust the AI" but "validate against YOUR documentation."

## 📊 Current Progress

### ✅ Phase 1: Configuration (COMPLETE)

- [x] Pre-configured MCP setups for Snowflake queries
- [x] GitHub MCP for repository access
- [x] RSA key authentication templates
- [x] Auto-approval settings for smooth workflow
- [x] Multi-tool support (Claude Code, Cursor, Codex)

### 🚧 Phase 2: Knowledge Library (IN PROGRESS)

- [ ] Create `context/` folder structure
- [ ] Build dbt Discovery API → GitHub automation
- [ ] Generate `strategy_analytics/` from 1,200 models
- [ ] Write domain READMEs with navigation patterns
- [ ] Document initial gotchas and business logic

### 📅 Phase 3: Team Rollout (PLANNED)

- [ ] Deploy to Strategy Analytics team
- [ ] Measure velocity and accuracy improvements
- [ ] Recruit champions from Risk and RevOps
- [ ] Scale to 75% adoption

## 🛠️ Technical Stack

| Component | Technology |
|-----------|------------|
| **AI Agent** | Codex (enterprise) / Claude Code |
| **Configuration** | Pre-configured MCP with Snowflake + GitHub |
| **Context Library** | GitHub monorepo with semantic layer |
| **Automation** | dbt Discovery API → GitHub sync |
| **Access Pattern** | Problem-based hierarchical navigation |

## 🎓 For New Contributors

### Adding to the Knowledge Library

1. Navigate to your team's folder (e.g., `context/credit_risk/`)
2. Document business logic, gotchas, query patterns
3. Open PR with your additions
4. Once merged, AI has permanent context

### Example Contribution

**File:** `context/credit_risk/gotchas.md`

```markdown
## Application Status Field

- **Pre-2023:** `status` can be NULL (legacy data issue)
- **Post-2023:** `status` always populated
- **For queries:** Use `COALESCE(status, 'UNKNOWN')` for pre-2023 data
```

AI now knows this forever. Every query generated follows this rule.

## 📈 Success Metrics

**Weekly tracking:**
- Active users (who used it this week)
- Library contributions (PRs merged)
- Success stories (shipped faster/better)
- Velocity metrics (before/after AI adoption)

**3-month goal:** 18/24 people actively using AI workflows

## 🔗 Key Resources

- **Full Vision:** See [VISION.md](VISION.md) for complete implementation plan
- **Setup Guide:** See [configs/README.md](configs/README.md) for installation
- **Support:** #ai-analytics Slack channel

## 💡 Why This Works

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

**Built with:** MCP (Model Context Protocol) | Snowflake Labs MCP | GitHub Copilot MCP | dbt Discovery API

# AI Playbook Implementation Plan

## The OKR

**Objective:** Deploy AI playbooks achieving 75% user adoption across technical teams (Analytics, Risk, RevOps)

- **Timeline:** 3 months
- **Target:** 18/24 people actively using AI workflows

---

## The Solution

### Technical Stack

| Component | Technology |
|-----------|------------|
| **AI Agent** | Codex (enterprise) or Claude Code |
| **Configuration** | Pre-configured MCP setup with keys |
| **Context Library** | GitHub monorepo with semantic layer |
| **Access** | GitHub MCP integration for AI navigation |

---

## The Context Library Architecture

### What It Is

A GitHub monorepo that gives AI agents complete context about your data stack, business logic, and tribal knowledge.

### Folder Structure

```
analytics-context/
├── README.md ("What problem are you working on?")
│
├── credit_risk/
│   ├── README.md
│   ├── applications/
│   ├── underwriting/
│   └── gotchas.md
│
├── practice_intelligence/
│   ├── README.md
│   ├── scheduling/
│   └── providers/
│
├── strategy_analytics/ (1,200 dbt models - YOUR TEAM)
│   ├── README.md
│   ├── finance/
│   ├── marketing/
│   └── product/
│
└── revops/
    ├── README.md
    └── revenue_recognition/
```

### Navigation Pattern

Problem-based hierarchy:

1. **Root README:** "What problem are you working on?"
2. **Domain folder:** Navigate to relevant team/domain
3. **Sub-domain README:** Guides to specific context files
4. **AI has complete context**

**No RAG. No vectors. Just hierarchical file navigation via READMEs.**

---

## What Goes in the Library

### Auto-Generated (Your Team)

**dbt Discovery API → GitHub automation**

- 1,200 models exploded into folder structure
- Schema, lineage, descriptions from dbt metadata
- Updates daily/weekly via automated PR
- `strategy_analytics/` folder stays synchronized automatically

### Manually Maintained (All Teams)

Each team owns and documents their domain:

- Business logic explanations
- Gotchas ("status can be NULL pre-2023")
- Common query patterns
- Domain-specific rules
- Tribal knowledge
- Compliance requirements

**Teams contribute via PR to their folder**

---

## Why This Solves the Trust Problem

### The Key Insight

**Teams maintain their GitHub section = Teams validate AI output against THEIR OWN documentation**

### The Validation Flow

1. AI reads team's documented rules (e.g., `credit_risk/gotchas.md`)
2. AI generates code following those rules
3. Analyst validates output against the rules THEY wrote
4. If AI missed something → PR new rule → AI learns it forever

**The library becomes the validation checklist.**

### Trust Message

✅ Not "trust the AI"
✅ But "validate against YOUR documentation"
✅ You control accuracy by documenting your rules
✅ More documentation = more accurate AI
✅ Your team's standards, enforced consistently

Risk teams can audit AI output against their own compliance requirements.

---

## Technical Setup

### Per-User Setup (~10 minutes)

1. Download Codex/Claude Code
2. Install pre-configured MCP file (you provide)
3. Point GitHub MCP to analytics-context repo
4. Done

### The Automation (Your Build)

**dbt → GitHub sync (runs daily/weekly):**

```python
1. Hit dbt Discovery API
2. Generate folder structure from 1,200 models
3. Create/update model.md files (schema, lineage, descriptions)
4. Create/update domain READMEs
5. Open PR: "dbt metadata sync - {date}"
6. Auto-merge or team reviews
```

**Manual contributions:** Teams PR their knowledge → you review → merge → AI has updated context

---

## The Build Plan

### Week 1-2: Build MVP

- [ ] Create GitHub repo: `analytics-context`
- [ ] Build root README with problem-based navigation
- [ ] Create folder structure for all domains
- [ ] Build dbt Discovery API → GitHub automation script
- [ ] Generate `strategy_analytics/` from your 1,200 dbt models
- [ ] Write core documentation (style guide, initial gotchas)
- [ ] Test automation (run script, verify PR generation)

### Week 3-4: Prove with Your Team

- [ ] Deploy to your analysts
- [ ] Provide pre-configured MCP setup
- [ ] Train on workflows
- [ ] Measure: velocity, accuracy, time saved
- [ ] Collect testimonials and success stories
- [ ] Iterate based on feedback
- [ ] Achieve 100% adoption on your team

### Week 4: Recruit Champions

- [ ] Identify 1 champion from Risk team
- [ ] Identify 1 champion from RevOps team
- [ ] Demo your team's results (metrics + stories)
- [ ] Train champions deeply on the system
- [ ] Get them excited and bought in

**Target:** 25% adoption (your team + champions)

---

## Why This Works

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

### For You

- Build once, scales across teams
- Champions handle training and rollout
- Knowledge compounds over time
- Clear metrics for adoption

---

## Success Metrics

### Define "Adoption" (Clarify with boss NOW)

Is it:
- "Used once this month"?
- "Ships 50%+ of work with AI"?
- "Contributed at least 1 PR"?

### Track Weekly

- Active users (who used it this week)
- Library contributions (PRs merged)
- Success stories (shipped faster/better)
- Velocity metrics (before/after)

---

## The Pitch to Teams

### Core Message
**"You control the knowledge. AI executes it faster."**

### Not: "Trust the AI"

### But: "Document your rules once. AI follows them forever. Validate against YOUR standards."

### Team-Specific Pitches

**For Risk:**
"Document compliance requirements. AI follows them. Audit every output against rules YOU wrote."

**For RevOps:**
"Document revenue logic once. AI generates accurate calcs every time. No human error."

**For Everyone:**
"Your knowledge preserved. New hires learn from it. AI uses it. Tribal knowledge never lost."

---

## What You're Actually Building

### Not just an AI tool.

### A living knowledge base that:

1. Captures institutional knowledge across teams
2. Makes AI agents accurate through context
3. Enables validation against team-documented standards
4. Scales expertise across all analysts
5. Compounds value over time

**The library is infrastructure. Adoption is execution. Champions are the multiplier.**

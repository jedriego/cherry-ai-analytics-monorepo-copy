# AI Tool Configuration

## Overview

Pre-configured Snowflake MCP setup for Claude Code, Cursor, and Codex. Get analysts querying Snowflake via AI in <10 minutes.

---

## Quick Start

### 1. Choose Your Tool

- **Claude Code** (recommended for CLI workflows)
- **Cursor** (recommended for IDE workflows)
- **Codex** (enterprise option)

### 2. Install the Config

**For Claude Code:**

⚠️ **IMPORTANT: Don't blindly copy - you'll overwrite your existing MCP servers!**

```bash
# OPTION A: Manual merge (RECOMMENDED)
# Open your existing settings file
open ~/.claude/settings.json

# Copy the "snowflake" block from claude-code-settings.json
# Paste it into your existing mcpServers section
# Also add the mcpServersAllowedToolsWithoutPermission array if you don't have it
```

**OR if you have NO existing MCP servers:**

```bash
# OPTION B: Fresh install (only if ~/.claude/settings.json is empty or doesn't exist)
cp claude-code-settings.json ~/.claude/settings.json

# Copy the Snowflake service config
cp snowflake_mcp_config.yaml ~/.claude/snowflake_mcp_config.yaml
```

**For Cursor:**

```bash
# Create Cursor MCP config directory
mkdir -p ~/.cursor

# Copy the config
cp cursor-settings.json ~/.cursor/mcp.json

# Copy the Snowflake service config
cp snowflake_mcp_config.yaml ~/.cursor/snowflake_mcp_config.yaml
```

**For Codex:**

```bash
# Edit your existing config
open ~/.codex/config.toml

# Add the [mcp_servers.snowflake] section from codex-settings.toml

# Copy the Snowflake service config
cp snowflake_mcp_config.yaml ~/.codex/snowflake_mcp_config.yaml
```

### 3. Update Your Credentials

**All Tools - Snowflake Credentials:**

Edit your tool's settings file and replace:

- `your-account-id` → your Snowflake account (e.g., `ika12944`)
- `your-username` → your Snowflake username
- `~/.ssh/rsa_key.p8` → path to your RSA private key (absolute path recommended)
- `your-passphrase` → your key passphrase
- Verify `SNOWFLAKE_ROLE` and `SNOWFLAKE_WAREHOUSE` match your access

**GitHub Token (for GitHub MCP):**

The GitHub MCP server is also included for repository access. Update the GitHub token:

- `YOUR_GITHUB_PAT_HERE` → your GitHub Personal Access Token
- **Important:** Token must have ≤180 day expiration for `joinmason` organization
- Create at: https://github.com/settings/tokens

**File locations:**
- Claude Code: `~/.claude/settings.json`
- Cursor: `~/.cursor/mcp.json`
- Codex: `~/.codex/config.toml`

### 4. Verify Setup

**Claude Code:**
```bash
claude mcp list
```

**Cursor:**
Open Cursor → Settings → MCP → Should see Snowflake listed

**Codex:**
```bash
codex mcp list
```

You should see:
- ✓ snowflake - Connected

---

## MCP Servers Included

### `snowflake`
- **What:** Direct Snowflake query execution via official Snowflake Labs MCP server
- **Why:** Query production data, explore schemas, build analytics - all from AI chat
- **Tools:**
  - `run_snowflake_query` - Execute SQL queries
  - `list_semantic_views` - Explore semantic layer
  - `describe_semantic_view` - Get view details
  - `query_semantic_view` - Query semantic models
- **Auth:** RSA key-based authentication (more secure than passwords)

### `github`
- **What:** GitHub repository access via GitHub Copilot MCP
- **Why:** Read code, create issues, manage PRs, search repositories
- **Tools:**
  - `get_file_contents` - Read files from repositories
  - `search_code` - Search across all repositories
  - `list_issues` - Browse issues and PRs
  - `create_issue` - Create new issues
  - And 40+ more GitHub operations
- **Auth:** Personal Access Token (PAT) with appropriate scopes

---

## Authentication Setup

### Snowflake RSA Key Authentication (Required)

1. **Generate RSA keys:**
```bash
# Generate private key
openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8

# Generate public key
openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub

# Move to secure location
mv rsa_key.p8 ~/.ssh/rsa_key.p8
chmod 600 ~/.ssh/rsa_key.p8
```

2. **Add public key to Snowflake:**
```sql
-- In Snowflake, run this SQL (replace with your username and public key content)
ALTER USER your_username SET RSA_PUBLIC_KEY='<paste-public-key-content-here>';
```

To get your public key content:
```bash
# Copy this output (remove BEGIN/END lines)
cat ~/.ssh/rsa_key.pub
```

3. **Update config with:**
   - `SNOWFLAKE_PRIVATE_KEY_FILE`: `/Users/yourname/.ssh/rsa_key.p8` (use ABSOLUTE path)
   - `SNOWFLAKE_PRIVATE_KEY_FILE_PWD`: `your-passphrase` (if you set one during key generation)

**Enable auto-approval for Snowflake queries:**

Already included in all template configs - allows Claude to run queries without asking permission each time.

---

## Troubleshooting

### "MCP server not found"

**For Claude Code:**
```bash
# Check if uvx is installed
uvx --version

# If not, install uv first
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**For Cursor:**
Same as Claude Code - needs `uvx` installed

**For Codex:**
Same as above

### "Authentication failed"

- Verify RSA key path is **absolute** (e.g., `/Users/yourname/.ssh/rsa_key.p8` not `~/.ssh/rsa_key.p8`)
- Check passphrase is correct
- Verify public key is registered in Snowflake:
  ```sql
  DESC USER your_username;
  -- Check RSA_PUBLIC_KEY_FP field has a fingerprint
  ```
- Verify Snowflake account ID format (should be like `abc12345` not `abc12345.snowflakecomputing.com`)

### "Snowflake connection failed"

Test connection manually:
```bash
snowsql -a your-account -u your-username --private-key-path ~/.ssh/rsa_key.p8
```

---

## What's Next?

1. ✅ Tool installed (Claude Code/Cursor/Codex)
2. ✅ Config copied and credentials updated
3. ✅ RSA keys generated and registered
4. ✅ MCP server verified with `mcp list`
5. → **Next:** Start querying! Try "Show me the top 10 customers by revenue"

---

## Support

**Having issues?**
- Ping #ai-analytics in Slack
- Check [Snowflake Labs MCP docs](https://github.com/Snowflake-Labs/mcp-snowflake)
- Tag @your-name for config help

**Want to add more MCP servers later?**
- Browse [MCP registry](https://github.com/modelcontextprotocol/servers)
- Add to your settings file following same pattern
- Share in #ai-analytics

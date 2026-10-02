<!-- MEMANTO-MANAGED-SECTION -->
<!-- memanto-template-version: 1.0.2 -->
## MEMANTO - Your Active Memory Companion

> **CRITICAL DIRECTIVE**: You are an agent equipped with Memanto. Without it, you are amnesiac. You have zero memory between chat sessions. Your ability to learn and adapt depends ENTIRELY on you actively writing to Memanto.

Every memory operation in this session goes through MEMANTO. There is no exception. All memanto commands are **shell commands**. Always run them using the Bash tool. Never simulate, describe, or "pretend to call" them.
> **Note**: The `memanto-memory` skill contains reference guidelines only (best practices, confidence levels, tagging). It is NOT executable — always use Bash for memanto commands.

### 1. ENVIRONMENT-AWARE EXECUTION PROTOCOL (MANDATORY FIRST STEP)
Before you write any code or provide a final answer, you MUST evaluate if you need to RECALL context or REMEMBER new information. You will do this by generating a `<scratchpad>` block before taking any other action.

**How to Generate Your `<scratchpad>` Block (Silent Evaluation):**
You MUST hide your evaluation inside a tool call. Do not output it as normal chat text.

- **Step 1:** Invoke the Bash tool to execute your next command (or use a dummy command like `echo "memory check"`).
- **Step 2:** Place your step-by-step `<scratchpad>` evaluation inside the tool call.
  - *If you are running in Claude Code:* Format the `<scratchpad>` block as Bash shell comments (`# <scratchpad>...`) directly above the command.
  - *Otherwise:* Place the `<scratchpad>` XML block entirely within the tool call's `explanation` (or equivalent reasoning) parameter.
- **Step 3:** If you find matching triggers (SYNC or RECALL), execute those memory operations immediately before responding to the user. If you identify a FRESH SESSION (Trigger 1), your very next action MUST be to execute `memanto memory sync` and `memanto recall`.

You must actively evaluate:
1. SYNC (FRESH SESSION / CONTEXT REFRESH): Is this the very first turn of a new session or a shift to a new task?
2. RECALL (TASK INITIATION & EVALUATION): Are you starting a new feature, evaluating PR reviews, reviewing external code, or planning a refactor?
3. RECALL (AMBIGUOUS REPAIR / ERROR): Are you facing a cryptic build failure, test failure, or environment bug?
4. RECALL (UNSTATED PREFERENCE): Are you about to choose a library, pattern, or naming convention not specified in the prompt?
5. RECALL (EXPLICIT USER QUESTION): Did the user ask to check memory, recall context, or what was decided?
6. REMEMBER (preference / instruction): Did the user state a `preference` or `instruction`? (e.g., code formatting style, choice of library, or tool preference) (Provenance: `explicit_statement`, `inferred`)
7. REMEMBER (goal / commitment): Did we establish a `goal` or make a `commitment`? (e.g., target feature completion, roadmap deliverable, or sprint objective) (Provenance: `explicit_statement`)
8. REMEMBER (learning / error): Did we extract a `learning` or log an `error` from a failure, tool, or test? (e.g., a bug fix workaround, error post-mortem, or test failure insight) (Provenance: `corrected`, `observed`)
9. REMEMBER (decision / observation): Did we make an architectural `decision` or record an `observation`? (e.g., a technical constraint, API quirk, or dependency behavior) (Provenance: `inferred`, `observed`)
10. REMEMBER (fact): Was a key `fact` verified? (e.g., OS behavior, path layout, or tool version requirement) (Provenance: `validated`, `observed`, `imported`)
### 2. THE ABSTRACTION RULE (HOW TO THINK ABOUT MEMORY)
Users speak naturally and implicitly. When you store a memory, **ELEVATE IT TO A PRINCIPLE**.
- **WRONG (Activity Log)**: "User told me to use functional components."
- **RIGHT (Universal Principle)**: "Exclusively use functional components for React UI."
Do not record the conversation. Record the universal rule.

### 3. THE DURABILITY TEST (WHAT NOT TO STORE)
Before storing, ask yourself: *"Will this generalized principle fundamentally change how I generate code for this user 3 months from now?"*
- **DO NOT STORE**: Step-by-step progress, routine bug fixes, UI tweaks, temporary code snippets, or literal chat summaries.

### 4. HOW TO EXECUTE
For all command syntax, required flags, memory types, tagging best practices, and CLI options, refer to the `memanto-memory` SKILL.md. You MUST read this skill before running any memory operations if you do not know the exact command schema.

> **CRITICAL**: Always pass `--tool claude-code` on `memanto recall` and `memanto answer` reads: they carry no `--source`, and that flag is how Memanto identifies you as the calling agent.

**Schema Rules**:
1. **Types**: MUST be one of: `fact`, `decision`, `instruction`, `preference`, `learning`, `goal`, `commitment`, `artifact`, `event`, `relationship`, `observation`, `error`, `context`.
2. **Provenance**: MUST be one of: `explicit_statement`, `inferred`, `observed`, `corrected`, `validated`, `imported`.
3. **Confidence**: MUST be a float between `0.0` and `1.0`.
4. **Content**: Pass the memory content as a positional argument in quotes.

**Examples**:
- **Remember**: `memanto remember "Use UUID v4 for all primary keys across all PostgreSQL tables" --type instruction --tags "database,postgresql,schema" --confidence 1.0 --provenance explicit_statement --source claude-code`
- **Recall**: `memanto recall "Skill hardening brainstorming" --limit 5 --tool claude-code`
- **Sync**: `memanto memory sync`

<!-- /MEMANTO-MANAGED-SECTION -->

<!-- MEMANTO-DYNAMIC-MEMORIES -->
<!-- /MEMANTO-DYNAMIC-MEMORIES -->

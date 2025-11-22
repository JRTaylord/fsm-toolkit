# FSM Toolkit - Quick Reference Card

## 🎯 One-Line Summary
Extract state machines from code using AI → Generate beautiful diagrams → Convert to debuggable XState

---

## 🚀 Getting Started (30 seconds)

### Windows
```powershell
.\quickstart.ps1
```

### macOS / Linux
```bash
./quickstart.sh
```

---

## 📋 Common Commands

### Analyze Your Code
```bash
cd code-to-fsm
node cli.js analyze /path/to/project --to-xstate
```

### Convert Mermaid to XState
```bash
cd mermaid-to-xstate
node cli.js diagram.mmd -o machine.js
```

### Interactive Mode (Chat with Claude)
```bash
cd code-to-fsm
node cli.js interactive /path/to/project
```

---

## 📁 What You Get

```
📊 state-machine.mmd      ← Mermaid diagram (visual)
📄 analysis.txt           ← Full explanation
🎯 state-machine.js       ← XState code (executable)
```

---

## 🎓 Typical Workflow

1. **Extract**: `node cli.js analyze ./robot-code`
2. **Review**: Open `state-machine.mmd`
3. **Refine**: Edit diagram if needed
4. **Convert**: `node cli.js diagram.mmd -o robot.js`
5. **Refactor**: Use generated XState in your code
6. **Debug**: Use XState Inspector

---

## 💡 Use Cases

| Scenario | Command |
|----------|---------|
| Understand legacy code | `analyze /old-project` |
| Document your code | `analyze /src -o /docs/fsm` |
| Refactor to XState | `analyze /src --to-xstate` |
| Design new feature | Create `.mmd` → convert to XState |

---

## 🔧 Options Cheat Sheet

### code-to-fsm
```bash
-o, --output <dir>              # Output directory
-f, --files <files...>          # Specific files only
--focus "component"             # Focus on specific part
--to-xstate                     # Generate XState too
--machine-id "myMachine"        # Custom XState ID
```

### mermaid-to-xstate
```bash
-o, --output <file>             # Output file
-f, --format <format>           # esm|cjs|json
-i, --id <id>                   # Machine ID
```

---

## ⚡ Quick Examples

### Example 1: Analyze Python Robot
```bash
cd code-to-fsm
node cli.js analyze ../robot-project -f controller.py sensor.py --to-xstate
```

### Example 2: Design First, Code Later
```bash
# 1. Design in Mermaid
cat > robot.mmd << 'EOF'
stateDiagram-v2
    [*] --> Idle
    Idle --> Moving: start
    Moving --> [*]: stop
EOF

# 2. Convert to XState
cd mermaid-to-xstate
node cli.js robot.mmd -o robot-machine.js

# 3. Implement using the state machine
```

### Example 3: Document Existing Code
```bash
cd code-to-fsm
node cli.js analyze ../my-app --focus "authentication flow" -o ../docs/diagrams
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "node not found" | Install Node.js 14+ |
| "No files found" | Use `-f` to specify files |
| "Claude API error" | Run in artifacts environment |
| Emoji issues (Windows) | Use Windows Terminal |

---

## 📚 Full Documentation

- `README.md` - Overview & features
- `PLATFORM_COMPATIBILITY.md` - Windows/macOS/Linux setup
- `code-to-fsm/WORKFLOW_GUIDE.md` - Detailed workflow
- `code-to-fsm/README.md` - Analyzer docs
- `mermaid-to-xstate/README.md` - Converter docs

---

## 🌟 Key Features

- ✅ **Cross-platform** - Windows, macOS, Linux
- ✅ **Multi-language** - Python, JS, C++, Java, etc.
- ✅ **AI-powered** - Claude understands your code
- ✅ **Visual** - Beautiful Mermaid diagrams
- ✅ **Executable** - Working XState machines
- ✅ **Debuggable** - XState Inspector support

---

## 🎯 Next Steps

1. Run quickstart script
2. Try it on example robot code
3. Analyze your own project
4. Read WORKFLOW_GUIDE.md for deep dive

**Questions?** Check the full README.md or PLATFORM_COMPATIBILITY.md

---

Happy state machine engineering! 🎉

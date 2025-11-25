# FSM Toolkit - Quick Reference Card

## 🎯 One-Line Summary
Extract state machines from code using AI → Generate beautiful Mermaid diagrams

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
node cli.js analyze /path/to/project
```

### Interactive Mode (Chat with Claude)
```bash
cd code-to-fsm
node cli.js interactive /path/to/project
```

### Focus on Specific Component
```bash
cd code-to-fsm
node cli.js analyze /path/to/project --focus "navigation system"
```

---

## 📁 What You Get

```
📊 state-machine.mmd      ← Mermaid diagram source
📄 analysis.txt           ← Full explanation
🌐 state-machine.html     ← Interactive visualization
```

---

## 🎓 Typical Workflow

1. **Extract**: `node cli.js analyze ./robot-code`
2. **View**: Opens automatically in browser
3. **Review**: Check `state-machine.mmd` and `analysis.txt`
4. **Export**: Use browser controls to export as SVG/PNG
5. **Document**: Add diagrams to your documentation
6. **Share**: Share with your team

---

## 💡 Use Cases

| Scenario | Command |
|----------|---------|
| Understand legacy code | `analyze /old-project` |
| Document your code | `analyze /src -o /docs/fsm` |
| Code review | `analyze /feature-branch --focus "feature"` |
| Team communication | `analyze /src` (share exported diagram) |

---

## 🔧 Options Cheat Sheet

### code-to-fsm
```bash
-o, --output <dir>              # Output directory (default: ./fsm-output)
-f, --files <files...>          # Specific files only
-p, --patterns <patterns...>    # File patterns to match
--focus "component"             # Focus on specific part
```

---

## ⚡ Quick Examples

### Example 1: Analyze Python Robot
```bash
cd code-to-fsm
node cli.js analyze ../robot-project -f controller.py sensor.py
```

### Example 2: Document Existing Code
```bash
cd code-to-fsm
node cli.js analyze ../my-app --focus "authentication flow" -o ../docs/diagrams
```

### Example 3: Interactive Exploration
```bash
cd code-to-fsm
node cli.js interactive ../my-app
# Chat with Claude about the state machine
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "node not found" | Install Node.js 14+ |
| "No files found" | Use `-f` to specify files |
| "Claude Code CLI not found" | Install Claude Code CLI |
| Emoji issues (Windows) | Use Windows Terminal |

---

## 📚 Full Documentation

- `README.md` - Overview & features
- `PLATFORM_COMPATIBILITY.md` - Windows/macOS/Linux setup
- `code-to-fsm/WORKFLOW_GUIDE.md` - Detailed workflow
- `code-to-fsm/README.md` - Full analyzer documentation

---

## 🌟 Key Features

- ✅ **Cross-platform** - Windows, macOS, Linux
- ✅ **Multi-language** - Python, JS, C++, Java, etc.
- ✅ **AI-powered** - Claude understands your code
- ✅ **Visual** - Beautiful Mermaid diagrams
- ✅ **Interactive** - Browser-based viewer with zoom/pan
- ✅ **Exportable** - SVG, PNG, and Mermaid source

---

## 🎯 Next Steps

1. Run quickstart script
2. Try it on example robot code
3. Analyze your own project
4. Read WORKFLOW_GUIDE.md for deep dive

**Questions?** Check the full README.md or PLATFORM_COMPATIBILITY.md

---

Happy state machine engineering! 🎉

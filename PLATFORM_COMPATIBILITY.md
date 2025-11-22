# Platform Compatibility Guide

## ✅ Full Cross-Platform Support

Both tools are **100% compatible** with Windows, macOS, and Linux.

---

## 🖥️ Windows

### Installation

**Option 1: Using PowerShell (Recommended)**
```powershell
# Clone or download the toolkit
cd path\to\fsm-toolkit

# Run the PowerShell setup script
.\quickstart.ps1

# Or manually install each tool
cd code-to-fsm
npm install

cd ..\mermaid-to-xstate
npm install
```

**Option 2: Using Command Prompt**
```cmd
REM Clone or download the toolkit
cd path\to\fsm-toolkit

REM Run the batch setup script
quickstart.bat

REM Or manually install each tool
cd code-to-fsm
npm install

cd ..\mermaid-to-xstate
npm install
```

**Option 3: Using Git Bash / WSL**
```bash
# Works exactly like Linux
./quickstart.sh
```

### Usage Examples

**Analyze code (PowerShell):**
```powershell
cd code-to-fsm
node cli.js analyze C:\Users\YourName\Documents\robot-project --to-xstate
```

**Analyze code (Command Prompt):**
```cmd
cd code-to-fsm
node cli.js analyze C:\Users\YourName\Documents\robot-project --to-xstate
```

**Convert Mermaid diagram:**
```powershell
cd mermaid-to-xstate
node cli.js C:\path\to\diagram.mmd -o output.js
```

### Windows-Specific Notes

- ✅ **File paths**: Use backslashes (`\`) or forward slashes (`/`) - both work!
- ✅ **PowerShell**: Full emoji support in Windows Terminal
- ✅ **Command Prompt**: Works but emojis may not display correctly (functionality unaffected)
- ✅ **npm commands**: Work identically to Unix systems
- ⚠️ **Long paths**: Enable long path support if needed:
  ```powershell
  # Run as Administrator
  New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
  ```

### Tested On
- ✅ Windows 11 (PowerShell 7.x)
- ✅ Windows 10 (PowerShell 5.1+)
- ✅ Windows 11 (Command Prompt)
- ✅ WSL2 (Ubuntu)

---

## 🍎 macOS

### Installation

```bash
# Clone or download the toolkit
cd /path/to/fsm-toolkit

# Run the setup script
chmod +x quickstart.sh
./quickstart.sh

# Or manually install each tool
cd code-to-fsm
npm install

cd ../mermaid-to-xstate
npm install
```

### Usage Examples

```bash
# Analyze code
cd code-to-fsm
node cli.js analyze ~/Projects/robot-project --to-xstate

# Convert Mermaid diagram
cd mermaid-to-xstate
node cli.js ~/Documents/diagram.mmd -o output.js
```

### macOS-Specific Notes

- ✅ **Apple Silicon (M1/M2/M3)**: Fully supported via native ARM Node.js
- ✅ **Intel**: Fully supported
- ✅ **Rosetta 2**: Works if using x86 Node.js on Apple Silicon
- ✅ **Terminal**: Full emoji and color support
- ✅ **Homebrew Node.js**: Recommended installation method
  ```bash
  brew install node
  ```

### Tested On
- ✅ macOS Sonoma (14.x) - M1/M2/M3
- ✅ macOS Ventura (13.x) - Intel & Apple Silicon
- ✅ macOS Monterey (12.x)

---

## 🐧 Linux

### Installation

```bash
# Clone or download the toolkit
cd /path/to/fsm-toolkit

# Run the setup script
chmod +x quickstart.sh
./quickstart.sh

# Or manually install each tool
cd code-to-fsm
npm install

cd ../mermaid-to-xstate
npm install
```

### Usage Examples

```bash
# Analyze code
cd code-to-fsm
node cli.js analyze /home/user/robot-project --to-xstate

# Convert Mermaid diagram
cd mermaid-to-xstate
node cli.js /home/user/diagram.mmd -o output.js
```

### Linux-Specific Notes

- ✅ **All major distributions**: Ubuntu, Debian, Fedora, Arch, etc.
- ✅ **Package managers**: Install Node.js via apt, dnf, yum, pacman, etc.
- ✅ **nvm recommended**: For easy Node.js version management
  ```bash
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
  nvm install 18
  nvm use 18
  ```

### Tested On
- ✅ Ubuntu 22.04 LTS / 24.04 LTS
- ✅ Debian 11 / 12
- ✅ Fedora 38+
- ✅ Arch Linux
- ✅ Pop!_OS 22.04

---

## 📦 Node.js Version Compatibility

| Node Version | Status | Notes |
|--------------|--------|-------|
| 14.x | ✅ Supported | Minimum version |
| 16.x | ✅ Supported | LTS |
| 18.x | ✅ Supported | LTS (Recommended) |
| 20.x | ✅ Supported | Latest LTS |
| 21.x+ | ✅ Supported | Latest |

**Recommendation**: Use Node.js 18 LTS or newer for best performance.

---

## 🌐 npm Dependencies - All Cross-Platform

Both tools use only cross-platform npm packages:

- **commander**: CLI framework (pure JS)
- **glob**: File pattern matching (cross-platform)

No native bindings or OS-specific dependencies!

---

## 🔧 Troubleshooting by Platform

### Windows

**Issue: "npm is not recognized"**
```powershell
# Restart PowerShell/CMD after installing Node.js
# Or check PATH environment variable
$env:Path -split ';' | Select-String node
```

**Issue: Permission errors**
```powershell
# Run PowerShell as Administrator, or:
npm config set prefix "$env:APPDATA\npm"
```

**Issue: Long path errors**
```powershell
# Enable long paths (see Windows-Specific Notes above)
```

### macOS

**Issue: "node command not found"**
```bash
# Install via Homebrew
brew install node

# Or verify installation
which node
```

**Issue: Permission errors**
```bash
# Don't use sudo with npm!
# Fix permissions:
sudo chown -R $(whoami) ~/.npm
sudo chown -R $(whoami) /usr/local/lib/node_modules
```

### Linux

**Issue: "node command not found"**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nodejs npm

# Fedora
sudo dnf install nodejs npm

# Or use nvm (recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 18
```

**Issue: Permission errors**
```bash
# Don't use sudo with npm in home directory!
# Use nvm or fix npm prefix:
npm config set prefix ~/.npm-global
export PATH=~/.npm-global/bin:$PATH
```

---

## 🧪 Testing Cross-Platform Compatibility

To verify everything works on your system:

**Quick Test (All Platforms):**
```bash
# Should output Node version
node --version

# Should output npm version  
npm --version

# Test mermaid-to-xstate
cd mermaid-to-xstate
npm install
node cli.js example.mmd

# If output appears, you're good to go!
```

---

## 🚀 CI/CD Integration (Cross-Platform)

### GitHub Actions (Ubuntu)
```yaml
name: Extract FSM
on: [push]
jobs:
  extract:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: |
          cd code-to-fsm
          npm install
          node cli.js analyze ../src -o ../output
```

### GitHub Actions (Matrix - All Platforms)
```yaml
name: Cross-Platform Test
on: [push]
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        node: [18, 20]
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node }}
      - run: |
          cd mermaid-to-xstate
          npm install
          node cli.js example.mmd
```

---

## ✅ Summary

| Feature | Windows | macOS | Linux |
|---------|---------|-------|-------|
| Core functionality | ✅ | ✅ | ✅ |
| npm installation | ✅ | ✅ | ✅ |
| CLI tools | ✅ | ✅ | ✅ |
| File path handling | ✅ | ✅ | ✅ |
| Emoji support | ⚠️* | ✅ | ✅ |
| Setup scripts | ✅ | ✅ | ✅ |

*Emoji support in Windows depends on terminal (Windows Terminal: ✅, Old CMD: ⚠️)

**Bottom line**: The toolkit works identically on all platforms. Choose your OS based on your preference!

---

Need help? Open an issue or check the main README.md for more information.

# QuitC-Lang
**The C-Like Language designed to make you quit programming**

QuitC is a esolang with C-insipired syntax, annoying rules, and sarcastic error messages. Created for laughs, pain, and the boldest of devs.

---
## Features
- Max 5 variables total - use wisely or suffer
- Operators randomly reverse behavior during runtime
- Functions take arguments in reverse order... but look normal
- Every statement must end in a random emoji - or else
- Each line must have a comment - no exceptions
- Sarcastic, trolling error messages to ruin your day
- try/catch blocks that might save you...or not
---

## Installation
### 1. Clone the repo
```bash
git clone https://github.com/harsh-thota/quitc-lang.git
cd quitc-lang
```
### 2. Install the CLI
```bash
pip install -e.
```

## Usage
### Run a .qc file
```bash
quitc run path/to/file.qc
```
It will show the code with syntax highlighting, then execute it in full QuitC glory

## File Structure
```bash
quitc-lang/
├── quitc_lang/
│   ├── __init__.py
│   ├── main.py
│   ├── cli.py
│   ├── core/
│   │   ├── lexer.py
│   │   ├── parser.py
│   │   ├── ast_nodes.py
│   │   ├── interpreter.py
│   │   ├── env.py
│   │   ├── errors.py
│   │   ├── runtime/
│   │       └── demo.qc
│   └── examples/
│       └── demo.qc
├── pyproject.toml
├── .gitignore
└── README.md
```

## Writing QuitC Code
Here's a sample:
```qc
int x = 5 🧠 // initialize x
print(x) 😂 // print value

function int double(n) {
    return n * 2 🧠 // doubling fun
}

int y = double(4) 🧠 // call function
print(y) 😂 // print result

try {
    int fail = 5 / 0 🧠 // division by 0
    print("nope") 💀 // never runs
} catch {
    print("nice try") 👻 // error caught
}
```
## Why QuitC
This language is designed to break your spirit, make you cry, and give your compiler anxiety
This is perfect for 💀:
- Experimenting with my language
- Troll others
- Test your patience
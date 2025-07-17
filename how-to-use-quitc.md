---

# QuitC Language Guide

> The programming language that trolls you when you mess up, and only respects emoji-terminated lines 😈

---

## Basic Rules

QuitC intentionally makes you suffer for fun. It has:

* **Max 5 total variables allowed**
* **Operators can randomly reverse meaning**
* **Function arguments are passed in reverse order**
* **Every line must end with an emoji**
* **Every line must have a comment**
* **Sarcastic errors when you mess up**

---

## Requirements

Each line must follow these rules:

| Requirement               | Description                                                             |
| ------------------------- | ----------------------------------------------------------------------- |
| ✅ **Emoji**               | Every statement must end with a valid emoji (or it fails sarcastically) |
| ✅ **Comment**             | Every line must have a comment after the statement                      |
| ⚠️ **5 Variables Max**    | The total number of unique variables cannot exceed 5                    |
| 🔁 **Flipping Operators** | Sometimes `+` means `-`, `*` means `/`, and chaos ensues                |
| 🔁 **Reverse Args**       | Functions take arguments in reverse **order** at runtime                |

---

## Features & Syntax

---

### Variables

```qc
int x = 10 🤡 // create a variable
string name = "QuitC" 😂 // a string variable
```

> ⚠️ You cannot have more than 5 variables total. Use them wisely!

---

### Operators (and how they troll you)

```qc
int y = x + 2 🤡 // might actually subtract depending on mood
int z = y * 3 😈 // could be division if you're unlucky
```

> Operators may randomly **reverse behavior**. Good luck debugging.

---

### Print

```qc
print(x) 🤡 // show the value of x
print("Hello!") 🤡 // strings too
```

---

### Functions

```qc
function int double(n) {
    return n * 2 😈 // doubles the input
}
```

**Calling functions:**

```qc
int result = double(5) 😈 // passed as-is
```

> But internally: args are received **in reverse order**. You're warned.

---

### While Loops

```qc
int i = 0 🫠 // start value
while (i < 5) {
    print(i) 🫠 // output value
    i = i + 1 🤡 // increment
}
```

---

### If / Else

```qc
if (x < 10) {
    print("x is small") 🫠
} else {
    print("x is big") 😂
}
```

---

### Try / Catch

```qc
try {
    int bad = 1 / 0 🫠 // breaks
    print("never happens") 😒
} catch {
    print("you messed up") 😭 // sarcastic response
}
```

---

### Return Statements

```qc
function int triple(n) {
    return n * 3 😈 // triple it
}
```

---

## Errors (with sarcasm)

QuitC doesn't just throw errors — it insults you.

* ❌ Forgot emoji?
  `"No emoji? No execution. Rules are rules. [Context: 4]"`

* ❌ Too many variables?
  `"You think you're clever making 6 variables? Nope."`

* ❌ Missing comment?
  `"Where's the commentary genius? Add a comment."`

* ❌ Using undefined variable?
  `"Wow. You're referencing a ghost. Define it maybe?"`

> These errors are randomly sarcastic — to keep you humble.

---

## Example: Full Program

```qc
int x = 5 👻 // define x
print(x) 🤡 // output x

function int square(n) {
    return n * n 😵 // square the input
}

int result = square(4) 😂 // call function
print(result) 😭 // print result

try {
    int broken = 4 / 0 😒 // deliberate fail
    print("unreachable") 😵 // won't happen
} catch {
    print("Nice try") 😒 // recover sarcastically
}
```

---

## Run It

Once installed:

```bash
quitc run your_file.qc
```

Or use the [QuitC Web Playground](https://quitc-lang.onrender.com/) to test online.
## ✅ Exploiting PHP `proc_open()` Remote Code Execution:

`proc_open()` is a built-in function in PHP — and it's one of the most powerful (and dangerous) ways to execute system commands.

### 🔍 What is `proc_open()`?

- `proc_open()` is a powerful PHP function used to execute external system commands with full control over input/output streams.
- It provides access to **stdin**, **stdout**, **stderr**, environment variables, and allows asynchronous execution.
- Unlike `exec()`, `shell_exec()`, or `system()`, it enables building complex I/O pipelines between PHP and the command.
- It is highly flexible but also dangerous if user input is not sanitized — can lead to **command injection**.
- Always use `escapeshellarg()` or `escapeshellcmd()` to sanitize inputs before passing them to `proc_open()`.
- Prefer native PHP alternatives (like `ZipArchive`, `file_get_contents()`, etc.) whenever possible for safety and clarity.

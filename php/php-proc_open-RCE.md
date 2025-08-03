## ✅ Exploiting PHP `proc_open()` Remote Code Execution:

`proc_open()` is a built-in function in PHP — and it's one of the most powerful (and dangerous) ways to execute system commands.

### 🔍 What is `proc_open()`?

- `proc_open()` is a powerful PHP function used to execute external system commands with full control over input/output streams.
- It provides access to **stdin**, **stdout**, **stderr**, environment variables, and allows asynchronous execution.
- Unlike `exec()`, `shell_exec()`, or `system()`, it enables building complex I/O pipelines between PHP and the command.
- It is highly flexible but also dangerous if user input is not sanitized — can lead to **command injection**.
- Always use `escapeshellarg()` or `escapeshellcmd()` to sanitize inputs before passing them to `proc_open()`.
- Prefer native PHP alternatives (like `ZipArchive`, `file_get_contents()`, etc.) whenever possible for safety and clarity.

## Vulnerable Code:

- The vulnerability occurs because the `$command` variable is built using unsanitized user input `($_POST['password'])`, which is directly concatenated into a shell command executed by `proc_open()`, leading to possible command injection.
```
<?php
if (isset($_POST['backup']) && !empty($_POST['password'])) {
    $password = cleanEntry($_POST['password']);
    $backupFile = "backups/backup_" . date('Y-m-d') . ".zip";

    if ($password === false) {
        echo "<div class='error-message'>Error: Try another password.</div>";
    } else {
        $logFile = '/tmp/backup_' . uniqid() . '.log';
       
        $command = "zip -x './backups/*' -r -P " . $password . " " . $backupFile . " .  > " . $logFile . " 2>&1 &";
        
        $descriptor_spec = [
            0 => ["pipe", "r"], // stdin
            1 => ["file", $logFile, "w"], // stdout
            2 => ["file", $logFile, "w"], // stderr
        ];

        $process = proc_open($command, $descriptor_spec, $pipes);
        if (is_resource($process)) {
            proc_close($process);
        }

        sleep(2);

        $logContents = file_get_contents($logFile);
        if (strpos($logContents, 'zip error') === false) {
            echo "<div class='backup-success'>";
            echo "<p>Backup created successfully.</p>";
            echo "<a href='" . htmlspecialchars($backupFile) . "' class='download-button' download>Download Backup</a>";
            echo "<h3>Output:</h3><pre>" . htmlspecialchars($logContents) . "</pre>";
            echo "</div>";
        } else {
            echo "<div class='error-message'>Error creating the backup.</div>";
        }

        unlink($logFile);
    }
}
?>
```

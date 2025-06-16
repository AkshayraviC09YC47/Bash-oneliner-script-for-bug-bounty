#!/usr/bin/env python3

import subprocess

burpsuite_path = "/home/akshay/Documents/burpsuite_pro_v2024.3.1/burpsuite_pro_v2025.5.4.jar"
loader_path = "/home/akshay/Documents/burpsuite_pro_v2024.3.1/Loader.jar"
ram_size="-Xmx16384M" #16GB ram
hidpi = "-Dsun.java2d.uiScale=2"

# Get the display resolution
display_res = subprocess.check_output("xrandr | grep '*'", shell=True).decode('utf-8')

# Check if the display resolution is 1920x1200
if "1920x1200" in display_res:
    subprocess.call(
        f"nohup java {ram_size} --add-opens=java.desktop/javax.swing=ALL-UNNAMED "
        f"--add-opens=java.base/java.lang=ALL-UNNAMED "
        f"--add-opens=java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED "
        f"--add-opens=java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED "
        f"--add-opens=java.base/jdk.internal.org.objectweb.asm.Opcodes=ALL-UNNAMED "
        f"-javaagent:{loader_path} -noverify -jar {burpsuite_path} &", shell=True)
else:
    subprocess.call(
        f"nohup java {ram_size} {hidpi} --add-opens=java.desktop/javax.swing=ALL-UNNAMED "
        f"--add-opens=java.base/java.lang=ALL-UNNAMED "
        f"--add-opens=java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED "
        f"--add-opens=java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED "
        f"--add-opens=java.base/jdk.internal.org.objectweb.asm.Opcodes=ALL-UNNAMED "
        f"-javaagent:{loader_path} -noverify -jar {burpsuite_path} &", shell=True)

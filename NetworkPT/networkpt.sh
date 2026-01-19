#!/bin/bash

# =========================
# USAGE CHECK
# =========================
if [ $# -ne 1 ]; then
  echo "Usage: $0 <ip_list.txt>"
  exit 1
fi

INPUT_FILE="$1"

if [ ! -f "$INPUT_FILE" ]; then
  echo "[-] File not found: $INPUT_FILE"
  exit 1
fi

# =========================
# DERIVE FOLDER NAME
# =========================
BASENAME=$(basename "$INPUT_FILE")
SCAN_NAME="${BASENAME%.*}"
BASE_DIR="nmap-$SCAN_NAME"

XML_DIR="$BASE_DIR/xml-format"
NMAP_DIR="$BASE_DIR/nmap-format"
GNMAP_DIR="$BASE_DIR/gnmap-format"

# =========================
# CREATE DIRECTORY STRUCTURE
# =========================
mkdir -p "$XML_DIR" "$NMAP_DIR" "$GNMAP_DIR"

echo "[+] Scan name      : $SCAN_NAME"
echo "[+] Output folder  : $BASE_DIR"
echo "[+] Starting scan..."

# =========================
# MAIN SCAN LOOP
# =========================
while read -r IP; do

  # Skip empty lines and comments
  [[ -z "$IP" || "$IP" =~ ^# ]] && continue

  echo "[+] Scanning $IP"

  nmap -Pn \
    -sT -sV \
    --version-light \
    --script "default,safe" \
    --open \
    -T4 \
    --max-retries 2 \
    --host-timeout 30m \
    --stats-every 60s \
    -oX "$XML_DIR/$IP.xml" \
    -oN "$NMAP_DIR/$IP.nmap" \
    -oG "$GNMAP_DIR/$IP.gnmap" \
    "$IP"

done < "$INPUT_FILE"

echo "[+] Scan completed successfully"
echo "[+] Results saved in: $BASE_DIR"

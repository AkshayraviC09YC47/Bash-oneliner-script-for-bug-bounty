#!/bin/bash

# Exit if input file is not provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <ip_list.txt>"
  exit 1
fi

INPUT_FILE="$1"

# Exit if input file does not exist
if [ ! -f "$INPUT_FILE" ]; then
  echo "[-] File not found: $INPUT_FILE"
  exit 1
fi

# Extract filename without extension (private.txt -> private)
BASENAME=$(basename "$INPUT_FILE")
SCAN_NAME="${BASENAME%.*}"

# Base output directory (nmap-private)
BASE_DIR="nmap-$SCAN_NAME"

# Output directories for each format
XML_DIR="$BASE_DIR/xml-format"        # XML output for parsing/reporting
NMAP_DIR="$BASE_DIR/nmap-format"      # Normal human-readable output
GNMAP_DIR="$BASE_DIR/gnmap-format"    # Grepable output for automation

# Create directory structure
mkdir -p "$XML_DIR" "$NMAP_DIR" "$GNMAP_DIR"

echo "[+] Scan name     : $SCAN_NAME"
echo "[+] Output folder : $BASE_DIR"
echo "[+] Starting scan..."

# Read IPs one by one from input file
while read -r IP; do

  # Skip empty lines and commented lines
  [[ -z "$IP" || "$IP" =~ ^# ]] && continue

  echo "[+] Scanning $IP"

  nmap -Pn \                          # Skip host discovery (assume host is up)
    -sT -sV \                         # TCP connect scan + service version detection
    --version-light \                 # Light version probing (low noise)
    --script "default,safe" \         # Run only safe, non-intrusive NSE scripts
    --open \                          # Show only open ports
    -T4 \                             # Faster timing (safe for internal networks)
    --max-retries 2 \                 # Limit retries to reduce scan delays
    --host-timeout 30m \              # Stop scanning host if it exceeds 30 minutes
    --stats-every 60s \               # Show progress every 60 seconds
    -oX "$XML_DIR/$IP.xml" \          # Save XML output
    -oN "$NMAP_DIR/$IP.nmap" \        # Save normal Nmap output
    -oG "$GNMAP_DIR/$IP.gnmap" \      # Save grepable output
    "$IP"                             # Target IP address

done < "$INPUT_FILE"

echo "[+] Scan completed successfully"
echo "[+] Results saved in: $BASE_DIR"

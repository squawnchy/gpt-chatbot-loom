#!/usr/bin/env bash

set -euo pipefail

# Logging function for cleaner output
log() {
    echo "[INFO] $1"
}

install_requirements() {
    log "Installing requirements..."
    python3 -m pip install -r requirements.txt
}

run_chatbot_loom() {
    log "Clearing screen..."
    clear
    log "Running chatbot_loom..."
    python3 -m chatbot_loom
}

main() {
    install_requirements
    run_chatbot_loom
}

main

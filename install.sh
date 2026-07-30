#!/bin/bash

INSTALL_DIR="/usr/local/bin"
BINARY_NAME="osltxt"
REPO="socialmediatvtweet-tech/osltxt-format"

echo "Downloading the latest version of osltxt from GitHub..."

DOWNLOAD_URL="https://github.com/${REPO}/releases/latest/download/osltxt.py"

if command -v curl &> /dev/null; then
    sudo curl -L -o "${INSTALL_DIR}/${BINARY_NAME}" "${DOWNLOAD_URL}"
elif command -v wget &> /dev/null; then
    sudo wget -O "${INSTALL_DIR}/${BINARY_NAME}" "${DOWNLOAD_URL}"
else
    echo "Error: Neither curl nor wget is installed!"
    exit 1
fi

sudo chmod +x "${INSTALL_DIR}/${BINARY_NAME}"

echo "Done! osltxt has been successfully installed."

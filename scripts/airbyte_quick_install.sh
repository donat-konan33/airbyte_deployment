#!/usr/bin/env bash

set -e

# get last version
get_latest_version() {
  curl --silent "https://api.github.com/repos/airbytehq/abctl/releases/latest" |
  grep '"tag_name":' |
  sed -E 's/.*"v([^"]+)".*/\1/'
}

# checkout of OS
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

# Mapping architecture
case "$ARCH" in
  x86_64) ARCH="amd64" ;;
  arm64|aarch64) ARCH="arm64" ;;
  *) echo "❌ Unsuppported Architecture: $ARCH" && exit 1 ;;
esac

# Mapping OS extension
case "$OS" in
  linux|darwin) EXT="tar.gz" ;;
  msys*|cygwin*|mingw*|windows)
    OS="windows"
    EXT="zip"
    ;;
  *) echo "❌ Unsupported OS: $OS" && exit 1 ;;
esac

# last abctl version
VERSION=$(get_latest_version)
echo "📦 last abctl version : v$VERSION"

# Build url
FILENAME="abctl-v$VERSION-$OS-$ARCH.$EXT"
URL="https://github.com/airbytehq/abctl/releases/download/v$VERSION/$FILENAME"

# downlaoding
echo "⬇️ download of $FILENAME of $URL"
curl -LO "$URL"

# Extraction
echo "📂 Extraction..."
if [[ "$EXT" == "tar.gz" ]]; then
  tar -xvzf "$FILENAME"
elif [[ "$EXT" == "zip" ]]; then
  unzip "$FILENAME"
else
  echo "❌ Format unknown: $EXT"
  exit 1
fi

AIRBYTE_DIR="abctl-v$VERSION-$OS-$ARCH"
chmod +x "$AIRBYTE_DIR/abctl"
sudo mv "$AIRBYTE_DIR/abctl" /usr/local/bin

# cleanup
rm "$FILENAME"
rm -rf "$AIRBYTE_DIR"


# Run Airbyte
abctl local install
while [[ -z "$EMAIL" ]]; do
  read -p "Hit your email : " EMAIL
  if [[ -z "$EMAIL" ]]; then
    echo "❌ Email is mandatory. Please hit your email."
  fi
done

read -p -s "Hit your password : " PASSWORD
echo
abctl local credentials --email "$EMAIL" --password "$PASSWORD"

echo "✅ Locally abctl installed and ready to use ( : ./abctl)"

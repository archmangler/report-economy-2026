#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Installing MacTeX (this may take a while)...${NC}"

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install MacTeX using Homebrew
brew install --cask mactex-no-gui

# Add TeX to PATH
echo -e "${BLUE}Adding TeX to PATH...${NC}"
export PATH="/Library/TeX/texbin:$PATH"

# Verify LaTeX installation
echo -e "${BLUE}Verifying LaTeX installation...${NC}"
if command -v latex &> /dev/null; then
    echo -e "${GREEN}LaTeX installed successfully!${NC}"
else
    echo "LaTeX installation failed. Please install manually from: https://www.tug.org/mactex/"
fi

# Refresh shell
echo -e "${BLUE}Refreshing shell...${NC}"
exec $SHELL
eval "$(/usr/libexec/path_helper)"
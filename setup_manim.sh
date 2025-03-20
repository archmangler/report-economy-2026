#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Setting up Manim environment...${NC}"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Create virtual environment
echo -e "${BLUE}Creating virtual environment...${NC}"
python3 -m venv manim_env

# Activate virtual environment
echo -e "${BLUE}Activating virtual environment...${NC}"
source manim_env/bin/activate

# Upgrade pip
echo -e "${BLUE}Upgrading pip...${NC}"
pip install --upgrade pip

# Install system dependencies (for Ubuntu/Debian)
if command -v apt-get &> /dev/null; then
    echo -e "${BLUE}Installing system dependencies...${NC}"
    sudo apt-get update
    sudo apt-get install -y \
        libcairo2-dev \
        libpango1.0-dev \
        ffmpeg \
        texlive-full \
        texlive-latex-extra \
        texlive-fonts-extra \
        texlive-latex-recommended \
        texlive-science \
        tipa \
        libx11-dev \
        pkg-config \
        python3-dev

# For macOS using Homebrew
elif command -v brew &> /dev/null; then
    echo -e "${BLUE}Installing system dependencies...${NC}"
    brew install cairo pkgconfig pango ffmpeg
fi

# Install Python dependencies
echo -e "${BLUE}Installing Python dependencies...${NC}"
pip install \
    manim \
    numpy \
    scipy \
    matplotlib \
    tqdm \
    pillow \
    networkx \
    colour

# Verify installation
echo -e "${BLUE}Verifying Manim installation...${NC}"
python3 -c "import manim" && echo -e "${GREEN}Manim installed successfully!${NC}"

# Print success message
echo -e "${GREEN}Setup complete! To activate the environment:${NC}"
echo -e "source manim_env/bin/activate"

# Create a test file
echo -e "${BLUE}Creating a test file...${NC}"
cat > test_manim.py << EOL
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

EOL

echo -e "${GREEN}Test file created: test_manim.py${NC}"
echo -e "${BLUE}To run the test file:${NC}"
echo -e "manim -pql test_manim.py SquareToCircle"

# Linux/macOS
source manim_env/bin/activate
manim -pql test_manim.py SquareToCircle

# Windows
.\manim_env\Scripts\activate
manim -pql test_manim.py SquareToCircle 
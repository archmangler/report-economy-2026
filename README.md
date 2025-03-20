# Global Economy 2026 Projection Visualization
## Manim-based Economic Data Visualization Tool

### Overview
* This script creates a professional-grade animated presentation of global economic projections for 2026. 
* It uses the Manim library to generate smooth animations and transitions between different economic metrics and country groupings.
* The concept of this project is create an ongoing economic and geopolitical projection incorporating various material factors which affect the global economy, like military power, population size, advent of technological advances and trends. The final report is meant to be a realistic synthesis of complex factors required to build a holistic view of the geopolitical-economic landscape for coming years..

### Data Sources
Currently using placeholder/example data. To use actual projections, update the data dictionary with figures from:
- International Monetary Fund (IMF)
- World Bank
- Asian Development Bank (ADB)
- OECD Economic Outlook

### Key Metrics Visualized
1. GDP Nominal (in trillion USD)
2. GDP PPP (Purchasing Power Parity)
3. GDP Per Capita (in thousands USD)

### Economy Groups Covered
1. Major Global Economies:
   - United States
   - China
   - European Union
   - India
   - Russia
   - Brazil

2. ASEAN Economies:
   - Indonesia
   - Thailand
   - Singapore
   - Malaysia
   - Vietnam
   - Cambodia

### Main Functions

#### `class GlobalEconomyPresentation(Scene)`
Main presentation class that orchestrates all visualizations.

```python
def construct(self):
    # Main entry point
    # Controls the overall flow of the presentation
```

#### Title and Introduction
```python
def create_title_slide(self):
    # Creates opening title
    # "The Global Economy in 2026: Projections and Trends"
```

```python
def create_intro_animation(self):
    # Generates 3D rotating globe animation
    # Creates transition to main content
```

```python
def show_gdp_projections(self):
    # Core visualization function
    # Creates three separate charts for each metric:
    # - GDP Nominal
    # - GDP PPP
    # - GDP per Capita
    # Shows year-by-year projections (2024-2026)
```

#### Supporting Visualizations
```python
def show_global_trade(self):
    # Creates line graph for trade volumes
    # Shows trade progression over time
```

```python
def show_tech_impact(self):
    # Visualizes technology sector impact
    # Shows interconnected tech sectors
```

```python
def show_conclusion(self):
    # Presents key takeaways
    # Summarizes main findings
```

### Animation Features
- 5-second transitions between data points
- Smooth fade effects between sections
- Color-coded metrics:
  - Blue: GDP Nominal
  - Green: GDP PPP
  - Red: GDP per Capita
- Dynamic value labels
- Year indicators
- Descriptive subtitles for each metric

### Technical Details

#### Data Structure
```python
data = {
    "Country": [
        [GDP_Nominal_2024, GDP_Nominal_2025, GDP_Nominal_2026],
        [GDP_PPP_2024, GDP_PPP_2025, GDP_PPP_2026],
        [GDP_PerCapita_2024, GDP_PerCapita_2025, GDP_PerCapita_2026]
    ]
}
```

#### Chart Specifications
- Bar Charts: Used for GDP comparisons
- Line Graphs: Used for trade trends
- Network Diagrams: Used for tech sector relationships

#### Animation Parameters
- Transition duration: 5 seconds
- Wait time between sections: 3 seconds
- Fade duration: 2 seconds

### Requirements
- Python 3.7+
- Manim library
- Cairo graphics
- LaTeX installation
- FFmpeg

### Installation

#### System Dependencies
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y \
    libcairo2-dev \
    libpango1.0-dev \
    ffmpeg \
    texlive-full

# macOS
brew install cairo pkgconfig pango ffmpeg mactex
```

#### Python Environment Setup
```bash
# Create virtual environment
python3 -m venv manim_env

# Activate environment
source manim_env/bin/activate  # Linux/Mac
.\manim_env\Scripts\activate   # Windows

# Install dependencies
pip install manim numpy scipy pillow
```

### Usage

#### Basic Execution
```bash
# Run the presentation
manim -pql global_economy.py GlobalEconomyPresentation
```

#### Output Options
```bash
# High quality render
manim -pqh global_economy.py GlobalEconomyPresentation

# Medium quality with progress bar
manim -pqm global_economy.py GlobalEconomyPresentation --progress_bar=display
```

### Output Files
The script generates:
1. An MP4 video file containing the full presentation
   - Location: `./media/videos/`
   - Format: 1080p @ 60fps
2. Individual PNG frames for each key visualization
   - Location: `./media/images/`
3. LaTeX-rendered text elements
4. High-quality vector graphics

### Customization Options

#### Visual Elements
- Chart colors and styles
- Font sizes and types
- Animation timing
- Transition effects
- Background colors

#### Data Presentation
- Metric ranges
- Label formats
- Chart scales
- Country groupings
- Time periods

### Best Practices
1. Data Accuracy
   - Verify all economic data
   - Cross-reference multiple sources
   - Update projections regularly

2. Visual Clarity
   - Maintain consistent spacing
   - Ensure readable text sizes
   - Use appropriate color contrast
   - Test on different screen sizes

3. Performance
   - Pre-render complex animations
   - Optimize video output settings
   - Monitor memory usage
   - Backup rendered files

### Future Improvements
1. Data Integration
   - API connections to economic databases
   - Automated data updates
   - Real-time data visualization

2. Enhanced Interactivity
   - Click-through capabilities
   - Custom viewing speeds
   - Section selection

3. Additional Features
   - More economic indicators
   - Regional comparisons
   - Historical trends
   - Alternative projection scenarios

### Contributing
Contributions are welcome! Please consider:
- Data visualization improvements
- Animation optimization
- Additional economic metrics
- Documentation updates
- Bug fixes and testing

### License
[Specify your license here]

### Contact
[Your contact information]

### Acknowledgments
- Manim Community
- Economic Data Providers
- 3Blue1Brown for visualization inspiration

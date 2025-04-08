# Shear Force and Bending Moment Diagram Plotter

A Python tool that generates professional Shear Force Diagrams (SFD) and Bending Moment Diagrams (BMD) from structural analysis data.

## Overview

This tool reads structural analysis data from an Excel file and creates high-quality visualizations of Shear Force and Bending Moment diagrams. It's designed for structural engineers, civil engineering students, and professionals who need clear visual representations of beam behavior under loading conditions.

## Features

- **Dual Diagram Display**: Generates both SFD and BMD side by side for easy comparison
- **Automatic Value Annotation**: Labels maximum and minimum values with precise measurements
- **Professional Hatching**: Creates properly hatched diagrams following engineering conventions
- **Support Indicators**: Displays support locations with appropriate markers
- **High-Resolution Output**: Saves diagrams as high-quality PNG images
- **Detailed Console Output**: Provides exact values and positions of maximum/minimum forces and moments

## Requirements

- Python 3.x
- pandas
- matplotlib
- numpy
- Excel file with structural analysis data

## Installation

```bash
pip install pandas matplotlib numpy openpyxl
 ```

## Usage
1. Prepare your Excel file with columns for:
   
   - Distance (m)
   - SF (kN) - Shear Force values
   - BM (kN-m) - Bending Moment values
2. Run the script:
```bash
python plot_sfdbmd.py
 ```

3. The script will:
   - Read data from 'SFS_Screening_SFDBMD.xlsx'
   - Generate and display the diagrams
   - Save the output as 'SFDBMD_Plot.png'
   - Print key values to the console
## Example Output
The generated plot includes:

- Left side: Bending Moment Diagram (BMD) in red
- Right side: Shear Force Diagram (SFD) in blue
- Hatched areas indicating magnitude and direction
- Annotations showing maximum positive and negative values
- Support indicators at beam endpoints
## Error Handling
The script includes robust error handling to:

- Detect issues with the Excel file format
- Display available sheets if the expected data isn't found
- Show sample data to help diagnose formatting problems



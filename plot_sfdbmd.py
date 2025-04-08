import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the Excel file
excel_file = 'SFS_Screening_SFDBMD.xlsx'
try:
    # Try to read the data from Excel file
    df = pd.read_excel(excel_file)
    print("Excel data columns:", df.columns.tolist())
    
    # Use the correct column names as found in the Excel file
    x = df['Distance (m)']
    shear = df['SF (kN)']
    moment = df['BM (kN-m)']
    
    # Get exact max/min values from the Excel file for annotations
    max_sf = shear.max()  # 16.961 kN
    min_sf = shear.min()  # -37.257 kN
    max_bm = moment.max()  # 60.886 kN-m
    min_bm = moment.min()  # -29.701 kN-m
    
    # Create a figure with two subplots side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
    
    # Plot Bending Moment Diagram (left side as in reference)
    ax1.plot(x, moment, 'r-', linewidth=2)
    
    # Create hatching effect similar to the reference image for BMD
    for i in range(len(x)-1):
        if moment[i] > 0:
            ax1.fill([x[i], x[i], x[i+1], x[i+1]], [0, moment[i], moment[i+1], 0], 'r', alpha=0.3)
            # Add vertical lines for hatching effect
            num_hatches = max(2, int((x[i+1] - x[i]) * 10))  # Adjust density
            for j in range(num_hatches):
                hx = x[i] + (x[i+1] - x[i]) * j / num_hatches
                h1 = 0
                h2 = moment[i] + (moment[i+1] - moment[i]) * j / num_hatches
                if h2 > 0:
                    ax1.plot([hx, hx], [h1, h2], 'r-', linewidth=0.5, alpha=0.5)
        elif moment[i] < 0:
            ax1.fill([x[i], x[i], x[i+1], x[i+1]], [0, moment[i], moment[i+1], 0], 'r', alpha=0.3)
            # Add vertical lines for hatching effect
            num_hatches = max(2, int((x[i+1] - x[i]) * 10))  # Adjust density
            for j in range(num_hatches):
                hx = x[i] + (x[i+1] - x[i]) * j / num_hatches
                h1 = 0
                h2 = moment[i] + (moment[i+1] - moment[i]) * j / num_hatches
                if h2 < 0:
                    ax1.plot([hx, hx], [h1, h2], 'r-', linewidth=0.5, alpha=0.5)
    
    # Add arrows for supports (assuming at start and end)
    ax1.annotate('', xy=(x.iloc[0], 0), xytext=(x.iloc[0], -10),
                arrowprops=dict(facecolor='black', width=1.5, headwidth=8))
    ax1.annotate('', xy=(x.iloc[-1], 0), xytext=(x.iloc[-1], -10),
                arrowprops=dict(facecolor='black', width=1.5, headwidth=8))
    
    # Annotations for BMD max/min values with exact values from Excel
    if max_bm > 0:
        pos_max_idx = moment.idxmax()
        ax1.annotate(f'Max: {max_bm:.3f} kN-m', 
                    xy=(x[pos_max_idx], max_bm),
                    xytext=(x[pos_max_idx] - 0.5, max_bm + 5),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6),
                    fontsize=9)
    
    if min_bm < 0:
        neg_max_idx = moment.idxmin()
        ax1.annotate(f'Max: {abs(min_bm):.3f} kN-m', 
                    xy=(x[neg_max_idx], min_bm),
                    xytext=(x[neg_max_idx] - 0.5, min_bm - 5),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6),
                    fontsize=9)
    
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.set_title('Bending Moment Diagram (BMD)', fontsize=12)
    ax1.set_xlabel('Position (m)', fontsize=10)
    ax1.set_ylabel('Bending Moment (kN-m)', fontsize=10)
    
    # Plot Shear Force Diagram (right side as in reference)
    ax2.plot(x, shear, 'b-', linewidth=2)
    
    # Create hatching effect similar to the reference image for SFD
    for i in range(len(x)-1):
        if shear[i] > 0:
            ax2.fill([x[i], x[i], x[i+1], x[i+1]], [0, shear[i], shear[i+1], 0], 'b', alpha=0.3)
            # Add vertical lines for hatching effect
            num_hatches = max(2, int((x[i+1] - x[i]) * 10))  # Adjust density
            for j in range(num_hatches):
                hx = x[i] + (x[i+1] - x[i]) * j / num_hatches
                h1 = 0
                h2 = shear[i] + (shear[i+1] - shear[i]) * j / num_hatches
                if h2 > 0:
                    ax2.plot([hx, hx], [h1, h2], 'b-', linewidth=0.5, alpha=0.5)
        elif shear[i] < 0:
            ax2.fill([x[i], x[i], x[i+1], x[i+1]], [0, shear[i], shear[i+1], 0], 'b', alpha=0.3)
            # Add vertical lines for hatching effect
            num_hatches = max(2, int((x[i+1] - x[i]) * 10))  # Adjust density
            for j in range(num_hatches):
                hx = x[i] + (x[i+1] - x[i]) * j / num_hatches
                h1 = 0
                h2 = shear[i] + (shear[i+1] - shear[i]) * j / num_hatches
                if h2 < 0:
                    ax2.plot([hx, hx], [h1, h2], 'b-', linewidth=0.5, alpha=0.5)
    
    # Add arrows for supports (assuming at start and end)
    ax2.annotate('', xy=(x.iloc[0], 0), xytext=(x.iloc[0], -10),
                arrowprops=dict(facecolor='black', width=1.5, headwidth=8))
    ax2.annotate('', xy=(x.iloc[-1], 0), xytext=(x.iloc[-1], -10),
                arrowprops=dict(facecolor='black', width=1.5, headwidth=8))
    
    # Annotations for SFD max/min values with exact values from Excel
    if max_sf > 0:
        pos_max_idx = shear.idxmax()
        ax2.annotate(f'Max: {max_sf:.3f} kN', 
                    xy=(x[pos_max_idx], max_sf),
                    xytext=(x[pos_max_idx] - 0.5, max_sf + 3),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6),
                    fontsize=9)
    
    if min_sf < 0:
        neg_max_idx = shear.idxmin()
        ax2.annotate(f'Max: {abs(min_sf):.3f} kN', 
                    xy=(x[neg_max_idx], min_sf),
                    xytext=(x[neg_max_idx] - 0.5, min_sf - 3),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6),
                    fontsize=9)
    
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.set_title('Shear Force Diagram (SFD)', fontsize=12)
    ax2.set_xlabel('Position (m)', fontsize=10)
    ax2.set_ylabel('Shear Force (kN)', fontsize=10)
    
    # Add a title below the subplots matching exactly the reference image
    plt.figtext(0.5, 0.01, 'Bending Moment Diagram (Left) & Shear Force Diagram (Right)', 
                ha='center', fontsize=12, fontstyle='italic')
    
    # Adjust spacing between subplots
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    
    # Save the figure with high resolution
    plt.savefig('SFDBMD_Plot.png', dpi=300, bbox_inches='tight')
    print("Plot saved as SFDBMD_Plot.png")
    print(f"Correctly plotted with Excel values:")
    print(f"  Max SF: {max_sf:.3f} kN at position {x[shear.idxmax()]:.3f} m")
    print(f"  Min SF: {min_sf:.3f} kN at position {x[shear.idxmin()]:.3f} m")
    print(f"  Max BM: {max_bm:.3f} kN-m at position {x[moment.idxmax()]:.3f} m")
    print(f"  Min BM: {min_bm:.3f} kN-m at position {x[moment.idxmin()]:.3f} m")
    
    # Show the plot
    plt.show()
    
except Exception as e:
    print(f"Error: {e}")
    
    # If there's an error with the Excel file, try to print its structure
    try:
        xls = pd.ExcelFile(excel_file)
        print("Available sheets:", xls.sheet_names)
        
        # Read the first sheet to see its structure
        first_sheet = pd.read_excel(excel_file, sheet_name=0)
        print("First few rows of data:")
        print(first_sheet.head())
        
    except Exception as inner_e:
        print(f"Additional error examining Excel file: {inner_e}") 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Manufacturing Performance Analysis
# Contact: 23f3002525@ds.study.iitm.ac.in

# Equipment Efficiency Rate - 2024 Quarterly Data
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Efficiency_Rate': [70.71, 78.83, 80.04, 77.79]
}

df = pd.DataFrame(data)

# Calculate average
average_efficiency = df['Efficiency_Rate'].mean()
industry_target = 90

print(f"Average Equipment Efficiency Rate: {average_efficiency:.2f}")
print(f"Industry Target: {industry_target}")
print(f"Gap to Target: {industry_target - average_efficiency:.2f}")

# Create visualizations
plt.figure(figsize=(12, 8))

# Subplot 1: Quarterly Trend
plt.subplot(2, 2, 1)
plt.plot(df['Quarter'], df['Efficiency_Rate'], marker='o', linewidth=2, markersize=8)
plt.axhline(y=industry_target, color='r', linestyle='--', label='Industry Target (90)')
plt.axhline(y=average_efficiency, color='g', linestyle='--', label=f'Current Average ({average_efficiency:.2f})')
plt.title('Equipment Efficiency Rate - 2024 Quarterly Trend')
plt.xlabel('Quarter')
plt.ylabel('Efficiency Rate')
plt.legend()
plt.grid(True, alpha=0.3)

# Subplot 2: Gap Analysis
plt.subplot(2, 2, 2)
gap = industry_target - df['Efficiency_Rate']
colors = ['red' if x > 0 else 'green' for x in gap]
plt.bar(df['Quarter'], gap, color=colors, alpha=0.7)
plt.title('Gap to Industry Target by Quarter')
plt.xlabel('Quarter')
plt.ylabel('Gap (Target - Actual)')
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

# Subplot 3: Performance Distribution
plt.subplot(2, 2, 3)
plt.hist(df['Efficiency_Rate'], bins=4, alpha=0.7, color='skyblue', edgecolor='black')
plt.axvline(x=average_efficiency, color='g', linestyle='--', label=f'Average ({average_efficiency:.2f})')
plt.axvline(x=industry_target, color='r', linestyle='--', label='Target (90)')
plt.title('Efficiency Rate Distribution')
plt.xlabel('Efficiency Rate')
plt.ylabel('Frequency')
plt.legend()

# Subplot 4: Improvement Required
plt.subplot(2, 2, 4)
improvement_needed = industry_target - df['Efficiency_Rate']
plt.bar(df['Quarter'], improvement_needed, color='orange', alpha=0.7)
plt.title('Improvement Required by Quarter')
plt.xlabel('Quarter')
plt.ylabel('Points to Reach Target')

plt.tight_layout()
plt.savefig('manufacturing_performance_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Statistical Analysis
print("\n=== STATISTICAL ANALYSIS ===")
print(f"Standard Deviation: {df['Efficiency_Rate'].std():.2f}")
print(f"Minimum: {df['Efficiency_Rate'].min()}")
print(f"Maximum: {df['Efficiency_Rate'].max()}")
print(f"Range: {df['Efficiency_Rate'].max() - df['Efficiency_Rate'].min():.2f}")

# Trend Analysis
trend = np.polyfit(range(len(df)), df['Efficiency_Rate'], 1)[0]
print(f"Quarterly Trend: {trend:.2f} points per quarter")

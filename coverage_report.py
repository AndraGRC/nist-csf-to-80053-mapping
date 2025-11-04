import pandas as pd
import matplotlib.pyplot as plt

controls = pd.read_csv('nist-800-53-controls-with-enhancements.csv')
mapping = pd.read_csv('nist-csf-to-80053-mapping.csv')
csf = pd.read_csv('nist-csf-functions.csv')

# Filter only CONTROL rows for counts
controls_only = controls[controls['Row_Type']=='CONTROL'].copy()

# Join mapping -> controls to know family
m = mapping.merge(controls_only, left_on='80053_Control_ID', right_on='Control_ID', how='left')

# Coverage by family
fam_counts = m.groupby('Control_Family').size().sort_values(ascending=False)
plt.figure()
fam_counts.plot(kind='bar')
plt.title('Mapped 800-53 Controls by Family')
plt.tight_layout()
plt.savefig('coverage_by_family.png')

# Coverage by CSF Function
csf_func = mapping.merge(csf[['CSF_ID','CSF_Function']], on='CSF_ID', how='left')
func_counts = csf_func.groupby('CSF_Function').size().sort_values(ascending=False)
plt.figure()
func_counts.plot(kind='bar')
plt.title('Mappings by CSF Function')
plt.tight_layout()
plt.savefig('mappings_by_csf_function.png')

# Save summary CSVs
fam_counts.to_frame('Count').to_csv('summary_family_counts.csv')
func_counts.to_frame('Count').to_csv('summary_function_counts.csv')

print('Generated: coverage_by_family.png, mappings_by_csf_function.png, summary_family_counts.csv, summary_function_counts.csv')
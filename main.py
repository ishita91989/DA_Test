import pandas as pd
import sweetviz as sv

df = pd.read_csv('DAtest.csv')
report = sv.analyze(df)
report.show_html('DAtest_sweetviz.html')
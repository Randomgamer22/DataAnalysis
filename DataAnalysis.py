import pandas as pd
import plotly.express as px

df = pd.read_csv("csvfiles/Student_data.csv")
df_1 = df.drop_duplicates(subset = ['student_id', 'level']).reset_index()
attempts_df = df.groupby(['student_id', 'level'])['attempt'].mean()
del df_1['index']
print(df_1)
print(attempts_df)

fig = px.scatter(df_1, x = 'student_id', y = 'level', size = attempts_df, color = attempts_df)
fig.show()
import pandas as pd
import numpy as np


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labe
                  ls)
print(df.head(3))
        name  score  attempts qualify
a  Anastasia   12.5         1     yes
b       Dima    9.0         3      no
c  Katherine   16.5         2     yes
df = df.dropna()
new_df = df[['name', 'score']]
new_row = {'name': 'Suresh', 'score': 15.5, 'attempts': 1, 'qualify': 'yes'}
df = df.append(new_row, ignore_index=True)

  df = df.append(new_row, ignore_index=True)
df = df.drop('attempts', axis=1)
df['Success'] = df['score'].apply(lambda x: 1 if x > 10 else 0)
df.to_csv('my_data.csv', index=False)
 
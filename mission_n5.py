import matplotlib.pyplot as plt
import num2words as n2w
import pandas as pd
from faker import Faker
from wordcloud import WordCloud

# *********** CREATING AND SAVING DATA FILE *******************

fake = Faker()

names = []
numbers = []

for i in range(50):
    students_name = fake.name()
    student_grades = fake.random_int(1, 10)
    names.append(students_name)
    numbers.append(student_grades)

raw_data = {'names': names,
            'grades': numbers}
df = pd.DataFrame(raw_data, columns=['names', 'grades'])
df.to_csv('data_student_grades.csv', index=False)
file = pd.read_csv('data_student_grades.csv')

# ******************** HISTOGRAM ****************

grades = file['grades'].values
n, bins, columns = plt.hist(grades, density=True, facecolor='blue', alpha=0.75)  # noqa
plt.xlabel('Values')
plt.ylabel('Probability')
plt.title('Histogram of values')
plt.grid(True)
plt.show()


# ******************** WORD CLOUD ****************
word_numbers = []
for i in range(50):
    word_numbers.append(n2w.num2words(grades[i], lang='pt-BR'))
    i += 1

text = " ".join(text for text in word_numbers)

word_cloud = WordCloud(background_color='black', width=800, height=400).generate(text)  # noqa
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')
word_cloud.to_file('Words_cloud.png')

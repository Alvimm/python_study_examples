import matplotlib.pyplot as plt
import num2words as n2w
import pandas as pd
from faker import Faker
from wordcloud import WordCloud

fake = Faker()
column_of_names = []
column_of_numbers = []
quantity_of_names_and_numbers = 50
word_numbers = []

for i in range(quantity_of_names_and_numbers):
    students_name = fake.name()
    students_grade = fake.random_int(1, 10)
    column_of_names.append(students_name)
    column_of_numbers.append(students_grade)

creating_data = {'names': column_of_names,
                 'grades': column_of_numbers}
treating_data = pd.DataFrame(creating_data, columns=['names', 'grades'])
treating_data.to_csv('data_student_grades.csv', index=False)
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
for i in range(quantity_of_names_and_numbers):
    word_numbers.append(n2w.num2words(grades[i], lang='pt-BR'))
    i += 1

text = " ".join(text for text in word_numbers)
word_cloud = WordCloud().generate(text)
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')
plt.show()
# word_cloud.to_file('words_cloud_image.png')

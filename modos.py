import os

for i in os.listdir('test'):
    for j in os.listdir(f'test/{i}'):
        if j == 'lesson_10':
            os.removedirs(f'test/{i}/lesson_10')
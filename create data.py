import os
import shutil
import sys

# creating paths to our 'train_images' and 'test_images' directories
train_image_dir = os.path.join(os.getcwd(), 'train_images')
test_image_dir = os.path.join(os.getcwd(), 'test_images')

def create_path(path):
    
    '''
    this function takes in a directory path and checks if the path exists or not
    if the path does not exist then it creates a new directory for the specified path
    '''
    
    if not os.path.exists(path):
        drt = path.split('/')[-1]
        print(f"Directory doesn't exist. Making '{drt}' directory now!")
        print("----------------------------------------------------------------")
        os.mkdir(path)

def move_file(file_source, file_destination_train, file_destination_test, test_size):
    
    '''
    this function takes the file source path and train/test path alongwith the test size
    of a specific category i.e., COVID, Normal, Viral Pneumonia and moves the files based
    on the test size (for now we have set the test size at 20% of our total data per 
    category)
    '''
    
    for i, file in enumerate(os.listdir(file_source)):
    
        file_path = os.path.join(file_source, file)
    
        if i < test_size:
            shutil.move(file_path, file_destination_test)    
        else:
            shutil.move(file_path, file_destination_train)

# setting path to our covid images, normal images, and pneumonia images
covid_files = 'Radiography_Data/COVID/images'
covid_path = os.path.join(os.getcwd(), covid_files)

normal_files = 'Radiography_Data/Normal/images'
normal_path = os.path.join(os.getcwd(), normal_files)

pneumonia_files = 'Radiography_Data/Viral Pneumonia/images'
pneumonia_path = os.path.join(os.getcwd(), pneumonia_files)

# setting path to training folders for our categories
covid_train = os.path.join(train_image_dir, 'COVID')
normal_train = os.path.join(train_image_dir, 'Normal')
pneumonia_train = os.path.join(train_image_dir, 'Viral Pneumonia')

# setting path to test folders for our categories
covid_test = os.path.join(test_image_dir, 'COVID')
normal_test = os.path.join(test_image_dir, 'Normal')
pneumonia_test = os.path.join(test_image_dir, 'Viral Pneumonia')

# creating path to train image directory alongwith the respective categories
create_path(train_image_dir)
create_path(covid_train)
create_path(normal_train)
create_path(pneumonia_train)

# creating path to test image directory alongwith the respective categories
create_path(test_image_dir)
create_path(covid_test)
create_path(normal_test)
create_path(pneumonia_test)

# checking the total number of images available per category
NUM_COVID = len(os.listdir(covid_path))
NUM_NORMAL = len(os.listdir(normal_path))
NUM_PNEUMONIA = len(os.listdir(pneumonia_path))

print(f'\nNumber of training images by category:')
print(f'COVID: {NUM_COVID} \nNormal: {NUM_NORMAL} \nViral Pneumonia: {NUM_PNEUMONIA}')

# setting the total number of test images to 20% of total available images per category
TEST_SIZE_C = int(NUM_COVID * 0.20)
TEST_SIZE_N = int(NUM_NORMAL * 0.20)
TEST_SIZE_P = int(NUM_PNEUMONIA * 0.20)

print(f'\nNumber of test images by category:')
print(f'COVID: {TEST_SIZE_C} \nNormal: {TEST_SIZE_N} \nViral Pneumonia: {TEST_SIZE_P}')

# moving files to train/test directories 
move_file(covid_path, covid_train, covid_test, TEST_SIZE_C)
move_file(normal_path, normal_train, normal_test, TEST_SIZE_N)
move_file(pneumonia_path, pneumonia_train, pneumonia_test, TEST_SIZE_P)
print('\nImages have been successfully moved to the respective directories!')
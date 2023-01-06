# VGGNET

A transfer learning approach to predict COVID-19 from a chest X-ray of a patient.

## What is COVID-19?

COVID-19 is an infectious disease caused by SARS-COV-2 virus. It's first outbreak was during 2020 in the city of Wuhan, China. Within a short period of
4 months almost 90% of the world was reporting its cases. In the beginning the mortality rate of the virus was quite high which became a serious concern
worldwide. As of January 2023, 663 million cases of virus infections have been reported with around 6.7 million deaths worldwide. 

![covid-19](https://images.unsplash.com/photo-1583324113626-70df0f4deaab?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2832&q=80)

### Symptoms

* fever or chills
* cough
* shortness of breath
* difficulty in breathing
* fatigue
* muscle or body aches
* headaches
* loss of sense of smell or taste

### Diagnosis

The diagnosis of COVID-19 is made by direct detection of SARS-CoV-2 RNA using nucleic acid amplification tests (NAATs) or by detection of viral protein 
using an antigen test. A positive NAAT or antigen test is generally indicative of infection and does not need to be repeated. To test for the COVID-19 virus, 
a health care provider takes a sample from the nose (nasopharyngeal swab), throat (throat swab) or saliva. The samples are then sent to a lab for testing.

![covid-testing](https://images.unsplash.com/photo-1628246972740-e778a24742a9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80)

### References

* [WHO](https://covid19.who.int/)
* [Wikipedia](https://en.wikipedia.org/wiki/COVID-19)

## About the dataset

The dataset is publicly available on kaggle for download and can be used in personal projects. The dataset consist of chest X-rays that fall under three categories
namely COVID-19, Normal, and Viral Pneumonia. There are around 12,000 images in total. You can download the dataset from [here.](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database)

## How to get started?

Open the terminal on your mac and type 
```html
mkdir covid
```
Then switch to the new directory using
```html
cd covid
```
Now clone the repository on your local machine using
```html
git clone https://github.com/kotiyalanurag/VGGNET-COVID-19.git
```
Now create a virtual environment using assuming you have python installed on your machine
```html
python -m venv env
```
Switch on your new environment using
```html
source env/bin/activate
```
Now install the requirements for this project using
```html
pip install -r requirements.txt
```
Now just download the dataset from [kaggle](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database), 
unzip the folder and rename the main folder to "Radiography_Data".
Then run the following on terminal
```html
python create data.py
```
Your folder structure will be generated. Now you can open the jupyter notebook and have fun playing with it. 

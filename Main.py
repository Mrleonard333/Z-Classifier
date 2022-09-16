import pandas as pd
from os import system
from time import sleep
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# v Import the modules that will be used
LB = LabelEncoder()                 # v Will only get the three closest datas
KNN = KNeighborsClassifier(n_neighbors=3)
RFC = RandomForestClassifier()

SYMPTOMS = pd.read_csv('SYMPTOMS.csv') # < Get the data from the CSV file
X1 = SYMPTOMS.drop('Result', axis=1)
Y1 = SYMPTOMS.Result

# v Transform the data for the machine training
X1['skin_tone'] = LB.fit_transform(X1['Old_skin_tone'])
X1['eye_color'] = LB.fit_transform(X1['Old_eye_color'])
X1['mental_health'] = LB.fit_transform(X1['Old_mental_health'])
X1 = X1.drop(['Old_skin_tone', 'Old_eye_color', 'Old_mental_health'], axis=1)
RFC.fit(X1, Y1) # < Make the machine training

TYPE = pd.read_csv('TYPE.csv')
X2 = TYPE.drop('Result', axis=1)
Y2 = TYPE.Result
KNN.fit(X2, Y2)

system('cls')

print('[Coding_Foundation] - [Z-Classifier]\n')
sleep(1)
print('[0] Common')
sleep(0.5)
print('[1] Grey')
sleep(0.5)
print('[2] White\n')
sleep(1)
ST = int(input("[NUMBER] What is the patient's skin tone?: "))

system('cls')

print('[Coding_Foundation] - [Z-Classifier]\n')
sleep(1)
print('[0] Common')
sleep(0.5)
print('[1] Green')
sleep(0.5)
print('[2] Red')
sleep(0.5)
print('[3] White\n')
sleep(1)
YC = int(input("[NUMBER] What is the patient's eye color?: "))

system('cls')

print('[Coding_Foundation] - [Z-Classifier]\n')
sleep(1)
print('[0] Bad')
sleep(0.5)
print('[1] Good')
sleep(0.5)
print('[2] Horrible\n')
sleep(1)
MH = int(input("[NUMBER] What is the patient's mental health?: "))

system('cls')   # v Will classify the data
RESULT = RFC.predict([[ST,YC,MH]])
system('cls')

print('[Coding_Foundation] - [Z-Classifier]\n')
sleep(1)
print(f'Result[{RESULT[0]}]')
sleep(0.5)          # v Show the precision of the machine
print(f'Precision[{RFC.score(X1, Y1)}]\n')
sleep(1)
if RESULT[0] == 'Zombie':
    input('[NUMBER/STRING] Continue: ')

elif RESULT[0] == 'Infected':
    print('Be carefull, the patient can turn into a zombie any time...')
    exit()

elif RESULT[0] == 'Human':
    print('The patient is not infected...')
    exit()

system('cls')

print('[Coding_Foundation] - [Z-Classifier]\n')
sleep(1)
TL = float(input("[NUMBER] What is the zombie's teeth length?: "))
if TL > 3.5: TL = 3.5
sleep(0.5)
NL = float(input("[NUMBER] What is the zombie's nails length?: "))
if NL > 4.5: NL = 4.5
sleep(0.5)
EW = float(input("[NUMBER] What is the zombie's ears width?: "))
if EW > 8.5: EW = 8.5
sleep(0.5)

system('cls')
RESULT = KNN.predict([[TL,NL,EW]])
system('cls')

print('[Coding_Foundation] - [Z-Classifier]\n')
sleep(1)
print(f'Result[{RESULT[0]}]')
sleep(0.5)
print(f'Precision[{KNN.score(X2, Y2)}]\n')
sleep(1)
print('[Contain process starting]')
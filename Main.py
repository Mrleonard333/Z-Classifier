import pandas as pd
from os import system
from time import sleep
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

def Clear():
    system('clear')
    system('cls')

LE = LabelEncoder()                 # v Will only get the three closest datas
KNN = KNeighborsClassifier(n_neighbors=3)
RFC = RandomForestClassifier()

SYMPTOMS = pd.read_csv('SYMPTOMS.csv') # < Get the data from the CSV file
Input_1 = SYMPTOMS.drop('Result', axis=1)
Output_1 = SYMPTOMS.Result

# v Transform the data for the machine training
Input_1['New_Skin_Tone'] = LE.fit_transform(X1['Skin_tone'])
Input_1['New_Eye_Color'] = LE.fit_transform(X1['Eye_color'])
Input_1['New_Mental_Health'] = LE.fit_transform(X1['Mental_Health'])
Input_1 = Input_1.drop(['Skin_tone', 'Eye_color', 'Mental_Health'], axis=1)
RFC.fit(Input_1, Output_1) # < Make the machine training

TYPE = pd.read_csv('TYPE.csv')
Input_2 = TYPE.drop('Result', axis=1)
Output_2 = TYPE.Result
KNN.fit(Input_2, Output_2)

Clear()

print('[Coding_Foundation] - [Z-Classifier]\n')
sleep(1)
print('[0] Common')
sleep(0.5)
print('[1] Grey')
sleep(0.5)
print('[2] White\n')
sleep(1)
Skint_Tone = int(input("[NUMBER] What is the patient's skin tone?: "))

Clear()

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
Eye_Color = int(input("[NUMBER] What is the patient's eye color?: "))

Clear()

print('[Coding_Foundation] - [Z-Classifier]\n')
sleep(1)
print('[0] Bad')
sleep(0.5)
print('[1] Good')
sleep(0.5)
print('[2] Horrible\n')
sleep(1)
Mental_Health = int(input("[NUMBER] What is the patient's mental health?: "))

Clear()        # v Will classify the data
RESULT = RFC.predict([[Skint_Tone,Eye_Color,Mental_Health]])
Clear()

print('[Coding_Foundation] - [Z-Classifier]\n')
sleep(1)
print(f'Result[{RESULT[0]}]')
sleep(0.5)          # v Show the precision of the machine
print(f'Precision[{RFC.score(Input_1, Output_1)}]\n')
sleep(1)
if RESULT[0] == 'Zombie':
    input('[NUMBER/STRING] Continue: ')

elif RESULT[0] == 'Infected':
    print('Be carefull, the patient can turn into a zombie any time...')
    exit()

elif RESULT[0] == 'Human':
    print('The patient is not infected...')
    exit()

Clear()

print('[Coding_Foundation] - [Z-Classifier]\n')
sleep(1)
Teeth = float(input("[NUMBER] What is the zombie's teeth length?: "))
if Teeth > 3.5:
    Teeth = 3.5
sleep(0.5)
Nails = float(input("[NUMBER] What is the zombie's nails length?: "))
if Nails > 4.5:
    Nails = 4.5
sleep(0.5)
Ears_and_Width = float(input("[NUMBER] What is the zombie's ears width?: "))
if Ears_and_Width > 8.5:
    Ears_and_Width = 8.5
sleep(0.5)

Clear()
RESULT = KNN.predict([[Teeth,Nails,Ears_and_Width]])
Clear()

print('[Coding_Foundation] - [Z-Classifier]\n')
sleep(1)
print(f'Result[{RESULT[0]}]')
sleep(0.5)
print(f'Precision[{KNN.score(Input_2, Output_2)}]\n')
sleep(1)
print('[Contain process starting]')
# [Z-Classifier]

## A system that classify the user data with a zombie theme.
![Illustrative_Zombie](https://static.wikia.nocookie.net/plague-inc/images/7/75/Versão2_IRM_Estágio_6_Vírus_Necroa.png/revision/latest?cb=20191029002223&path-prefix=pt-br)
## The system use the [sklearn](https://scikit-learn.org/stable/index.html) library<br>With the [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html?highlight=kneighborsclassifier#sklearn.neighbors.KNeighborsClassifier) and [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html?highlight=randomforestclassifier#sklearn.ensemble.RandomForestClassifier).

# [Example]
```
 /---------------------------------------------------\
  [Coding_Foundation] - [Z-Classifier]

   [0] Common
   [1] Grey
   [2] White

  [NUMBER] What is the patient's skin tone?: 1
 |---------------------------------------------------|
  [Coding_Foundation] - [Z-Classifier]

  [0] Common
  [1] Green
  [2] Red
  [3] White
  
  [NUMBER] What is the patient's eye color?: 2
 |---------------------------------------------------|
  [Coding_Foundation] - [Z-Classifier]

  [0] Bad
  [1] Good
  [2] Horrible

  [NUMBER] What is the patient's mental health?: 2
 |---------------------------------------------------|
  [Coding_Foundation] - [Z-Classifier]

  Result[Zombie]
  Precision[1.0]

  [NUMBER/STRING] Continue:
 |---------------------------------------------------|
  [Coding_Foundation] - [Z-Classifier]

  [NUMBER] What is the zombie's teeth length?: 1.0
  [NUMBER] What is the zombie's nails length?: 1.0
  [NUMBER] What is the zombie's ears width?: 4.0
 |---------------------------------------------------|
  [Coding_Foundation] - [Z-Classifier]
 
  Result[Common_Zombie]
  Precision[1.0]

  [Contain process starting]
 \---------------------------------------------------/
```

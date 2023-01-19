# [Z-Classifier]

## A system that classify the user data with a zombie theme.
![Illustrative_Zombie](https://camo.githubusercontent.com/858c59bc6b5d9e0af36b8a5ae40d3d77f1b90fc39460864fc765c152d2ec47af/68747470733a2f2f7374617469632e77696b69612e6e6f636f6f6b69652e6e65742f706c616775652d696e632f696d616765732f372f37352f566572732543332541336f325f49524d5f45737425433325413167696f5f365f562543332541447275735f4e6563726f612e706e672f7265766973696f6e2f6c61746573743f63623d323031393130323930303232323326706174682d7072656669783d70742d6272)
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

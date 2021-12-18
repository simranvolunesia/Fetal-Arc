# Fetal-Arc
Predicting Fetal Health, and Birth-Weight of fetus using Machine Learning

## Abstract
> The moment a child is born, the mother is also born. She never existed before. The woman existed, but the mother, never. A mother is something absolutely new.

<p align="justify">The lines talk about pregnancy, which is one of the most beautiful phases in women’s life. To make it nicer and easier, it is utmost important to take care of fetal health. </p>

This project focuses on machine learning techniques used for predicting 
1. Fetal Health as Normal, Suspect or Pathological using cardiotocography (CTG) data 
2. Birth weight of baby using gestational age and mother’s features. 
<p align="justify">For <strong>birth weight prediction</strong>, <i>RandomForestRegressor</i> and <i>AdaBoostRegressor</i> are used in a weighted fashion to give final result of birth weight in kgs, 
with <strong>root mean squared error (rmse) being 0.42 on train set and 0.44 on test set</strong>. Going for the second problem of predicting <strong>fetal health as normal, suspect or pathological</strong>, 
<i>Support Vector Classifier, Decision Tree Classifier, Adaboost Classifier, Random Forest Classifier</i> are used and through <i>majority voting</i> the final label is assigned. 
This technique gave <strong>macro recall score of 0.95 on train set and 0.92 on test set</strong>.</p>

## Why to address this problem?
<p align="justify"> Pregnancy is the most delightful period. Healthy
pregnancy leads to healthy baby. So fetal care
becomes utmost important. According to WHO,
one million babies die within 24 hours of birth
due to premature birth and complications during
birth. Also, around 810 women die each day during
delivery or soon after delivery. This really causes
the need to take care of fetus with utmost priority.</p>

## Problem Background
<p align="justify">
Cardiotocography (CTG) is well-known and
most widely used method to know about fetal
health which records (graph) the fetal heartbeat
(cardio) and uterine contractions (toco) of mother
during pregnancy. It is carried out during third
trimester or sometimes even during final trimester
and during delivery so as to know if fetal heartbeat is not hampered by uterine contractions. For
mother and fetus various parameters are measured which are also captured in dataset. Normal condition occurs
when every parameter is within desired range, fetal health is suspectible when one of parameters is
abnormal and pathological when more than one parameters are not normal. In case of suspectible, call
is made for more tests while for pathological state,
there are emergency actions taken by the doctor.
The machine learning algorithms provide a quick
support and equip the doctors to take actions immediately in case the fetus is in abnormal condition.</p>
<p align="justify">
Birth weight stands most crucial for fetus, defining the risk during delivery, mortality rate within
one year and somewhat related to diseases that
occur in adulthood. Birth weight is difficult to
measure directly but a rough estimate can be made
by experienced doctors. Low birth weight can potentially causes major issues and Over weight can
lead to serious injuries to mother and fetus during
delivery, hence getting even a rough estimate in
this direction would also serve to be of great help.
Various machine learning techniques can be employed to predict fetal birth weight by exploiting
the features of mother.
</p>

## Links for dataset
<div>Fetal Health Classification: https://www.kaggle.com/andrewmvd/fetal-health-classification</div>
<div>Birth Weight Prediction: http://people.reed.edu/~jones/141/Bwt.dat</div>

## Link for deployed website
https://fetalhealth-simran.herokuapp/

For more details, kindly have a look at repository and attached report, ppt

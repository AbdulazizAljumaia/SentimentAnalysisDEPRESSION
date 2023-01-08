import pandas as pd

dataset = pd.read_excel('depressed.xlsx')

neg = []
pos = []

for i in range(len(dataset)):
    if dataset.label[i] == 0:
        neg.append(dataset.text[i])
    elif dataset.label[i] == 1:
        pos.append(dataset.text[i])
        
neg = neg[:len(pos)]

negData = pd.DataFrame([' '.join(neg).split(' ')]).T
posData = pd.DataFrame([' '.join(pos).split(' ')]).T

negDataPD = pd.DataFrame(negData.groupby(0).size())
posDataPD = pd.DataFrame(posData.groupby(0).size())

negDataPD.columns = ['label']
posDataPD.columns = ['label']
posDataPD['Token'] = posDataPD.index
negDataPD['Token'] = negDataPD.index

posDataPD = posDataPD.reset_index(drop=True)
negDataPD = negDataPD.reset_index(drop=True)


test = 'أنا تعبت وأحس أني بموت من الإكتئاب'
newTest = test.split(' ')

weghtsNeg = []
wehgtsPos = []

for i in range(len(newTest)):
    for j in range(len(negDataPD)):
        if newTest[i] == negDataPD['Token'][j]:
            weghtsNeg.append(negDataPD['label'][j])
            
    for q in range(len(posDataPD)):
        if newTest[i] == posDataPD['Token'][q]:
            wehgtsPos.append(posDataPD['label'][q])
        
Summed_weight = []
for i, j in zip(weghtsNeg,wehgtsPos):
    if j > i:
        Summed_weight.append('pos')
    elif i > j:
        Summed_weight.append('neg')
    elif i == j:
        Summed_weight.append('neut')

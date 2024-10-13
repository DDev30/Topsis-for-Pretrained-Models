import numpy as np

def topsis(data, weights):
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1_score', 'ROC-AUC']
    
    
    norm = np.sqrt((data[metrics] ** 2).sum())
    normalized_data = data[metrics] / norm  

    
    for i, col in enumerate(metrics):
        normalized_data[col] *= weights[col]

    ideal = normalized_data.max()
    anti_ideal = normalized_data.min()
    
    data['D_Ideal'] = np.sqrt(((normalized_data - ideal) ** 2).sum(axis=1))
    data['D_Anti'] = np.sqrt(((normalized_data - anti_ideal) ** 2).sum(axis=1))
    
    data['T_Score'] = data['D_Anti'] / (data['D_Ideal'] + data['D_Anti'])
    data['Rnk'] = data['T_Score'].rank(ascending=False)

    return data[['Text', 'Models'] + metrics + ['T_Score', 'Rnk']]

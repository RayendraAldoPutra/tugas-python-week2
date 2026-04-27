import json

file_path = 'Week_5_6_7_Supervised_Learning_Hands_On_Classification_All_tanpa_tuning (1).ipynb'

with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        
        if "Choclate Quality analysis.csv" in source:
            cell['source'] = [
                "train = pd.read_csv('messi_all_goals.csv')\n",
                "# Membuat target kategorikal 'Target_Home' dari is_home_goal\n",
                "train['Target_Home'] = train['is_home_goal'].astype(int)\n",
                "train.head()"
            ]
            cell['outputs'] = [] # Clear output
            
        elif "sns.countplot(x='Target_Fat'" in source:
            cell['source'] = [
                "# Cek relative size dari kelas target\n",
                "sns.set_style('whitegrid')\n",
                "sns.countplot(x='Target_Home',data=train,palette='RdBu_r')"
            ]
            cell['outputs'] = []
            
        elif "Histogram Moisture" in source:
            cell['source'] = [
                "# Histogram Goal Minute\n",
                "plt.xlabel('Goal Minute')\n",
                "plt.ylabel('Count')\n",
                "plt.title('Histogram Goal Minute')\n",
                "train['goal_minute'].hist(bins=20, color='darkred', alpha=0.7, figsize=(10,6))"
            ]
            cell['outputs'] = []
            
        elif "Drop kolom yang tidak diperlukan untuk klasifikasi" in source:
            cell['source'] = [
                "# Drop kolom yang tidak diperlukan untuk klasifikasi dan lakukan encoding\n",
                "train.drop(['date', 'match_score', 'score_at_goal', 'is_home_goal', 'venue'], axis=1, inplace=True)\n",
                "train = pd.get_dummies(train, drop_first=True, dtype=int)\n",
                "train.head()"
            ]
            cell['outputs'] = []
            
        elif "train_test_split(train.drop('Target_Fat',axis=1)" in source:
            cell['source'] = [
                "from sklearn.model_selection import train_test_split\n",
                "X_train, X_test, y_train, y_test = train_test_split(train.drop('Target_Home',axis=1),\n",
                "                                                    train['Target_Home'], test_size=0.30,\n",
                "                                                    random_state=42)"
            ]
            cell['outputs'] = []

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)

print("Notebook updated successfully.")

# azure_ml_training.py
# XGBoost training pipeline for Jacob Davis's robotics predictive maintenance project
import pandas as pd
from azureml.core import Workspace, Dataset
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

ws = Workspace.from_config()
dataset = Dataset.get_by_name(ws, name='robot_telemetry_dataset')
df = dataset.to_pandas_dataframe()

# Feature engineering
df['vib_rolling_mean'] = df['vibration'].rolling(window=6).mean()
df['temp_rolling_std'] = df['temperature'].rolling(window=6).std()
df['power_efficiency'] = df['current_draw'] / (df['run_hours'] + 1)

X = df[['vib_rolling_mean', 'temp_rolling_std', 'power_efficiency', 'avg_current_draw', 'error_flag']]
y = df['failure_label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = XGBClassifier(scale_pos_weight=10, n_estimators=200, learning_rate=0.1)
model.fit(X_train, y_train)

print(classification_report(y_test, model.predict(X_test)))

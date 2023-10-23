import pandas as pd

df1 = pd.read_csv("/Users/mukh/Desktop/ortho_streamlit/AUC_outputs.csv", index_col=0)
df2 = pd.read_csv("/Users/mukh/Desktop/ortho_streamlit/output_models2.csv", index_col=0)

frames = [df1, df2]

result = pd.concat(frames, axis=1)

result.to_csv("/Users/mukh/Desktop/ortho_streamlit/layer-wise_data.csv")
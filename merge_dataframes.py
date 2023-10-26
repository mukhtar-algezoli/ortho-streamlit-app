import pandas as pd

df1 = pd.read_csv("/Users/mukh/Desktop/ortho_streamlit/layer-wise_data.csv", index_col=0)
df2 = pd.read_csv("/Users/mukh/Desktop/ortho_streamlit/sim_output.csv", index_col=0)

frames = [df1, df2]

result = pd.concat(frames, axis=1)

result.to_csv("/Users/mukh/Desktop/ortho_streamlit/layer-wise_data_new.csv")
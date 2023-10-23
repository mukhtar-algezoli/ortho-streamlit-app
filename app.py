import streamlit as st
import pandas as pd


st.write('# Layer-wise Analysis')

st.write("""To add a line graph press the (+) button and choose the metric and the type of the model. [Collpased On axis] and [Remaining Var axis] only works for the [Orthogonality AUC] metric (does nothing for the others). There is no data for the collapsed metrics of (WavLM, Data2Vec, Wav2Vec2 random) so it shoudl produce an error
         """)

# a selection for the user to specify the number of rows
# num_rows = st.slid('Number of rows', min_value=1, max_value=10)
num_rows = st.number_input("Choose The Number Of Rows",value= 0, step=1, min_value=0, max_value=10)

# columns to lay out the inputs
grid = st.columns([2,1,1,1])

# Function to create a row of widgets (with row number input to assure unique keys)
def add_row(row):
    with grid[0]:
        st.selectbox("Inquiry", ["Empty", "Speaker Accuracy", "Phone Accuracy", "ABX Within original", "ABX Across original", "ABX Within Collapsed", "ABX Across Collapsed", "Orthogonality AUC"],key=f'inquiry{row}')
    with grid[1]:
        st.selectbox("Model", ["Hubert", "Wav2Vec2", "WavLM", "Data2Vec", "Wav2Vec2Rand"], key=f'model{row}')
    with grid[2]:
        st.selectbox('Collpased On axis', ["spk", "ph"], key=f'Xaxis{row}')
    with grid[3]:
         st.selectbox('Remaining Var axis', ["spk", "ph"], key=f'Yaxis{row}')

# Loop to create rows of input widgets
for r in range(num_rows):
    add_row(r)

def read_data() -> pd.DataFrame:
    # df1 = pd.read_csv("/Users/mukh/Desktop/ortho_streamlit/AUC_outputs.csv", index_col=0)
    # df2 = pd.read_csv("/Users/mukh/Desktop/ortho_streamlit/output_models2.csv", index_col=0)
    df = pd.read_csv("./layer-wise_data.csv", index_col=0)
    return df

used_columns = []
for r in range(num_rows):
    if getattr(st.session_state, "inquiry" + str(r)) == "Orthogonality AUC":
        used_columns.append("AUC_" + getattr(st.session_state, "model" + str(r)) + "_" + getattr(st.session_state, "Xaxis" + str(r)) + "_" + getattr(st.session_state, "Yaxis" + str(r)))
    
    elif getattr(st.session_state, "inquiry" + str(r)) == "Speaker Accuracy":
        used_columns.append(getattr(st.session_state, "model" + str(r)) + "_" + "spkAcc")
    
    elif getattr(st.session_state, "inquiry" + str(r)) == "Phone Accuracy":
        used_columns.append(getattr(st.session_state, "model" + str(r)) + "_" + "phAcc")    
    
    elif getattr(st.session_state, "inquiry" + str(r)) == "ABX Within original":
        used_columns.append(getattr(st.session_state, "model" + str(r)) + "_" + "ABXWithin_orig")
    
    elif getattr(st.session_state, "inquiry" + str(r)) == "ABX Across original":
        used_columns.append(getattr(st.session_state, "model" + str(r)) + "_" + "ABXAcross_orig")
    
    elif getattr(st.session_state, "inquiry" + str(r)) == "ABX Within Collapsed":
        used_columns.append(getattr(st.session_state, "model" + str(r)) + "_" + "ABXWithin_coll")
    
    elif getattr(st.session_state, "inquiry" + str(r)) == "ABX Across Collapsed":
        used_columns.append(getattr(st.session_state, "model" + str(r)) + "_" + "ABXAcross_coll")

# st.write(used_columns)
st.line_chart(read_data()[used_columns])


st.write('# Correlation Scatterplots')

st.write("""This part plots the correlation scatter between orthogonality AUC and other metrics. You can only one metric for the X-axis but many could be added to the Y-axis. Same restrictions from above apply to the Y-axis metrics""")

st.write("Xaxis")
cols = st.columns([2,1,1,1])

with cols[0]:
    st.selectbox("Inquiry", ["Empty", "Orthogonality AUC"],key=f'col0')

with cols[1]:
    st.selectbox("Model", ["Hubert", "Wav2Vec2", "WavLM", "Data2Vec", "Wav2Vec2Rand"], key=f"col1")

with cols[2]:
    st.selectbox('Collpased On axis', ["spk", "ph"], key=f'col2')

with cols[3]:
    st.selectbox('Remaining Var axis', ["spk", "ph"], key=f'col3')



st.write("Yaxis")
num_rows2 = st.number_input("Choose The Number Of Rows",value= 0, step=1, min_value=0, max_value=10, key="get_numbs2")

# columns to lay out the inputs
grid = st.columns([2,1,1,1])

# Function to create a row of widgets (with row number input to assure unique keys)
def add_row_scatter(row):
    with grid[0]:
        st.selectbox("Inquiry", ["Empty", "Speaker Accuracy", "Phone Accuracy", "ABX Within original", "ABX Across original", "ABX Within Collapsed", "ABX Across Collapsed", "Orthogonality AUC"],key=f'inquiry0{row}')
    with grid[1]:
        st.selectbox("Model", ["Hubert", "Wav2Vec2", "WavLM", "Data2Vec", "Wav2Vec2Rand"], key=f'model0{row}')
    with grid[2]:
        st.selectbox('Collpased On axis', ["spk", "ph"], key=f'Xaxis0{row}')
    with grid[3]:
         st.selectbox('Remaining Var axis', ["spk", "ph"], key=f'Yaxis0{row}')

# Loop to create rows of input widgets
for r in range(num_rows2):
    add_row_scatter(r)

if st.session_state.col0 == "Orthogonality AUC":
    Xaxis_scatter = "AUC_" + st.session_state.col1 +"_" + st.session_state.col2 + "_" + st.session_state.col3
else:
    Xaxis_scatter = None

scatter_Yaxis = []
for r in range(num_rows2):
    if getattr(st.session_state, "inquiry0" + str(r)) == "Orthogonality AUC":
        scatter_Yaxis.append("AUC_" + getattr(st.session_state, "model0" + str(r)) + "_" + getattr(st.session_state, "Xaxis0" + str(r)) + "_" + getattr(st.session_state, "Yaxis0" + str(r)))
    
    elif getattr(st.session_state, "inquiry0" + str(r)) == "Speaker Accuracy":
        scatter_Yaxis.append(getattr(st.session_state, "model0" + str(r)) + "_" + "spkAcc")
    
    elif getattr(st.session_state, "inquiry0" + str(r)) == "Phone Accuracy":
        scatter_Yaxis.append(getattr(st.session_state, "model0" + str(r)) + "_" + "phAcc")    
    
    elif getattr(st.session_state, "inquiry0" + str(r)) == "ABX Within original":
        scatter_Yaxis.append(getattr(st.session_state, "model0" + str(r)) + "_" + "ABXWithin_orig")
    
    elif getattr(st.session_state, "inquiry0" + str(r)) == "ABX Across original":
        scatter_Yaxis.append(getattr(st.session_state, "model0" + str(r)) + "_" + "ABXAcross_orig")
    
    elif getattr(st.session_state, "inquiry0" + str(r)) == "ABX Within Collapsed":
        scatter_Yaxis.append(getattr(st.session_state, "model0" + str(r)) + "_" + "ABXWithin_coll")
    
    elif getattr(st.session_state, "inquiry0" + str(r)) == "ABX Across Collapsed":
        scatter_Yaxis.append(getattr(st.session_state, "model0" + str(r)) + "_" + "ABXAcross_coll")

st.scatter_chart(
    read_data(),
    x= Xaxis_scatter,
    y= scatter_Yaxis,
    # color='col4',
    # size='col3',
)
# st.line_chart(read_data()[1])
# st.write(read_data()[2])


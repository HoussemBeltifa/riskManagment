import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import base64




st.image("images/risk.png",caption="",width=680)
st.title("Risk managment project")
st.subheader("Created by Mohamed Houssem Beltifa")


with st.sidebar:
    choose = option_menu("Risk managment", ["About", "Graph presentation", "high risk", "Report"],
                         icons=['archive-fill', 'bar-chart', 'activity', 'book'],
                         menu_icon="bootstrap-reboot", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#000000"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#000000"},
    }
    )


logo = Image.open('images/logo.png')
profile = Image.open('images/img.png')
if choose == "About":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the Project</p>', unsafe_allow_html=True)    
    with col2:               # To display brand log
        st.image(logo, width=100 )
    
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image(profile, width=480 )
    st.write("A risk management project that takes a CSV file with potential risks involves analyzing the data and developing a simple visual representation of the key risks. Additionally, a simple word-based description of the risks and the steps taken to mitigate them must be provided. The goal is to ensure stakeholders have a clear understanding of the most important risks and the project team's plan to address them, using data analysis and simple language and visuals.")
    
    
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Upload the risk file</p>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
        df = df.replace({0x82: ''}, regex=True)

        st.set_option('deprecation.showPyplotGlobalUse', False)

        # Create a bar chart of the number of occurrences of each risk category
        st.subheader("Chart 1: Histogram")
        plt.hist(df['Note'])
        plt.xlabel('Note')
        plt.ylabel('Count')
        plt.savefig('chart1.png')
        st.pyplot()
        plt.clf()

        # Create a stacked bar chart of the average score per risk category and probability
        st.subheader("Chart 2: Stacked Bar chart")
        grouped_df = df.groupby(['Probabilite', 'Risques'])['Note'].mean().unstack()
        grouped_df.plot(kind='bar', stacked=True)
        plt.xlabel('Probabilite')
        plt.ylabel('Note')
        plt.legend(title='Risques', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.savefig('chart2.png')
        st.pyplot()
        plt.clf()

        # Create a text file with the dataframe and the charts
        with open('risk_report.txt', 'w') as f:
            f.write(df.to_string())

            # Embed chart1.png in HTML
            with open('chart1.png', 'rb') as img_file:
                img_data = img_file.read()
                encoded_img = base64.b64encode(img_data).decode()
                f.write(f'<img src="data:image/png;base64,{encoded_img}">')

            # Embed chart2.png in HTML
            with open('chart2.png', 'rb') as img_file:
                img_data = img_file.read()
                encoded_img = base64.b64encode(img_data).decode()
                f.write(f'<img src="data:image/png;base64,{encoded_img}">')

        # Create a download link for the text file
        with open('risk_report.txt', 'rb') as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            href = f'<a href="data:file/txt;base64,{b64}" download="risk_report.txt">Download Risk Report</a>'
            st.markdown(href, unsafe_allow_html=True)

    
    
    
elif choose == "Graph presentation":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Graph presentation</p>', unsafe_allow_html=True)
        
    with col2:               
        st.image(logo, width=100 )
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
        df = df.replace({0x82: ''}, regex=True)

        st.set_option('deprecation.showPyplotGlobalUse', False)

        # Create a bar chart of the number of occurrences of each risk category
        st.subheader("Histogram :: Risk and their Notes")
        plt.hist(df['Probabilite'])
        plt.xlabel('Probabilite')
        plt.ylabel('Count')
        plt.savefig('chart1.png')
        st.pyplot()
        plt.clf()

        # Create a stacked bar chart of the average score per risk category and probability
        st.subheader("Stacked Bar chart :: Probability and Notes of all Risques")
        grouped_df = df.groupby(['Probabilite', 'Risques'])['Note'].mean().unstack()
        grouped_df.plot(kind='bar', stacked=True)
        plt.xlabel('Probabilite')
        plt.ylabel('Note')
        plt.legend(title='Risques', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.savefig('chart2.png')
        st.pyplot()
        plt.clf()
    
            

elif choose == "high risk":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Where are the highest rick at</p>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
        df = df.replace({0x82: ''}, regex=True)
        
        # Find the risk with the highest note value
        max_note = df['Note'].max()
        risk_with_max_note = df.loc[df['Note'] == max_note, 'Risques'].iloc[0]

        # Print the risk with the highest note value
        st.write(f"The risk with the highest note is '{risk_with_max_note}' with a note of {max_note}.")
        
        risk_counts = df.nlargest(5, 'Note')['Risques']
        st.write('Top 5 risks with highest note:')
        for risk in risk_counts:
            st.write('- ' + risk)



    
            

elif choose == "Report":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">get your report file</p>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
        df = df.replace({0x82: ''}, regex=True)

        st.set_option('deprecation.showPyplotGlobalUse', False)

        # Create a bar chart of the number of occurrences of each risk category
        #st.subheader("Chart 1: Histogram")
        plt.hist(df['Note'])
        plt.xlabel('Note')
        plt.ylabel('Count')
        plt.savefig('chart1.png')
        #st.pyplot()
        plt.clf()

        # Create a stacked bar chart of the average score per risk category and probability
        #st.subheader("Chart 2: Stacked Bar chart")
        grouped_df = df.groupby(['Probabilite', 'Risques'])['Note'].mean().unstack()
        grouped_df.plot(kind='bar', stacked=True)
        plt.xlabel('Probabilite')
        plt.ylabel('Note')
        plt.legend(title='Risques', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.savefig('chart2.png')
        #st.pyplot()
        plt.clf()

        # Create a text file with the dataframe and the charts
        with open('risk_report.txt', 'w') as f:
            f.write(df.to_string())

            # Embed chart1.png in HTML
            with open('chart1.png', 'rb') as img_file:
                img_data = img_file.read()
                encoded_img = base64.b64encode(img_data).decode()
                f.write(f'<img src="data:image/png;base64,{encoded_img}">')

            # Embed chart2.png in HTML
            with open('chart2.png', 'rb') as img_file:
                img_data = img_file.read()
                encoded_img = base64.b64encode(img_data).decode()
                f.write(f'<img src="data:image/png;base64,{encoded_img}">')

        # Create a download link for the text file
        with open('risk_report.txt', 'rb') as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            href = f'<a href="data:file/txt;base64,{b64}" download="risk_report.txt">Download Risk Report</a>'
            st.markdown(href, unsafe_allow_html=True)



elif choose == "Risk managment":
    st.text("main")




# st.header("Header")
# st.text("test this is a text blog")


# st.markdown("---")
# st.markdown("[Google](https://www.google.com)")
# st.markdown("**Hello** *world*")
# st.markdown("---")

# st.caption("Caption test")
# st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
# st.markdown("---")

# json={"a":"1,2,3","b":"4,5,6"}
# st.json(json)
# st.markdown("---")

# code="""
# print("test print code")
# def funct():
#     return "fonction work well";
# print(funct)"""
# st.code(code,language="python")
# st.markdown("---")

# st.write("## H2")
# st.metric(label="wind speed",value="120ms⁻¹",delta="-1.4ms⁻¹")
# st.markdown("---")

# table = pd.DataFrame({"Colume 1":[1,2,3,4,5,6],
#                       "Colume 2":[7,8,9,10,11,12]})
# st.table(table)
# st.dataframe(table)
# st.markdown("---")

# st.image("o.jpg",caption="Overlord",width=680)
# st.video("video.mp4")
# st.markdown("---")


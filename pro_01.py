import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Configurar el título de la aplicación
st.title('Manipulación y Análisis de Datos')

# Cargar archivo CSV
st.sidebar.header('Subir archivo CSV')
uploaded_file = st.sidebar.file_uploader("Elige un archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Mostrar el DataFrame cargado
    st.subheader('DataFrame')
    st.write(df)
    
    # Mostrar estadísticas descriptivas
    st.subheader('Estadísticas Descriptivas')
    st.write(df.describe())
    
    # Mostrar matriz de correlación
    st.subheader('Matriz de Correlación')
    corr_matrix = df.corr()
    st.write(corr_matrix)
    fig = px.imshow(corr_matrix, text_auto=True, aspect="auto", title='Matriz de Correlación')
    st.plotly_chart(fig)
    
    # Selección de columnas
    st.sidebar.subheader('Selección de Columnas')
    all_columns = df.columns.tolist()
    selected_columns = st.sidebar.multiselect('Selecciona las columnas', all_columns, all_columns)
    
    if selected_columns:
        df_selected = df[selected_columns]
        
        # Mostrar DataFrame con las columnas seleccionadas
        st.subheader('DataFrame con Columnas Seleccionadas')
        st.write(df_selected)
        
        # Operaciones de análisis de datos
        st.sidebar.subheader('Operaciones de Análisis de Datos')
        
        # Calcular media de una columna
        col_mean = st.sidebar.selectbox('Calcular Media de la Columna', selected_columns)
        if col_mean:
            mean_value = df_selected[col_mean].mean()
            st.write(f'Media de {col_mean}: {mean_value}')
        
        # Filtrar filas por valor de columna
        filter_column = st.sidebar.selectbox('Filtrar Filas por Valor de Columna', selected_columns)
        if filter_column:
            unique_values = df_selected[filter_column].unique()
            filter_value = st.sidebar.selectbox('Selecciona un valor para filtrar', unique_values)
            df_filtered = df_selected[df_selected[filter_column] == filter_value]
            
            st.subheader('DataFrame Filtrado')
            st.write(df_filtered)
        
        # Gráficos
        st.sidebar.subheader('Visualización de Datos')
        
        # Histograma
        hist_column = st.sidebar.selectbox('Selecciona la columna para Histograma', selected_columns)
        if hist_column:
            st.subheader(f'Histograma de {hist_column}')
            fig = px.histogram(df_selected, x=hist_column, nbins=30, title=f'Histograma de {hist_column}')
            st.plotly_chart(fig)
        
        # Diagrama de Dispersión
        scatter_x = st.sidebar.selectbox('Selecciona columna X para Diagrama de Dispersión', selected_columns)
        scatter_y = st.sidebar.selectbox('Selecciona columna Y para Diagrama de Dispersión', selected_columns)
        if scatter_x and scatter_y:
            st.subheader(f'Diagrama de Dispersión de {scatter_x} vs {scatter_y}')
            fig = px.scatter(df_selected, x=scatter_x, y=scatter_y, title=f'Diagrama de Dispersión de {scatter_x} vs {scatter_y}')
            st.plotly_chart(fig)
        
        # Diagrama de Caja
        box_column = st.sidebar.selectbox('Selecciona la columna para Diagrama de Caja', selected_columns)
        if box_column:
            st.subheader(f'Diagrama de Caja de {box_column}')
            fig = px.box(df_selected, y=box_column, title=f'Diagrama de Caja de {box_column}')
            st.plotly_chart(fig)
        
        # Operaciones Matemáticas
        st.sidebar.subheader('Operaciones Matemáticas')
        math_column = st.sidebar.selectbox('Selecciona la columna para Operaciones Matemáticas', selected_columns)
        operation = st.sidebar.selectbox('Selecciona la Operación', ['Suma', 'Resta', 'Multiplicación', 'División'])
        value = st.sidebar.number_input('Introduce el valor para la operación', value=1)
        
        if math_column and operation:
            if operation == 'Suma':
                df_selected[math_column + '_sum'] = df_selected[math_column] + value
            elif operation == 'Resta':
                df_selected[math_column + '_sub'] = df_selected[math_column] - value
            elif operation == 'Multiplicación':
                df_selected[math_column + '_mul'] = df_selected[math_column] * value
            elif operation == 'División':
                df_selected[math_column + '_div'] = df_selected[math_column] / value
            
            st.subheader(f'DataFrame con Operación {operation} aplicada a {math_column}')
            st.write(df_selected)

else:
    st.write("Por favor, sube un archivo CSV para comenzar.")

# Inicia la aplicación con: streamlit run nombre_del_archivo.py

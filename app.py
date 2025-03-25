import streamlit as st
import joblib
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

dt = joblib.load(open('model_joblib', 'rb'))

def main(title = 'Clasificador de Bandas según Productividad'.upper()):
    st.markdown("<h1 style='text-align: center; font-size: 25px; color: blue;'>{}</h1>".format(title), unsafe_allow_html=True)
    st.image('rabbit.jpeg', width=100)
    info = ''
    
    with st.expander("Introduce los parametros de la banda"):
        fertilidad = st.number_input('introduce fertilidad en %')    
        igualados = st.number_input('introduce nº igualados')
        mort_dest = st.number_input('introduce mortalidad al destete en %')
        qt_dest = st.number_input('introduce número de destetados')
        pes_dest = st.number_input('introduce peso al destete en kg')
        
        if st.button('Predecir'):
            prediction = dt.predict([[fertilidad, igualados, mort_dest, qt_dest, pes_dest]])
            
            if prediction == 0:
                info = 'Banda Normal'
            elif prediction == 1:
                info = 'Banda Buena'
            else:
                info = 'Banda Mala'
            st.success('Predicción: {}'.format(info))

if __name__ == "__main__":
    main()
        
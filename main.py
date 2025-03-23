import streamlit as st

st.set_page_config(page_title="Calculadora Regla 40%", layout="wide")
st.title("📈 Calculadora Regla del 40% para Tech Companies")

tab1, tab2 = st.tabs(["💰 Para Productos/SaaS", "👨💻 Para Servicios"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        crecimiento = st.number_input("Tasa crecimiento anual (%)", min_value=0.0, max_value=200.0, step=5.0)
        margen = st.number_input("Margen de beneficio (%)", min_value=-100.0, max_value=100.0, step=5.0)
    
    total = crecimiento + margen
    resultado = "✅ Cumple regla" if total >= 40 else "❌ Incumple regla"
    color = "green" if total >= 40 else "red"
    
    with col2:
        st.metric("Resultado SaaS/Productos", 
                f"{total:.1f}% / 40%", 
                resultado,
                delta_color="off")

with tab2:
    col3, col4 = st.columns(2)
    with col3:
        salario_anual = st.number_input("Salario bruto anual (€)", min_value=30000, max_value=100000, step=5000, value=50000)
        costes_variables = st.number_input("Costes variables anuales (€)", min_value=0, max_value=100000, step=5000)
        horas_facturadas = st.number_input("Horas facturables/año", min_value=100, max_value=2000, value=1320)
    
    margen_contribucion = salario_anual - costes_variables
    porcentaje_margen = (margen_contribucion / salario_anual) * 100
    tarifa_hora = salario_anual / ((1 - 0.4) * horas_facturadas)
    
    with col4:
        st.metric("Margen de contribución", 
                f"{porcentaje_margen:.1f}%", 
                "✅ Sano" if porcentaje_margen >= 40 else "⚠️ Peligro",
                delta_color="off")
        st.metric("Tarifa hora mínima", 
                f"{tarifa_hora:.2f}€/h", 
                "Ley de Ramos")

with st.expander("📚 Explicación Fórmulas"):
    st.markdown("""
    **Para Productos (SaaS/Startups):**
    ```
    Regla 40% = Crecimiento (%) + Margen Beneficio (%) ≥ 40
    ```
    
    **Para Servicios (Consultoría):**
    ```
    Margen Contribución = Salario Bruto - Costes Variables
    % Margen = (Margen Contribución / Salario Bruto) × 100 ≥ 40%
    Tarifa Hora = Salario Bruto / [(1 - 0.4) × Horas Facturables]
    ```
    """)

with st.expander("📈 Ejemplo RTVE (Licitação pública)"):
    st.table({
        "Concepto": ["Salario consultor", "Costes variables", "Margen contribución", "% Margen", "Tarifa hora"],
        "Valor": ["54.500€", "19.000€", "35.500€", "65,14%", "60€/h"]
    })

# Calculadora Regla 40% para Tech Companies

Una aplicación web interactiva que ayuda a calcular y evaluar la salud financiera de empresas de tecnología utilizando la Regla del 40% y otras métricas importantes.

## 🎯 ¿Qué es la Regla del 40%?

La Regla del 40% es una métrica clave en el sector tecnológico que combina el crecimiento y la rentabilidad. Una empresa cumple con la regla cuando la suma de su tasa de crecimiento anual y su margen de beneficio es igual o superior al 40%.

## ✨ Características

La aplicación incluye dos calculadoras principales:

### 1. Calculadora para Productos/SaaS
- Evalúa el cumplimiento de la Regla del 40%
- Calcula la combinación de crecimiento y margen de beneficio
- Muestra indicadores visuales del estado de la empresa

### 2. Calculadora para Servicios
- Calcula el margen de contribución
- Determina la tarifa hora mínima recomendada
- Incluye variables como salario bruto, costes variables y horas facturables

## 🚀 Cómo usar la aplicación

1. Selecciona la pestaña correspondiente según tu tipo de negocio (Productos/SaaS o Servicios)
2. Introduce los valores solicitados en los campos de entrada
3. Los resultados se actualizarán automáticamente
4. Consulta la sección de explicación de fórmulas para más detalles

## 🛠️ Tecnologías utilizadas

- Python
- Streamlit
- HTML/CSS

## 📊 Fórmulas principales

### Para Productos/SaaS
```
Regla 40% = Crecimiento (%) + Margen Beneficio (%) ≥ 40
```

### Para Servicios
```
Margen Contribución = Salario Bruto - Costes Variables
% Margen = (Margen Contribución / Salario Bruto) × 100 ≥ 40%
Tarifa Hora = Salario Bruto / [(1 - 0.4) × Horas Facturables]
```

## 🚀 Instalación y ejecución

1. Clona el repositorio
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```
3. Ejecuta la aplicación:
```bash
streamlit run main.py
```

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

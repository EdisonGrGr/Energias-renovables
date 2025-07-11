from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Cargar datos una sola vez
file_path = "DER/data/complete_renewable_energy_dataset.csv"
df = pd.read_csv(file_path)

@app.route('/')
def index():
    countries = sorted(df['Country'].dropna().unique())
    years = sorted(df['Year'].dropna().unique())
    energy_types = sorted(df['Energy Type'].dropna().unique())
    metrics = [col for col in df.columns if col not in ['Country', 'Year', 'Energy Type']]

    return render_template('index.html',
                           countries=countries,
                           years=years,
                           energy_types=energy_types,
                           metrics=metrics)

@app.route('/get_data', methods=['POST'])
def get_data():
    try:
        data = request.get_json()
        country = data.get('country')
        year = int(data.get('year'))
        energy = data.get('energy')
        metrics = data.get('metrics')

        # Filtrar DataFrame por país, año y tipo de energía
        filtered = df[
            (df['Country'] == country) &
            (df['Year'] == year) &
            (df['Energy Type'] == energy)
        ]

        if filtered.empty:
            print(f"⚠️ No hay datos para {country} - {year} - {energy}")
            return jsonify({'metrics': metrics, 'values': [0] * len(metrics)})

        values = []
        for metric in metrics:
            try:
                if metric not in filtered.columns:
                    raise ValueError(f"Columna '{metric}' no existe")
                val = filtered[metric].values[0]
                if pd.isna(val):
                    val = 0
                values.append(val)
            except Exception as e:
                print(f"❌ Error al procesar la métrica '{metric}': {e}")
                values.append(0)

        return jsonify({'metrics': metrics, 'values': values})

    except Exception as e:
        print(f"❌ Error general en /get_data: {e}")
        return jsonify({'error': 'Error interno del servidor'}), 500

if __name__ == '__main__':
    app.run(debug=True)
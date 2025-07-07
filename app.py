from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    articolo = request.json.get('articolo')
    listino_path = os.path.join(app.root_path, 'templates', 'LISTINO.csv')
    try:
        df = pd.read_csv(listino_path, delimiter=';|,', engine='python')
        df.columns = [c.strip().upper() for c in df.columns]
        row = df[df['ARTICOLO'].astype(str).str.lower() == str(articolo).lower()]
        if not row.empty:
            price = row.iloc[0]['LIST PRICE']
            price_str = str(price).replace('€','').replace(',','.').strip()
            return jsonify({'success': True, 'price': float(price_str)})
        else:
            return jsonify({'success': False})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)







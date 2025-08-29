from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Liste des fichiers SVG stockés dans le dossier static
    graph_files = [
        'disk_usage_chart.svg',
        'ram_usage_chart.svg',
        'active_users_chart.svg',
        'combined_usage_chart.svg'
    ]
    return render_template('index.html', graph_files=graph_files)

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000, debug=True)

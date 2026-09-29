from flask import Flask, jsonify, request
from app import create_app
from app.core.extensions import socketio

app = create_app()

# --- TAMBAHKAN KODE UJI COBA DI SINI ---
@app.route('/api/test', methods=['GET'])
def test_api():
    # Ini adalah data mentah yang ingin kita kirim ke Power Apps nanti
    data_untuk_dikirim = {
        "status": "berhasil",
        "pesan": "Halo! Ini adalah data dari Flask API.",
        "angka_percobaan": 100
    }
    
    return jsonify(data_untuk_dikirim)
# ---------------------------------------

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
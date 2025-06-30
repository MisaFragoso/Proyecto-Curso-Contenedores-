from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
DB_CONFIG = {
    'host': os.getenv('DATABASE_HOST', 'database'),
    'user': os.getenv('DATABASE_USER', 'distributec'),
    'password': os.getenv('DATABASE_PASSWORD', 'distributec123'),
    'database': os.getenv('DATABASE_NAME', 'inventario')
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/api/productos', methods=['GET'])
def get_productos():
    try:
        categoria = request.args.get('categoria')
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        if categoria:
            cursor.execute("SELECT * FROM productos WHERE categoria = %s", (categoria,))
        else:
            cursor.execute("SELECT * FROM productos")
        
        productos = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return jsonify(productos)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/productos/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos WHERE id = %s", (producto_id,))
        producto = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if producto:
            return jsonify(producto)
        return jsonify({'error': 'Producto no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/productos', methods=['POST'])
def create_producto():
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """INSERT INTO productos (nombre, categoria, precio, stock, descripcion) 
                   VALUES (%s, %s, %s, %s, %s)"""
        values = (data['nombre'], data['categoria'], data['precio'], data['stock'], data.get('descripcion', ''))
        
        cursor.execute(query, values)
        conn.commit()
        producto_id = cursor.lastrowid
        cursor.close()
        conn.close()
        
        return jsonify({'id': producto_id, 'message': 'Producto creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/productos/<int:producto_id>', methods=['PUT'])
def update_producto(producto_id):
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """UPDATE productos SET nombre=%s, categoria=%s, precio=%s, stock=%s, descripcion=%s 
                   WHERE id=%s"""
        values = (data['nombre'], data['categoria'], data['precio'], data['stock'], data.get('descripcion', ''), producto_id)
        
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({'message': 'Producto actualizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/estadisticas', methods=['GET'])
def get_estadisticas():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Total de productos
        cursor.execute("SELECT COUNT(*) as total_productos FROM productos")
        total_productos = cursor.fetchone()['total_productos']
        
        # Productos con stock bajo (menos de 10)
        cursor.execute("SELECT COUNT(*) as stock_bajo FROM productos WHERE stock < 10")
        stock_bajo = cursor.fetchone()['stock_bajo']
        
        # Productos por categoría
        cursor.execute("SELECT categoria, COUNT(*) as cantidad FROM productos GROUP BY categoria")
        por_categoria = cursor.fetchall()
        
        # Valor total del inventario
        cursor.execute("SELECT SUM(precio * stock) as valor_total FROM productos")
        valor_total = cursor.fetchone()['valor_total'] or 0
        
        cursor.close()
        conn.close()
        
        return jsonify({
            'total_productos': total_productos,
            'productos_stock_bajo': stock_bajo,
            'productos_por_categoria': por_categoria,
            'valor_total_inventario': float(valor_total)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/categorias', methods=['GET'])
def get_categorias():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT categoria FROM productos ORDER BY categoria")
        categorias = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        
        return jsonify(categorias)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

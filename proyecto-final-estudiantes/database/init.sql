-- Crear la tabla de productos
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    descripcion TEXT,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insertar datos de prueba
INSERT INTO productos (nombre, categoria, precio, stock, descripcion) VALUES
('MacBook Pro 14"', 'Laptops', 24999.00, 15, 'Laptop profesional con chip M2 Pro'),
('iPhone 15 Pro', 'Smartphones', 19999.00, 25, 'Smartphone con cámara profesional'),
('iPad Air', 'Tablets', 12999.00, 20, 'Tablet para trabajo y entretenimiento'),
('Samsung Galaxy S24', 'Smartphones', 15999.00, 18, 'Smartphone Android premium'),
('Dell XPS 13', 'Laptops', 18999.00, 12, 'Laptop ultradelgada para profesionales'),
('Surface Pro 9', 'Tablets', 16999.00, 8, 'Tablet 2 en 1 de Microsoft'),
('AirPods Pro', 'Accesorios', 4999.00, 30, 'Audífonos inalámbricos con cancelación de ruido'),
('Magic Mouse', 'Accesorios', 1999.00, 22, 'Mouse inalámbrico de Apple'),
('Logitech MX Master', 'Accesorios', 1599.00, 35, 'Mouse ergonómico para productividad'),
('Monitor LG 27"', 'Monitores', 8999.00, 10, 'Monitor 4K para profesionales'),
('Teclado Mecánico', 'Accesorios', 2999.00, 40, 'Teclado mecánico RGB'),
('Webcam HD', 'Accesorios', 899.00, 50, 'Cámara web 1080p para videoconferencias');

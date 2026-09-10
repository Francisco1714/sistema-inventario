class TestListarProductos:
    def test_listar_vacio(self, client):
        response = client.get('/api/v1/productos')
        data = response.get_json()

        assert response.status_code == 200
        assert data['success'] is True
        assert data['data'] == []
        assert data['pagination']['total'] == 0

    def test_listar_con_datos(self, client, sample_product):
        response = client.get('/api/v1/productos')
        data = response.get_json()

        assert response.status_code == 200
        assert len(data['data']) == 1
        assert data['data'][0]['nombre'] == 'Laptop Test'

    def test_paginacion(self, client):
        for i in range(15):
            client.post('/api/v1/productos', json={
                'nombre': f'Producto {i}',
                'precio': 10.0,
                'stock': 1
            })

        response = client.get('/api/v1/productos?page=1&per_page=12')
        data = response.get_json()

        assert len(data['data']) == 12
        assert data['pagination']['total'] == 15
        assert data['pagination']['pages'] == 2


class TestObtenerProducto:
    def test_obtener_existente(self, client, sample_product):
        response = client.get(f'/api/v1/productos/{sample_product.id}')
        data = response.get_json()

        assert response.status_code == 200
        assert data['success'] is True
        assert data['data']['nombre'] == 'Laptop Test'

    def test_obtener_no_existente(self, client):
        response = client.get('/api/v1/productos/999')
        data = response.get_json()

        assert response.status_code == 404
        assert data['success'] is False


class TestCrearProducto:
    def test_crear_valido(self, client):
        response = client.post('/api/v1/productos', json={
            'nombre': 'Mouse Gaming',
            'descripcion': 'Mouse RGB',
            'precio': 49.99,
            'stock': 25
        })
        data = response.get_json()

        assert response.status_code == 201
        assert data['success'] is True
        assert data['data']['nombre'] == 'Mouse Gaming'
        assert float(data['data']['precio']) == 49.99

    def test_crear_sin_nombre(self, client):
        response = client.post('/api/v1/productos', json={
            'precio': 49.99,
            'stock': 25
        })
        data = response.get_json()

        assert response.status_code == 400
        assert data['success'] is False

    def test_crear_precio_cero(self, client):
        response = client.post('/api/v1/productos', json={
            'nombre': 'Test',
            'precio': 0,
            'stock': 1
        })
        data = response.get_json()

        assert response.status_code == 400
        assert data['success'] is False

    def test_crear_stock_negativo(self, client):
        response = client.post('/api/v1/productos', json={
            'nombre': 'Test',
            'precio': 10.0,
            'stock': -1
        })
        data = response.get_json()

        assert response.status_code == 400
        assert data['success'] is False


class TestActualizarProducto:
    def test_put_existente(self, client, sample_product):
        response = client.put(f'/api/v1/productos/{sample_product.id}', json={
            'nombre': 'Laptop Actualizada',
            'descripcion': 'Nueva desc',
            'precio': 1299.99,
            'stock': 15
        })
        data = response.get_json()

        assert response.status_code == 200
        assert data['success'] is True
        assert data['data']['nombre'] == 'Laptop Actualizada'
        assert float(data['data']['precio']) == 1299.99

    def test_put_no_existente(self, client):
        response = client.put('/api/v1/productos/999', json={
            'nombre': 'Test',
            'precio': 10.0,
            'stock': 1
        })
        data = response.get_json()

        assert response.status_code == 404
        assert data['success'] is False

    def test_put_datos_invalidos(self, client, sample_product):
        response = client.put(f'/api/v1/productos/{sample_product.id}', json={
            'nombre': '',
            'precio': 10.0,
            'stock': 1
        })
        data = response.get_json()

        assert response.status_code == 400
        assert data['success'] is False


class TestPatchProducto:
    def test_patch_parcial(self, client, sample_product):
        response = client.patch(f'/api/v1/productos/{sample_product.id}', json={
            'precio': 799.99
        })
        data = response.get_json()

        assert response.status_code == 200
        assert data['data']['nombre'] == 'Laptop Test'
        assert float(data['data']['precio']) == 799.99

    def test_patch_no_existente(self, client):
        response = client.patch('/api/v1/productos/999', json={
            'nombre': 'Test'
        })
        data = response.get_json()

        assert response.status_code == 404
        assert data['success'] is False

    def test_patch_nombre_vacio(self, client, sample_product):
        response = client.patch(f'/api/v1/productos/{sample_product.id}', json={
            'nombre': ''
        })
        data = response.get_json()

        assert response.status_code == 400
        assert data['success'] is False


class TestEliminarProducto:
    def test_eliminar_existente(self, client, sample_product):
        response = client.delete(f'/api/v1/productos/{sample_product.id}')
        data = response.get_json()

        assert response.status_code == 200
        assert data['success'] is True

        response = client.get(f'/api/v1/productos/{sample_product.id}')
        assert response.status_code == 404

    def test_eliminar_no_existente(self, client):
        response = client.delete('/api/v1/productos/999')
        data = response.get_json()

        assert response.status_code == 404
        assert data['success'] is False

from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

# Pruebas unitarias para el modelo Laboratorio
class LaboratorioTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Configuración inicial de datos
        cls.laboratorio = Laboratorio.objects.create(
            nombre='Laboratorio Chile',
            ciudad='Talca',
            pais='Chile'
        )
    
    def test_model_content(self):
        
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, 'Laboratorio Chile')
        self.assertEqual(laboratorio.ciudad, 'Talca')
        self.assertEqual(laboratorio.pais, 'Chile')
        print("Test 'test_model_content': Los datos del modelo coinciden correctamente.")

    def test_url_respuesta_codigo_200(self):
        # Verificar que la URL devuelve un HTTP 200
        response = self.client.get(reverse('editar_laboratorio', args=[self.laboratorio.id]))
        self.assertEqual(response.status_code, 200)
        print("Test 'test_url_responde_200': La URL devolvió un código HTTP 200 exitosamente.")

    def test_template_correcto_OK(self):
        # Verificar que se usa la plantilla correcta y contiene contenido esperado
        response = self.client.get(reverse('editar_laboratorio', args=[self.laboratorio.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_laboratorio.html')
        self.assertContains(response, '<h2 class="text-center">Editar Laboratorio</h2>')
        print("Test 'test_template_correcto': La plantilla usada y el contenido HTML son correctos.")


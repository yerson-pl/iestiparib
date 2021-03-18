from django.db import models

# Create your models here.


def upload_location(instance, filename):
    return "postulantes/%s/%s" % (instance.correo, filename)

class Postulante(models.Model):
    """Model definition for Postulante."""
    
    CARRERA_CHOICES=[ 
        ('CC', 'Contrucción Civil'),
        ('C' , 'Contabilidad'),
        ('EM', 'Explotación Minera'),
    ]
    
  
    
    GENERO_CHOICES=[
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        
    ]

    # TODO: Define fields here
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    dni_num = models.IntegerField('N° DNI')
    ap_paterno = models.CharField('Apellido Paterno',max_length=100)
    ap_materno = models.CharField('Apellido Materno',max_length=100)
    nombre = models.CharField('Nombres', max_length=150)
    sexo = models.CharField('Sexo', max_length=2,choices=GENERO_CHOICES)
    fecha_nac = models.DateField('Fecha de Nacimiento (dd/MM/AAAA)')
    departamento = models.CharField('Departamento',max_length=80)
    provincia = models.CharField('Provincia',max_length=100)
    distrito = models.CharField('Distrito',max_length=150)
    direccion = models.CharField('Dirección',max_length=200)
    correo = models.EmailField('Correo', max_length=254, unique=True)
    inst_procedencia = models.CharField('Colegio de Procedencia',max_length=150)
    egreso = models.IntegerField('Año de egreso')
    celular = models.IntegerField('N° Celular')
    carrera = models.CharField('Programa de Estudios al que postula',max_length=2,choices=CARRERA_CHOICES)
    foto = models.FileField('Foto',upload_to=upload_location, blank=False, null=False)
    dni = models.FileField('Foto DNI', upload_to=upload_location, blank=False, null=False)
    certificado = models.FileField('Certificado de Estudios', upload_to=upload_location, blank=False, null=False)
    num_operacion = models.IntegerField('N° Operación Voucher', unique=True)
    voucher = models.FileField('Voucher', upload_to=upload_location, blank=False, null=False)


    class Meta:
        """Meta definition for Postulante."""

        verbose_name = 'Postulante'
        verbose_name_plural = 'Postulantes'

    def __str__(self):
        """Unicode representation of Postulante."""
        return self.nombre
from import_export import resources
from .models import ProgramaCurricular

class ProgramaCurricularResource(resources.ModelResource):
    class Meta:
        model = ProgramaCurricular

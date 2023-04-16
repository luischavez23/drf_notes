from rest_framework import routers
from .api import NotesViewSets

router = routers.DefaultRouter()

router.register('api/notes', NotesViewSets, 'notes')

urlpatterns = router.urls

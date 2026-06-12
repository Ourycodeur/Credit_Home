## Créons nos tables dans la base de données
from api.database import engine
from db.models import Base
Base.metadata.create_all(bind=engine)

print("Tables créées avec succès dans la base de données.")
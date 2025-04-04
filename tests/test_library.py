import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] =True
    with app.test_client() as client:
        yield client
        
def test_create_library(client):
    """
    Test creation Library
    """
    response = client.post("/library", json={"name": "HES Arc Library"})
    assert response.status_code ==201
    
def test_get_library(client):
    """Teste si on peut récupérer une bibliothèque existante."""
    # Créer une bibliothèque d'abord
    response = client.post("/library", json={"name": "Ma Bibliothèque"})
    assert response.status_code == 201  # Vérifie que la création a réussi

    library_id = response.json["id"]  # Récupérer l'ID de la bibliothèque créée

    # Récupérer la bibliothèque avec GET
    response = client.get(f"/library/{library_id}")
    assert response.status_code == 200  # Vérifie que la bibliothèque existe
    assert response.json["name"] == "Ma Bibliothèque"  # Vérifie les données
    
def test_update_library(client):
    """Teste si on peut modifier une bibliothèque existante."""
    response = client.post("/library", json={"name": "Ancienne Bibliothèque"})
    assert response.status_code == 201

    library_id = response.json["id"]

    # Mise à jour de la bibliothèque
    response = client.put(f"/library/{library_id}", json={"name": "Nouvelle Bibliothèque"})
    assert response.status_code == 200
    assert response.json["name"] == "Nouvelle Bibliothèque"
    
def test_delete_library(client):
    """Teste si on peut supprimer une bibliothèque."""
    response = client.post("/library", json={"name": "Temporaire"})
    assert response.status_code == 201

    library_id = response.json["id"]

    # Supprimer la bibliothèque
    response = client.delete(f"/library/{library_id}")
    assert response.status_code == 204  # 204 signifie suppression réussie

    # Vérifier que la bibliothèque n'existe plus
    response = client.get(f"/library/{library_id}")
    assert response.status_code == 404
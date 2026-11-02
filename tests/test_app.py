import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_health_disponible(client):
    reponse = client.get("/health")
    assert reponse.status_code == 200
    assert reponse.get_json() == {"status": "ok"}


def test_tickets_renvoie_la_liste(client):
    reponse = client.get("/tickets")
    assert reponse.status_code == 200
    donnees = reponse.get_json()
    assert isinstance(donnees, list)
    assert len(donnees) == 3
    for ticket in donnees:
        assert {"id", "titre", "statut"} <= ticket.keys()


def test_route_inexistante_renvoie_404(client):
    reponse = client.get("/nimportequoi")
    assert reponse.status_code == 404


def test_version_lit_la_variable_denvironnement(client, monkeypatch):
    monkeypatch.setenv("APP_VERSION", "abc1234")
    reponse = client.get("/version")
    assert reponse.status_code == 200
    assert reponse.get_json() == {"version": "abc1234"}
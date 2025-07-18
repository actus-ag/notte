import pytest
from notte_sdk import NotteClient


def test_start_close_session():
    client = NotteClient()

    response = client.sessions.start()
    assert response.status == "active"
    response = client.sessions.stop(session_id=response.session_id)
    assert response.status == "closed"


def test_start_close_session_factory():
    client = NotteClient()
    with client.Session(proxies=False) as session:
        assert session.session_id is not None
        status = session.status()
        assert status.status == "active"
    assert session.response is not None
    assert session.response.status == "closed"


def test_start_close_session_with_proxy():
    client = NotteClient()
    with client.Session(proxies=True) as session:
        assert session.session_id is not None
        status = session.status()
        assert status.status == "active"
    assert session.response is not None


def test_start_close_session_with_viewport():
    client = NotteClient()
    with client.Session(viewport_height=100, viewport_width=100) as session:
        assert session.session_id is not None
        status = session.status()
        assert status.status == "active"
    assert session.response is not None


@pytest.fixture
def session_id() -> str:
    return "ee72bb85-8c16-4fd1-9e0e-e4228b08a209"


def test_replay_session(session_id: str):
    client = NotteClient()
    response = client.sessions.replay(session_id=session_id)
    assert len(response.replay) > 0


def test_replay_session_with_frame(session_id: str):
    client = NotteClient()
    response = client.sessions.replay(session_id=session_id)
    assert len(response.replay) > 0
    first_frame = response.frame(frame_idx=0)
    assert first_frame is not None
    last_frame = response.frame(frame_idx=-1)
    assert last_frame is not None
    assert first_frame != last_frame

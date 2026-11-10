import pytest
import logging

logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def session_resource():
    logger.info("[SESSION] Подготовка ресурса (начало сессии)")
    resource = {"id": 999, "name": "session_resource", "connected": True}
    yield resource
    logger.info("[SESSION] Очистка ресурса (конец сессии)")
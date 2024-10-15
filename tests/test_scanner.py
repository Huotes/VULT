from vult.scanner import NetworkScanner
from unittest.mock import MagicMock

def test_scan():
    # Criar uma configuração de teste
    config = MagicMock()
    config.target = '192.168.1.1'
    config.ports = '80'

    # Criar um logger falso
    logger = MagicMock()

    # Inicializar o scanner com a configuração de teste
    scanner = NetworkScanner(config, logger)

    # Mock do resultado da varredura
    scanner.nm.scan = MagicMock(return_value={'scan': 'resultado_falso'})

    # Rodar o scan e verificar o resultado
    result = scanner.scan()
    assert result == 'resultado_falso'

import nmap

class NetworkScanner:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.nm = nmap.PortScanner()

    def scan(self):
        self.logger.info(f"Iniciando varredura em {self.config.target} nas portas {self.config.ports}")
        self.nm.scan(self.config.target, self.config.ports)
        scan_results = self.nm.csv()
        self.logger.debug(f"Resultados da varredura: {scan_results}")
        return scan_results

import json

class Reporter:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def generate_report(self, vulnerabilities):
        self.logger.info(f"Gerando relatório em {self.config.output}")
        with open(self.config.output, 'w') as f:
            json.dump(vulnerabilities, f, indent=4)
        self.logger.info("Relatório gerado com sucesso.")

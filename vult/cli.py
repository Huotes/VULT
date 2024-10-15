# vult/cli.py
import argparse
from .scanner import NetworkScanner
from .packet_creator import PacketCreator
from .vulnerability_analyzer import VulnerabilityAnalyzer
from .reporter import Reporter
from .config import Config
from .logger import setup_logger

def main():
    parser = argparse.ArgumentParser(description='Vult - Scanner de Vulnerabilidades Automatizado')
    parser.add_argument('-t', '--target', required=True, help='Alvo do escaneamento (IP ou faixa de IP)')
    parser.add_argument('-p', '--ports', default='1-1024', help='Portas a serem escaneadas (padrão: 1-1024)')
    parser.add_argument('-o', '--output', default='report.json', help='Arquivo de saída do relatório')
    args = parser.parse_args()

    config = Config(target=args.target, ports=args.ports, output=args.output)
    logger = setup_logger()

    scanner = NetworkScanner(config, logger)
    scan_results = scanner.scan()

    packet_creator = PacketCreator(config, logger)
    packet_results = packet_creator.create_and_send_packets(scan_results)

    analyzer = VulnerabilityAnalyzer(logger)
    vulnerabilities = analyzer.analyze(scan_results, packet_results)

    reporter = Reporter(config, logger)
    reporter.generate_report(vulnerabilities)

if __name__ == '__main__':
    main()

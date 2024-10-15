from scapy.all import IP, TCP, sr1

class PacketCreator:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def create_and_send_packets(self, scan_results):
        results = []
        for host in scan_results['hosts']:
            for port in host['ports']:
                pkt = IP(dst=host['ip'])/TCP(dport=port, flags='S')
                self.logger.debug(f"Enviando pacote para {host['ip']}:{port}")
                response = sr1(pkt, timeout=1, verbose=0)
                if response:
                    results.append({'ip': host['ip'], 'port': port, 'response': response.summary()})
        return results

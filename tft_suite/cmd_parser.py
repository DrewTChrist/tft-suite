""" This module will hold callable classes used to 
    aid in parsing commands for screens.
"""

class IwlistParser:
    """Parses information from iwlist"""
    
    def __call__(self, iwlist: str) -> list:
        lines: list[str] = iwlist.split('\n')
        networks: list[dict] = []
        for i in range(len(lines)):
            if 'Cell' in lines[i]:
                n: dict = {
                    'Address': lines[i].strip(),
                    'Channel': lines[i+1].strip(),
                    'Frequency': lines[i+2].strip(),
                    'Quality': lines[i+3].strip(),
                    'Encryption key': lines[i+4].strip().split(':')[1],
                    'ESSID': lines[i+5].strip().split(':')[1],
                }
                networks.append(n)
        return networks
    
iwlist_parser: IwlistParser = IwlistParser()

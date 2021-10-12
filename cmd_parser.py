class IwlistParser:
    
    def __call__(self, iwlist):
        lines = iwlist.split('\n')
        networks = []
        for i in range(len(lines)):
            if 'Cell' in lines[i]:
                n = {
                    'Address': lines[i].strip(),
                    'Channel': lines[i+1].strip(),
                    'Frequency': lines[i+2].strip(),
                    'Quality': lines[i+3].strip(),
                    'Encryption key': lines[i+4].strip().split(':')[1],
                    'ESSID': lines[i+5].strip().split(':')[1],
                }
                networks.append(n)
        return networks
    
iwlist_parser = IwlistParser()

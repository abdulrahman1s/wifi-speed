import requests
import ssl

class TLSAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl._create_unverified_context()
        ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
        kwargs['ssl_context'] = ctx
        return super(TLSAdapter, self).init_poolmanager(*args, **kwargs)


def fetch_client():
    fetch = requests.session()
    fetch.verify = False
    fetch.mount('https://', TLSAdapter())
    return fetch

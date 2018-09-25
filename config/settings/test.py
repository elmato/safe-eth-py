from .base import *

INSTALLED_APPS += (
)

SECRET_KEY = 'testtest'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

ETHEREUM_NODE_URL = 'http://localhost:8545'
SAFE_FUNDER_PRIVATE_KEY = '4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d'
SAFE_TX_SENDER_PRIVATE_KEY = '6cbed15c793ce57650b9877cf6fa156fbef513c4e6134f022a85b1ffdd59b2a1'
SAFE_FUNDER_MAX_ETH = 0.1
SAFE_FUNDING_CONFIRMATIONS = 0
SAFE_GAS_PRICE = 1
SAFE_CONTRACT_ADDRESS = '0x2727D69C0BD14B1dDd28371B8D97e808aDc1C2f7'
SAFE_VALID_CONTRACT_ADDRESSES = [SAFE_CONTRACT_ADDRESS]

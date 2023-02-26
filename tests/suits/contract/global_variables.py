from tests.contract.brocker_init import BrokerPact
from tests.contract.client import ServiceClient


consumer = 'Client'
provider = 'Server'
mock_url = 'http://localhost:1234'
base_url = 'https://nextgenkube.ai-logix.net'

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "",
    "tenantId": "ad41d6c3-67f0-47cc-9de3-e07fd185c1c7"
}

pact = BrokerPact(consumer, provider)
contract = pact.get_pact_contract()
client = ServiceClient(mock_url)

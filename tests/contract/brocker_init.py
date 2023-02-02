import atexit
from pact import Consumer, Provider, Like, EachLike, Term, Verifier



class BrokerPact:
    """
    This class is used to initiate pact broker
    """

    def __init__(self, consumer, provider):
        self.consumer = consumer
        self.provider = provider
        self.contract_path = fr"{consumer}-{provider}.json"

        self.like = Like
        self.eachlike = EachLike
        self.term = Term

    def get_pact_contract(self):
        pact = Consumer(self.consumer).has_pact_with(Provider(self.provider))

        pact.start_service()
        atexit.register(pact.stop_service)

        return pact

    def verify_pact(self, base_url: str):
        result, logs = Verifier(provider=None, provider_base_url=base_url).verify_pacts(self.contract_path)
        return result

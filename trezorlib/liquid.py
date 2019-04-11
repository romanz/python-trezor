from . import messages
from .tools import expect


@expect(messages.LiquidBlindedOutput)
def blind_output(client):
    return client.call(
        messages.LiquidBlindOutput(amount=123, script_pubkey=b'PUBKEY')
    )

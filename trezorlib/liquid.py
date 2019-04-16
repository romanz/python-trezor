from . import messages
from .tools import expect


@expect(messages.LiquidBlindedOutput)
def blind_output(client):
    blind = b'\xAA'*32
    return client.call(
        messages.LiquidBlindOutput(amount=123, script_pubkey=blind)
    )

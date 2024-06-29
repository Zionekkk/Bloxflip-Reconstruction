import tls_client

session = tls_client.Session(
    client_identifier="firefox_127",
    random_tls_extension_order=True
)

res = session.get(
    "https://api.bloxflip.com/live-feed/all-bets",
)

#print(res.text)
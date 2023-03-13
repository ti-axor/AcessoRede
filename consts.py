axor_to_mdl = {
    "lcosta": "lmichaeli",
    "fcunha": "fteixeira",
    "tsouza": "tvsouza",
    "eguedes": "esiqueira",
    # 'jmeyrelles': 'tvsouza',
}

# net = ["100\\finnet-remessa", "100\\finnet-retorno", "99\\depto"]

# user_list = {
#     'lmichaeli': net,
#     'fteixeira': [],
#     'tvsouza': [net[len(net) - 1]],
#     'esiqueira': [],
#     'lbarbosa': net[0:2],
#     'cbarbosa': [net[len(net) - 1]],
#     'mfrancisco': net,
#     'lmosa': net,
#     'cmorielo': net[0:2],
#     'jmeyrelles': net,
# }


direc = ["Y:", "F:", "G:"]

net = [
    {"drt": "100\\finnet-remessa", "lct": "Y:"},
    {"drt": "100\\finnet-retorno", "lct": "F:"},
    {"drt": "99\\depto", "lct": "G:"},
]

user_list = {
    "lmichaeli": net,
    "fteixeira": [],
    "tvsouza": [net[len(net) - 1]],
    "esiqueira": [],
    "lbarbosa": net[0:2],
    "cbarbosa": [net[len(net) - 1]],
    "mfrancisco": net,
    "lmosa": [net[len(net) - 1]],
    "cmorielo": net[0:2],
    "jmeyrelles": net,
}

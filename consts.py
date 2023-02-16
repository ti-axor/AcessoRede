axor_to_mdl = {
    'lcosta': 'lmichaeli',
    'fcunha': 'fteixeira',
    'tsouza': 'tvsouza',
    'eguedes': 'esiqueira',
    # 'jmeyrelles': 'tvsouza',
}

net = ["100\\finnet-remessa", "100\\finnet-retorno", "99\\depto"]

user_list = {
    'lmichaeli': net,
    'fteixeira': [],
    'tvsouza': [net[len(net) - 1]],
    'esiqueira': [],
    'lbarbosa': net[0:2],
    'cbarbosa': [net[len(net) - 1]],
    'mfrancisco': net,
    'lmosa': net,
    'cmorielo': net[0:2],
    'jmeyrelles': net,
}


direc = ["Y:", "F:", "G:"]

net_test = [
    {
        "drt": "100\\finnet-remessa",
        "lct": "Y:"
    },
    {
        "drt": "100\\finnet-retorno",
        "lct": "F:"
    },
    {
        "drt": "99\\depto",
        "lct": "G:"
    }
]

user_list_test = {
    'lmichaeli': net_test,
    'fteixeira': [],
    'tvsouza': [net_test[len(net) - 1]],
    'esiqueira': [],
    'lbarbosa': net_test[0:2],
    'cbarbosa': [net_test[len(net) - 1]],
    'mfrancisco': net_test,
    'lmosa': net_test,
    'cmorielo': net_test[0:2],
    'jmeyrelles': net_test,
}

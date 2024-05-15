def bombons (dinheiro, preço) :
    n_bombons = dinheiro // preço
    troco = dinheiro % preço
    return n_bombons, troco 

def a_mais(dinheiro, preço):
    qtd, troco = bombons(dinheiro, preço)
    return preço - troco

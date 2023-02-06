# from inventory_report.inventory.product import Product

from inventory_report.inventory.product import Product


def test_cria_produto():
    product_instance = Product(
        '0',
        'Tap Shoes',
        'IDONEOS Ltda',
        '01/01/2021',
        '01/01/2050',
        '457230',
        'manter em local arejado e seco'
    )

    assert product_instance.id == '0'
    assert product_instance.nome_do_produto == 'Tap Shoes'
    assert product_instance.nome_da_empresa == 'IDONEOS Ltda'
    assert product_instance.data_de_fabricacao == '01/01/2021'
    assert product_instance.data_de_validade == '01/01/2050'
    assert product_instance.numero_de_serie == '457230'
    assert product_instance.instrucoes_de_armazenamento == 'manter em local'
    ' arejado e seco'

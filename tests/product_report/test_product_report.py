# from inventory_report.inventory.product import Product


from inventory_report.inventory.product import Product


def test_relatorio_produto():
    report_instance = Product(
        '0',
        'Tap Shoes',
        'IDONEOS Ltda',
        '01/01/2021',
        '01/01/2050',
        '457230',
        'instruções'
    )

    report_instance = str(report_instance)

    report = (
        "O produto Tap Shoes"
        + " fabricado em 01/01/2021"
        + " por IDONEOS Ltda com validade"
        + " até 01/01/2050"
        + " precisa ser armazenado instruções."
    )

    assert report == report_instance

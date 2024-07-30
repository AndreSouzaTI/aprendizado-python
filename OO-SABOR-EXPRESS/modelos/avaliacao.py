class Avaliacao:
    """
        Inicializa uma instância de Avaliação.

        Parâmetros:
        - cliente (str): O nome do cliente.
        - nota (int): A nota dada pelo cliente ao restaurante.
        """
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota
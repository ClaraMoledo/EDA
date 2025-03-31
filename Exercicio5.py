class ArvoreGenealogica:
    def __init__(self):
        """Inicializa a árvore genealógica vazia."""
        self.membros = {}  # Dicionário para armazenar todos os membros
    
    def adicionar_membro(self, nome, idade, sexo, pai=None):
        """
        Adiciona um novo membro à árvore genealógica.
        
        Args:
            nome (str): Nome do membro.
            idade (int): Idade do membro.
            sexo (str): Sexo do membro ('M' ou 'F').
            pai (str, optional): Nome do pai. Default é None.
        
        Returns:
            bool: True se adicionado com sucesso, False caso contrário.
        """
        # Criar novo membro
        novo_membro = {
            'nome': nome,
            'idade': idade,
            'sexo': sexo,
            'filhos': []
        }
        
        # Verificar se já existe um membro com esse nome
        if nome in self.membros:
            print(f"Erro: Já existe um membro com o nome '{nome}'.")
            return False
        
        # Adicionar à árvore
        self.membros[nome] = novo_membro
        
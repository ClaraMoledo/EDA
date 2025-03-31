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
        
    
        self.membros[nome] = novo_membro
        if pai is not None:
            if pai not in self.membros:
                print(f"Erro: Pai '{pai}' não encontrado na árvore.")
                del self.membros[nome]
                return False
            
            # Adicionar como filho do pai
            self.membros[pai]['filhos'].append(novo_membro)
        
        return True
    
    def buscar_membro(self, nome):
        """
        Busca um membro pelo nome.
        
        Args:
            nome (str): Nome do membro a ser buscado.
        
        Returns:
            dict or None: Dicionário do membro se encontrado, None caso contrário.
        """
        if nome in self.membros:
            return self.membros[nome]
        else:
            print(f"Membro '{nome}' não encontrado.")
            return None
    
    def _coletar_descendentes(self, membro, lista_descendentes):
        """
        Função auxiliar recursiva para coletar descendentes.
        
        Args:
            membro (dict): Membro atual.
            lista_descendentes (list): Lista onde serão adicionados os descendentes.
        """
        for filho in membro['filhos']:
            lista_descendentes.append(filho['nome'])
            self._coletar_descendentes(filho, lista_descendentes)
    
    def descendentes(self, nome):
        """
        Retorna uma lista com todos os descendentes do membro especificado.
        
        Args:
            nome (str): Nome do membro.
        
        Returns:
            list: Lista de nomes dos descendentes.
        """
        membro = self.buscar_membro(nome)
        if membro is None:
            return []
        
        lista_descendentes = []
        self._coletar_descendentes(membro, lista_descendentes)
        return lista_descendentes
    
    def _buscar_pai(self, nome_filho):
        """
        Função auxiliar para encontrar o pai de um membro.
        
        Args:
            nome_filho (str): Nome do filho.
            
        Returns:
            str or None: Nome do pai se encontrado, None caso contrário.
        """
        for nome_pai, pai in self.membros.items():
            for filho in pai['filhos']:
                if filho['nome'] == nome_filho:
                    return nome_pai
        return None
    
    def antepassados(self, nome):
        """
        Retorna uma lista com todos os antepassados diretos do membro.
        
        Args:
            nome (str): Nome do membro.
            
        Returns:
            list: Lista de nomes dos antepassados.
        """
        if nome not in self.membros:
            print(f"Membro '{nome}' não encontrado.")
            return []
        
        lista_antepassados = []
        atual = nome
        
        while True:
            pai = self._buscar_pai(atual)
            if pai is None:
                break
            
            lista_antepassados.append(pai)
            atual = pai
        
        return lista_antepassados
    
    def visualizar_arvore(self):
        """
        Imprime a árvore genealógica de forma hierárquica.
        """
        # Encontrar membros raiz (sem pais)
        raizes = []
        for nome in self.membros:
            pai = self._buscar_pai(nome)
            if pai is None:
                raizes.append(nome)
        
        print("\nÁrvore Genealógica:")
        print("=" * 40)
        
        for raiz in raizes:
            self._mostrar_subarvore(raiz, 0)
    
    def _mostrar_subarvore(self, nome, nivel):
        """
        Função auxiliar recursiva para mostrar uma subárvore.
        
        Args:
            nome (str): Nome do membro raiz da subárvore.
            nivel (int): Nível de indentação.
        """
        membro = self.membros[nome]
        indentacao = "  " * nivel
        genero = "M" if membro['sexo'] == 'M' else "F"
        
        print(f"{indentacao}└─ {membro['nome']} ({genero}, {membro['idade']} anos)")
        
        for filho in membro['filhos']:
            self._mostrar_subarvore(filho['nome'], nivel + 1)


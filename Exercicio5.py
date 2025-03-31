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
        if nome in self.membros:
            return self.membros[nome]
        else:
            print(f"Membro '{nome}' não encontrado.")
            return None
    
    def _coletar_descendentes(self, membro, lista_descendentes):

        for filho in membro['filhos']:
            lista_descendentes.append(filho['nome'])
            self._coletar_descendentes(filho, lista_descendentes)
    
    def descendentes(self, nome):
 
        membro = self.buscar_membro(nome)
        if membro is None:
            return []
        
        lista_descendentes = []
        self._coletar_descendentes(membro, lista_descendentes)
        return lista_descendentes
    
    def _buscar_pai(self, nome_filho):

        for nome_pai, pai in self.membros.items():
            for filho in pai['filhos']:
                if filho['nome'] == nome_filho:
                    return nome_pai
        return None
    
    def antepassados(self, nome):
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

        membro = self.membros[nome]
        indentacao = "  " * nivel
        genero = "M" if membro['sexo'] == 'M' else "F"
        
        print(f"{indentacao}└─ {membro['nome']} ({genero}, {membro['idade']} anos)")
        
        for filho in membro['filhos']:
            self._mostrar_subarvore(filho['nome'], nivel + 1)
# Exemplo de uso
def testar_arvore_genealogica():
    arvore = ArvoreGenealogica()
    
    # Adicionar membros
    arvore.adicionar_membro("João", 70, "M")
    arvore.adicionar_membro("Maria", 65, "F")
    arvore.adicionar_membro("Carlos", 50, "M", "João")
    arvore.adicionar_membro("Ana", 48, "F", "João")
    arvore.adicionar_membro("Pedro", 30, "M", "Carlos")
    arvore.adicionar_membro("Lucia", 28, "F", "Carlos")
    arvore.adicionar_membro("Lucas", 10, "M", "Pedro")
    arvore.adicionar_membro("Julia", 8, "F", "Pedro")
    
    # Visualizar árvore
    arvore.visualizar_arvore()
    
    # Testar busca
    print("\nBusca de membro:")
    membro = arvore.buscar_membro("Pedro")
    if membro:
        print(f"Encontrado: {membro['nome']}, {membro['idade']} anos, sexo: {membro['sexo']}")
    
    # Testar descendentes
    print("\nDescendentes de João:")
    desc = arvore.descendentes("João")
    print(f"Total: {len(desc)} descendentes")
    print(", ".join(desc))
    
    # Testar antepassados
    print("\nAntepassados de Lucas:")
    ante = arvore.antepassados("Lucas")
    print(f"Total: {len(ante)} antepassados diretos")
    print(", ".join(ante))
    
    # Testar antepassados (caso sem antepassados)
    print("\nAntepassados de João:")
    ante = arvore.antepassados("João")
    print(f"Total: {len(ante)} antepassados diretos")
    if ante:
        print(", ".join(ante))
    else:
        print("Nenhum antepassado encontrado (membro raiz)")

# Executar o teste
testar_arvore_genealogica()

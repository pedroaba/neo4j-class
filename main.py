from neo4j import GraphDatabase, Driver


def find_engineers(db):
    query = "MATCH (p:Pessoa) WHERE p.profissao = 'Engenheiro' OR p.profissao = 'Engenheira' RETURN p.nome AS nome"
    with db.session() as session:
        results = session.run(query)
        for record in results:
            print(f"Engenheiro: {record['nome']}")


def find_children_of(db, name):
    query = f"MATCH (p:Pessoa)-[:PAI_DE|MAE_DE]->(child:Pessoa) WHERE p.nome = '{name}' RETURN child.nome AS nome"
    with db.session() as session:
        results = session.run(query)
        for record in results:
            print(f"{name} é pai/mãe de: {record['nome']}")


def find_partner_since(db, name):
    query = f"MATCH (p:Pessoa)-[r:CASADO_COM]->(partner:Pessoa) WHERE p.nome = '{name}' RETURN partner.nome AS nome, r.desde AS desde"
    with db.session() as session:
        results = session.run(query)
        for record in results:
            print(f"{name} é casado(a) com {record['nome']} desde {record['desde']}")


def print_menu():
    title = " Exercício avaliativo sobre NEO4J "
    separator = "=" * 10
    top_bottom_separator = "=" * len(title)

    print(top_bottom_separator)
    print(f"{separator}{title}{separator}")
    print(top_bottom_separator)

    print("1. Quem é engenheiro?")
    print("2. Quem é pai de quem?")
    print("3. Desde quando está namorando?")
    print("4. Sair")


def main(neo4j: Driver):
    print_menu()

    loop = True
    while loop:
        option = input("Escolha uma das opções: ")

        match int(option):
            case 5:
                loop = False
            case 1:
                find_engineers(neo4j)
            case 2:
                name = input("Insira o nome da pessoa: ")
                find_children_of(neo4j, name)
            case 3:
                name = input("Insira o nome da pessoa: ")
                find_partner_since(neo4j, name)

    neo4j.close()


if __name__ == "__main__":
    user = "neo4j"
    uri = "neo4j+s://31babb77.databases.neo4j.io"
    password = "q6zYGRAz5XObU-mlkTGZ368wme0abggwCl87k4kcGBk"

    driver = GraphDatabase.driver(uri, auth=(user, password))

    main(driver)

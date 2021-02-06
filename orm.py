from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Criando conexão com o banco de dados
engine = create_engine('sqlite:///banco.db')

# Criando as seções
Session = sessionmaker(bind=engine)
session = Session()

# Criando a base declarativa
Base = declarative_base()


# Classe estudante
class Students(Base):
    __tablename__ = 'students'
    id_student = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f'{self.name}, {self.age}'


Base.metadata.create_all(engine)

# ============================= Cadastrando ===================================
# Adicionando estudantes
student = Students(name='Anna', age=18)
session.add(student)
session.commit()
# =============================================================================

# ============================= Listar ========================================
# Busca tudo
student = session.query(Students).all()
print(student)

# Número de rgistros
student = session.query(Students).count()
print(student)

# Primeiro reistro
student = session.query(Students).first()
print(student)

# filter
student = session.query(Students).filter(Students.name == 'Alex').all()
print(student)

# filter_by
student = session.query(Students).filter_by(name='Anna').all()
print(student)

# Buscando por similaridade
query = session.query(Students).filter(Students.name.like('%A%')).all()
print(query)
# =============================================================================

# ============================== Excluindo ====================================
data = session.query(Students).filter(Students.name == 'Alex').delete()

query = session.query(Students).filter(Students.name.like('%A%')).all()
print(query)
# =============================================================================

# ============================== Atualizando ==================================
data = session.query(Students).filter(Students.name == 'Anna').update(
        {'name': 'ana', 'age': 20}
)

query = session.query(Students).filter(Students.name.like('%A%')).all()
print(query)
# =============================================================================

from app import ma

# Receitas Schema
class ReceitasSchema(ma.Schema):
    # fields to show
    class Meta:
        fields = ('id', 'descricao', 'valor', 'data')

class DespesasSchema(ma.Schema):
    # fields to show
    class Meta:
        fields = ('id', 'descricao', 'valor', 'data', 'categoria')

# Receitas Schema
class UserSchema(ma.Schema):
    # fields to show
    class Meta:
        fields = ('id', 'nome', 'senha')

receita_schema = ReceitasSchema()
receitas_schema = ReceitasSchema(many=True)

despesa_schema = DespesasSchema()
despesas_schema = DespesasSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
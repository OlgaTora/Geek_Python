# import databases
# import sqlalchemy
# from sqlalchemy import create_engine, ForeignKey
#
# DATABASE_URL = "sqlite:///clinic.db"
# database = databases.Database(DATABASE_URL)
# metadata = sqlalchemy.MetaData()
#
# clients = sqlalchemy.Table(
#     'clients',
#     metadata,
#     sqlalchemy.Column('client_id', sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column('document', sqlalchemy.String(128), nullable=False, unique=True),
#     sqlalchemy.Column('surname', sqlalchemy.String(128), nullable=False),
#     sqlalchemy.Column('firstname', sqlalchemy.String(128), ),
#     sqlalchemy.Column('patronymic', sqlalchemy.String(128)),
#     sqlalchemy.Column('birthday', sqlalchemy.Date, nullable=False),
# )
#
# #
# # products = sqlalchemy.Table(
# #     'products',
# #     metadata,
# #     sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
# #     sqlalchemy.Column('product_name', sqlalchemy.String(32)),
# #     sqlalchemy.Column('description', sqlalchemy.Text(256)),
# #     sqlalchemy.Column('price', sqlalchemy.Float, nullable=False),
# # )
# #
# # orders = sqlalchemy.Table(
# #     'orders',
# #     metadata,
# #     sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
# #     sqlalchemy.Column('user_id', sqlalchemy.Integer, ForeignKey('users.id'), nullable=False),
# #     sqlalchemy.Column('product_id', sqlalchemy.Integer, ForeignKey('products.id'), nullable=False),
# #     sqlalchemy.Column('order_date', sqlalchemy.Date),
# #     sqlalchemy.Column('status', sqlalchemy.String(32)),
# # )
#
# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )
# metadata.create_all(engine)

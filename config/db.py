from sqlalchemy import create_engine,MetaData
engine=create_engine("mysql+pymysql://root:Sandra26@localhost:3306/utxjdb")
meta=MetaData()
conn=engine.connect()

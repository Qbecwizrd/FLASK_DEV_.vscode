from flask import Flask,request
#from  db import stores,items 
from flask_smorest import abort,Api
import uuid
from db import db
import models
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint  
import os  
def create_app(db_url):
    app=Flask(__name__) 
    # app.config["PROPOGATE_EXCEPTIONS"]=True
    # app.config["API_TITLE"]="Stores REST API"
    # app.config["API_VERSION"]="v1" 
    # app.config["OPENAPI_VERSION"]="3.0.3"
    # app.config["OPENAPI_URL_PREFIX"]="/"
    # app.config["OPEN"]
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    api = Api(app)

    @app.before_first_request
    def create_tables():
        db.create_all()
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    #create store
    # #create get method to get the stores 
    # @app.get("/store")
    # def get_stores():
    #     return {"store":list(stores.values())}

    # #create post method
    # @app.post("/store")
    # def create_stores():
    #     store_data=request.get_json()
    #     if "name" not in store_data:
    #         abort(404,message="Bad request.Please ensure that 'name' is included in the JSON playload")
    #     for store in stores:
    #         if store_data["name"]==store["name"]:
    #             abort(404,message="store already exists")
    #     store_id=uuid.uuid4().hex #f4435h3h3j3j2jh5543  
    #     new_store={**store_data,"id":store_id}
    #     stores[store_id]=new_store
    #     return new_store,201
    # #create method to enter items in store
    # @app.post("/item")
    # def create_item():  
    #     item_data=request.get_json()
    #     if(
    #         "price" not in item_data 
    #         or
    #         "store_id" not in item_data
    #         or 
    #         "name" not in item_data
    #     ):
    #         abort(
    #             400,
    #             message="Bad Request.Ensure 'price','store_id',and 'name' are included in the JSON payload. "
    #         )
    #     for item in items.values():
    #         if(
    #             item_data["name"]==item["name"]
    #             and item_data["store_id"]==item["store_id"]
    #         ):
    #             abort(404,"item already exists")
    #     if item_data["store_id"] not in stores:
    #         return abort(404,message={"store not found"})
    #     item_id=uuid.uuid4().hex
    #     item={**item_data,"id":item_id}
    #     items[item_id]=item
    #     return item,201
    # #get all items
    # @app.get("/item")
    # def get_all_items():
    #     #return "hello world"
    #     return {"items":list(items.values())}


    # #get the store 
    # @app.get("/store/<string:store_id>")
    # def get_store(store_id):    
    #     try:
    #         return stores[store_id]
    #     except KeyError:
    #         return abort(404,message="Store not found")


    # #get the items in the store
    # @app.get("/item/<string:item_id>")
    # def get_item_in_store(item_id):
    #     try:
    #         return items[item_id]
    #     except KeyError:
    #         return abort(404,message="item not found")

    # #delete an item
    # @app.delete("/item/<string:item_id>")
    # def delete_item(item_id):
    #     try:
    #         del items[item_id]
    #         return {"message":"Item has been deleted"}
    #     except KeyError:
    #         abort(404,message="Item not found")

    # #update the data in items
    # @app.put("/item/<string:item_id>")
    # def update_item(item_id):
    #     item_data=request.get_json()
    #     if "price" not in item_data or "name" not in item_data:
    #         abort(404,mesaage="Bad Request.Ensure that the 'price' and 'name' included in the JSON payload")
    #     try:
    #         item=items[item_id]
    #         item|=item_data

    #         return item
    #     except KeyError:
    #         abort(404,message="Item not found")

    # #delete a store in stores
    # @app.delete("/store/<string:store_id>")
    # def store_delete(store_id):
    #     try:
    #         del stores[store_id]
    #         return {"message":"Store Deleted"}
    #     except KeyError:
    #         abort(404,message="Store not found")

    return app

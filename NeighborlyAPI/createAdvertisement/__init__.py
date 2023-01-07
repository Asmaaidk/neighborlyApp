import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://neighborlycosmos:BTKJJ9JN82sG5M2wtPbYR0xkY2x8D63qZwthv5lRhpI2QuOK1UV7HWGB8BB8nIlOEO41XWmYCooLACDbrtoYFg==@neighborlycosmos.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlycosmos@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['neighborlydb']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )
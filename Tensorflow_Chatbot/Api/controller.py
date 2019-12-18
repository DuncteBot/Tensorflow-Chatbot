from django.http import JsonResponse
import json
from Bot import ChatBot as bot
from time import gmtime, strftime


def index(request):
    if request.method == 'POST':
        try:
            jsonData = json.loads(request.body.decode('utf-8'))
            msg = jsonData["msg"]
            user_id = jsonData["user_id"]
            res = bot.ChatBot.getBot().response(sentence=msg, user_id=user_id, show_details=True)
            time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            return JsonResponse({
                "desc": "Success",
                "ques": msg,
                "res": res,
                "user_id": user_id,
                "time": time
            })
        except Exception as e:
            return JsonResponse({"desc": "Missing parameters"}, status=400)

    else:
        return JsonResponse({"desc": "Bad request"}, status=400)

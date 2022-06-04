from flask import Flask, render_template, request, session, redirect, jsonify
import boto3
import datetime

app = Flask(__name__)

member_status = ["入室", "在室"]

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

@app.route("/")
def init(): 
    return render_template("menu.html")

#Ajaxの利用
@app.route("/ajax", methods=["GET","POST"])
def ajax():
    #現在時刻
    now_time = str(datetime.datetime.now())
    #状態を取得
    status = int(request.args.get("status"))
    #status = request.form.get("status")

    #Ajax確認用コード
    print("ajax成功")
    print(status)
    print(now_time)
    if status == 0:
        print("入室できた")
    elif status == 1:
        print("退室できた")

    
    #新しいアイテムの作成
    table = dynamodb.Table('user_log')
    table.put_item(
    Item={
        'room_number': 'KD0001_',
        'status': status,
        'time': now_time,
        }
    )
    

    return "True"
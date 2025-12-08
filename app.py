from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import asyncio
from telethon.sync import TelegramClient

app = Flask(__name__)
CORS(app)  # للسماح بطلبات من InfinityFree

# بيانات تيليجرام
API_ID = os.getenv('API_ID', '29111381')
API_HASH = os.getenv('API_HASH', 'c86ad2e2fadf7016897e792c8e5f2be9')
BOT_TOKEN = os.getenv('BOT_TOKEN', '8191013163:AAGFpIhPDo8_fH6QI5BTFIynUSZQK_tFp8s')
DEVELOPER_ID = 39492149

# تهيئة Telethon
client = None

def init_telegram():
    global client
    if client is None:
        client = TelegramClient('bot_session', API_ID, API_HASH)
        client.start(bot_token=BOT_TOKEN)

@app.route('/send-vote', methods=['POST', 'OPTIONS'])
def send_vote():
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.json
        
        # التأكد من تهيئة العميل
        init_telegram()
        
        # نص الرسالة للمطور
        message = f"""
        🗳️ **تصويت جديد!**
        
        👤 **المستخدم:**
        - الاسم: {data.get('first_name', 'غير معروف')}
        - ID: `{data.get('user_id')}`
        - يوزر: @{data.get('username', 'لا يوجد')}
        
        🖥️ **معلومات الجهاز:**
        - النظام: {data.get('platform')}
        - الشاشة: {data.get('screen')}
        - اللغة: {data.get('language')}
        
        🌐 **المتصفح:**
        {data.get('user_agent', 'غير معروف')[:200]}...
        
        ⏰ **الوقت:** {data.get('timestamp')}
        """
        
        # إرسال للمطور
        client.send_message(DEVELOPER_ID, message)
        
        # تأكيد للمستخدم
        try:
            client.send_message(
                int(data['user_id']),
                "✅ **شكراً لتصويتك!**\nتم استلام صوتك بنجاح."
            )
        except:
            pass  # إذا كان المستخدم حظر البوت
        
        return jsonify({
            "success": True,
            "message": "تم التصويت بنجاح"
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"خطأ: {str(e)}"
        }), 500

@app.route('/health')
def health():
    return jsonify({"status": "online"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

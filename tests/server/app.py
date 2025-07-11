# app.py - Flask 서버 진입점
from flask import Flask, request, jsonify, abort
from utils.image_processor import process_image
from utils.blur_face import blur_face
from utils.error_handler import make_error
from utils.auth import verify_token
from PIL import Image
import base64, io

app = Flask(__name__)

# 보안 인증 + 이미지 처리 + 결과 생성
@app.route('/api/v1/_secure_predict_xyz123', methods=['POST'])
def secure_predict():
    # 테스트용 인증 비활성화
    # verify_token(request)

    try:
        data = request.json
        if not data or 'image_base64' not in data:
            return make_error('MISSING_IMAGE_DATA', 400)

        image = Image.open(io.BytesIO(base64.b64decode(data['image_base64'])))

        # 요구사항 확장 정보
        # metadata = data.get('metadata', {})
        # user_id = metadata.get('user_id', 'anonymous')
        # timestamp = metadata.get('timestamp')

        processed_img, result = process_image(image)
        blurred_img = blur_face(processed_img)

        buf = io.BytesIO()
        blurred_img.save(buf, format='JPEG')
        encoded_img = base64.b64encode(buf.getvalue()).decode('utf-8')

        return jsonify({
            "result": result,
            "image_base64": encoded_img
            # , "image_url": f"http://<server_ip>/result/{user_id}_{timestamp}.jpg"
        })

    except Exception as e:
        return make_error(str(e), 500)

# 상태 확인용 엔드포인트
@app.route('/ping')
def ping():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

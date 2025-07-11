# utils/error_handler.py
from flask import jsonify

def make_error(message, code):
    """
    통일된 오류 응답 JSON 반환
    """
    return jsonify({
        'error': message,
        'code': code
    }), code

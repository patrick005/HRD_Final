# utils/auth.py
from flask import abort

def verify_token(request):
    """
    헤더 Authorization: Bearer <token> 형식 인증 처리
    """
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        abort(401)  # Unauthorized
    token = auth_header.split(' ')[1]
    if token != "your-secure-token":  # 실제 운영용 키로 교체
        abort(403)  # Forbidden

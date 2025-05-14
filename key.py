from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
import base64

# 프라이빗 키 생성
private_key = ec.generate_private_key(ec.SECP256R1())

# 퍼블릭 키 추출
public_key = private_key.public_key()

# base64url 형식으로 변환 (웹 표준용)
vapid_private = base64.urlsafe_b64encode(
    private_key.private_numbers().private_value.to_bytes(32, "big")
).rstrip(b'=').decode('utf-8')

vapid_public = base64.urlsafe_b64encode(
    public_key.public_bytes(
        serialization.Encoding.X962,
        serialization.PublicFormat.UncompressedPoint
    )
).rstrip(b'=').decode('utf-8')

print("VAPID_PUBLIC_KEY =", vapid_public)
print("VAPID_PRIVATE_KEY =", vapid_private)
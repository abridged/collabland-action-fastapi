import requests
from os import getenv
import binascii
import base58
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from fastapi import Request, HTTPException
import time


class SignatureVerifier:
    ed25519_public_key = None
    ecdsa_public_key = None

    def __init__(self) -> None:
        stage = "" if getenv("SERVER_ENV") == "production" else "-qa"
        api_url = f"https://api{stage}.collab.land/config"
        res = requests.get(api_url).json()
        SignatureVerifier.ed25519_public_key = self.convert_base58_to_hex(
            res.get("actionEd25519PublicKey")
        )
        SignatureVerifier.ecdsa_public_key = res.get("actionEcdsaPublicKey")
        print("SignatureVerifier Initialized.")
        print(f"api_url: {api_url}")
        print(f"ed25519_public_key: {SignatureVerifier.ed25519_public_key}")
        print(f"ecdsa_public_key: {SignatureVerifier.ecdsa_public_key}")

    def convert_base58_to_hex(self, base58_str: str) -> str:
        return binascii.hexlify(base58.b58decode(base58_str)).decode()

    async def verify_signature(req: Request):
        if req.url.path.endswith("/interactions") and req.method == "POST":
            ecdsa_signature = req.headers.get("X-Signature-Ecdsa")
            ed25519_signature = req.headers.get("X-Signature-Ed25519")
            signature_timestamp = int(req.headers.get("X-Signature-Timestamp"))
            signature_type = "ecdsa" if ecdsa_signature != None else "ed25519"
            request_body = await req.body()
            current_timestamp = int(time.time() * 1000)
            if (current_timestamp - signature_timestamp) < (5 * 60 * 1000):
                pass
            else:
                raise HTTPException(
                    401, detail="Invalid Request - Signature Timestamp in expired."
                )
            print(f"ecdsa_signature: {ecdsa_signature}")
            print(f"ed25519_signature: {ed25519_signature}")
            print(f"signature_timestamp: {signature_timestamp}")
            print(f"signature_type: {signature_type}")
            if signature_type == "ed25519":
                SignatureVerifier.verify_ed25519(
                    ed25519_signature=ed25519_signature,
                    signature_timestamp=f"{signature_timestamp}",
                    request_body=request_body,
                    key=SignatureVerifier.ed25519_public_key,
                )
            return
        else:
            print("Skipping verification...")
            return

    def verify_ed25519(
        ed25519_signature: str,
        signature_timestamp: int,
        request_body: bytes,
        key: str,
    ):
        verify_key = VerifyKey(bytes.fromhex(key))
        signature = bytes.fromhex(ed25519_signature)
        signed_data = bytes(signature_timestamp, "utf8") + request_body
        try:
            verify_key.verify(signed_data, signature)
            print("ED25519 signature verification successful.")
        except BadSignatureError:
            raise HTTPException(401, detail="Invalid Request - Signature not verified!")

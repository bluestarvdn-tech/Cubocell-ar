"""
CuboCell AR — Servidor Local com HTTPS
Não requer OpenSSL instalado.
"""
import sys, socket, os, threading, http.server

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()

# Tentar gerar certificado com trustme (não precisa OpenSSL)
def tentar_trustme():
    try:
        import trustme, ssl
        ca = trustme.CA()
        server_cert = ca.issue_cert("localhost", get_ip())
        server_cert.private_key_pem.write_to_path("key.pem")
        server_cert.private_key_pem.write_to_path("key.pem")
        with open("cert.pem", "wb") as f:
            for blob in server_cert.cert_chain_pems:
                blob.write_to_path("cert.pem")
        return True
    except ImportError:
        return False

# Tentar com cryptography
def tentar_cryptography():
    try:
        from cryptography import x509
        from cryptography.x509.oid import NameOID
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import rsa
        import datetime, ipaddress

        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        ip = get_ip()

        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, u"cubocell-local"),
        ])
        cert = (x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(datetime.datetime.utcnow())
            .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
            .add_extension(x509.SubjectAlternativeName([
                x509.DNSName(u"localhost"),
                x509.IPAddress(ipaddress.IPv4Address(ip)),
            ]), critical=False)
            .sign(key, hashes.SHA256())
        )

        with open("key.pem", "wb") as f:
            f.write(key.private_bytes(
                serialization.Encoding.PEM,
                serialization.PrivateFormat.TraditionalOpenSSL,
                serialization.NoEncryption()
            ))
        with open("cert.pem", "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))
        return True
    except ImportError:
        return False

import ssl
from pathlib import Path

PORT = 4443
ip = get_ip()

cert_ok = Path("cert.pem").exists() and Path("key.pem").exists()

if not cert_ok:
    print("Gerando certificado SSL...")
    if tentar_cryptography():
        print("Certificado gerado com cryptography!")
        cert_ok = True
    else:
        print("Instalando cryptography...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])
        if tentar_cryptography():
            print("Certificado gerado!")
            cert_ok = True

if not cert_ok:
    print("ERRO: Não foi possível gerar certificado.")
    input("Pressione Enter para fechar.")
    sys.exit(1)

handler = http.server.SimpleHTTPRequestHandler
handler.log_message = lambda *a: None  # silenciar logs

httpd = http.server.HTTPServer(("0.0.0.0", PORT), handler)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain("cert.pem", "key.pem")
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)

print("\n" + "="*55)
print("  CuboCell AR — Servidor rodando!")
print("="*55)
print(f"\n  No celular (mesmo Wi-Fi), acesse:")
print(f"\n  https://{ip}:{PORT}/celula-animal.html")
print(f"  https://{ip}:{PORT}/celula-vegetal.html")
print(f"  https://{ip}:{PORT}/procarionte.html")
print(f"\n  ⚠️  No celular: aceite o aviso 'site nao seguro'")
print(f"      Clique em Avancado > Continuar assim mesmo")
print(f"\n  Ctrl+C para parar")
print("="*55 + "\n")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServidor parado.")

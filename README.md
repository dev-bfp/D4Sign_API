🖋️ Integração com API D4Sign - Geração e Assinatura Automatizada de Documentos
Este módulo Python facilita a integração direta com a plataforma D4Sign, permitindo criar, configurar, enviar e acompanhar contratos para assinatura digital. A automação é especialmente útil para provedores de internet, sistemas de gestão e empresas que utilizam fluxos de assinatura recorrentes.

🔧 Funcionalidades implementadas
📄 Criação de documentos a partir de templates Word com preenchimento dinâmico de campos

👥 Adição de signatários com autenticação e selfie

📩 Envio automático para assinatura

✍️ Posicionamento da assinatura no documento

🔗 Download do documento assinado

🔔 Configuração de Webhooks para receber notificações em tempo real

🚀 Exemplo de uso
python
Copiar
Editar
from API_D4Sign import d4sign

# Criar documento com template preenchido automaticamente
doc = d4sign.make_document_by_template(dados_cliente)

# Adicionar signatário
d4sign.add_signer(doc['uuid'], "cliente@email.com")

# Definir posição da assinatura na página
d4sign.set_position_sign(doc['uuid'], "cliente@email.com")

# Enviar para assinatura
d4sign.send_to_signer(doc['uuid'])

# Baixar o documento
d4sign.get_url_doc(doc['uuid'])

# Registrar webhook para receber eventos
d4sign.webhook(doc['uuid'])
⚙️ Requisitos
Python 3.7+

Dependências:

requests

oauth2client

locale

datetime

🔐 Observações
As variáveis sensíveis como id_safe, endpoint_token, url_sign, url_webhook e id_template devem estar definidas no módulo Tokens.py.

A integração foi pensada para funcionar em conjunto com sistemas como IXC Provedor (já utilizado no projeto).

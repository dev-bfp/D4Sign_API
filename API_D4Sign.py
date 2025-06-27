import requests
import datetime
import time
import locale; locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
from pprint import pp as pp
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials # LIB DE AUTENTICAÇÃO DA GOOGLE
from Tokens import *

class d4sign():
    def make_document_by_template(dd, id_safe=id_safe, endpoint_token=endpoint_token, url_sign=url_sign):

        endpoint = f'/documents/{id_safe}/makedocumentbytemplateword{endpoint_token}'
        url_sign = url_sign + endpoint
        payload = {
            'name_document': f'Termo de Adesão SCM Red Fibra - {dd['contrato']['id']} - {dd['cliente']['razao']}',
            'templates': {id_template: {
                'nome_cliente': dd['cliente']['razao'], # tab cliente
                'cpf_cnpj': dd['cliente']['cnpj_cpf'], # tab cliente
                'rg_ie': dd['cliente']['ie_identidade'], # tab cliente
                'tel_res': dd['cliente']['fone'], # tab cliente
                'tel_cel': dd['cliente']['whatsapp'], # tab cliente
                'email': dd['cliente']['email'], # tab cliente
                'n_contrato': dd['contrato']['id'], # tab contrato
                'endereco': dd['contrato']['endereco'], # tab contrato
                'bairro': dd['contrato']['bairro'], # tab contrato
                'cidade': dd['contrato']['cidade'], # tab contrato
                'estado': dd['cliente']['uf'], # tab contrato
                'cep': dd['contrato']['cep'], # tab contrato
                'plano': dd['contrato']['contrato'], # tab contrato
                'valor_taxa': dd['contrato']['valor_taxa'], # tab contrato
                'valor_taxa_instalacao': dd['contrato']['valor_taxa_instalacao'],
                'valor_taxa_comodato': dd['contrato']['valor_taxa_comodato'],
                'valor_mes': dd['contrato']['valor_plano'], # tab contrato/plano
                'desconto_taxa': dd['contrato']['desconto_fidelidade'], # tab contrato
                'desconto_fide': dd['contrato']['desconto_fide'], # tab contrato
                'taxa_final': dd['contrato']['taxa_instalacao'], # tab contrato
                'mensalidade_final': dd['contrato']['valor_plano'], # tab contrato
                'vencimento': dd['contrato']['dia_vencimento'], # tab contrato/ tipo cobrança
                'tx_download': dd['login']['tx_download'], # tab contrato/plano velocidade
                'tx_upload': dd['login']['tx_upload'], # tab contrato/plano velocidade
                'tipo_onu': 'ZTE', # tab comodato
                'modelo_onu': 'F670L', # tab comodato
                'quantidade_onu': '1', # tab comodato
                'data_extenso': datetime.now().strftime("Osasco, %d de %B de %Y"),
                'data': datetime.now().strftime("%d/%B/%Y")
                        }   
                    }
                }
        
        headers = {
            'accept': 'application/json',
            'content-type': 'application/json'
        }
        
        response = requests.post(url_sign, json=payload, headers=headers)

        pp(response.text)
        return response.json()
        # -------------------- Fim --------------------

    def list_templates(endpoint_token=endpoint_token,url_sign=url_sign):
        endpoint = f'/templates{endpoint_token}'
        url_sign = url_sign + endpoint
        headers = {'accept': 'application/json'}

        response = requests.post(url_sign, headers=headers)
        pp(response.json())
        return response.json()
        # -------------------- Fim --------------------

    def add_signer(uuid_doc,email,endpoint_token=endpoint_token,url_sign=url_sign):

        endpoint = f'/documents/{uuid_doc}/createlist{endpoint_token}'
        url_sign = url_sign + endpoint
        payload = {'signers' : [{
                    'email': email,
                    'act': '1',
                    'foreign': '0',
                    'certificadoicpbr': '0',
                    'assinatura_presencial': '0',
                    'docauth': '0',
                    'docauthandselfie': '1',
                    }]
                }
        headers = {
            'accept': 'application/json',
            'content-type': 'application/json'
        }
        
        response = requests.post(url_sign, json=payload, headers=headers)

        pp(response.text)
        return response.json()
        # -------------------- Fim -------------------- 

    def send_to_signer(uuid_doc,endpoint_token=endpoint_token,url_sign=url_sign):
        
        mensagem_para_o_signatário = 'Olá, segue contrato para assinatura.'
        
        endpoint = f'/documents/{uuid_doc}/sendtosigner' + endpoint_token
        url_sign = url_sign + endpoint
        payload = {
                "message": f"{mensagem_para_o_signatário}",
                "skip_email": "0",
                "workflow": "0",
            }
        headers = {
            'accept': 'application/json',
            'content-type': 'application/json'
        }
        
        response = requests.post(url_sign, json=payload, headers=headers)

        pp(response.text)
        return response.json()
        # -------------------- Fim -------------------- 

    def set_position_sign(uuid_doc,email,endpoint_token=endpoint_token,url_sign=url_sign):

        endpoint = f"/documents/{uuid_doc}/addpins{endpoint_token}"
        url_sign = url_sign + endpoint
        payload = { "pins": [
                {
                    "type": "0",
                    "document": uuid_doc,
                    "email": email,
                    "page": "2",
                    "page_height": "297",
                    "page_width": "210",
                    "position_x": "130",
                    "position_y": "950"
                }
            ] }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(url_sign, json=payload, headers=headers)

        pp(response.text)
        return response.json()
        # -------------------- Fim -------------------- 

    def get_url_doc(uuid_doc,url_sign=url_sign,endpoint_token=endpoint_token):


        endpoint = f"/documents/{uuid_doc}/download{endpoint_token}"
        url_sign = url_sign + endpoint
        payload = {
            "type": "pdf",
            
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(url_sign, json=payload, headers=headers)

        print(response.json())
        return response.json()
        # -------------------- Fim --------------------

    def webhook(uuid_doc, url_sign=url_sign, endpoint_token=endpoint_token, url_webhook=url_webhook ):
        # Insere comunicação webhook no documento 
        url_post = f'{url_sign}/documents/{uuid_doc}/webhooks{endpoint_token}'
        payload = { 'url': url_webhook,}
        headers = { "content-type": "application/json",}
        response = requests.post(url_post, json=payload, headers=headers)
        print(response.text)
        return response
    


if __name__ == "__main__":
    print('D4Sign_Main')
    print(datetime.today().strftime('%d/%m/%Y %H:%M:%S'))
    
    print(datetime.today().strftime('%d/%m/%Y %H:%M:%S'))

import pytest
import httpx
import json


def test_search_ncm_90112010_return_1_result():
    espected = {
        "NCM": "9011.20.10",
        "EX": None,
        "DESCRIÇÃO": "Para fotomicrografia",
        "ALÍQUOTA(%)": 3.25
    }
            
    espected = json.loads(espected.to_json(orient='records', force_ascii=False))
    espected = json.dumps(espected, indent=4)
    
    request = httpx.get('http://127.0.0.1:6500/api/ncm/9011.20.10')
    assert espected == request

def test_search_invalid_ncm():
    espected = []
    request = httpx.get('http://127.0.0.1:6500/api/ncm/0129')
    assert espected == request

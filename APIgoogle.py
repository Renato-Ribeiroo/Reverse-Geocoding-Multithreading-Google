import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# Defina a chave de API do Google Maps
API_KEY = 'CHAVE API GOOGLE'

# Função para obter informações de geocodificação inversa
def reverse_geocode(lat_long):
    latitude, longitude = lat_long
    url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        country = ''
        state = ''
        city = ''

        # Itere pelos resultados em busca das informações desejadas
        for result in data['results']:
            for comp in result['address_components']:
                types = comp.get('types', [])
                if 'country' in types:
                    country = comp['long_name']
                if 'administrative_area_level_1' in types:
                    state = comp['short_name']
                if 'locality' in types or 'administrative_area_level_2' in types:
                    city = comp['long_name']
        
        return country, state, city
    else:
        return '', '', ''

def process_location(input_filename, output_filename):
    # Ler o arquivo Excel com os dados
    df = pd.read_excel(input_filename)
    
    # Paralelizar a chamada à API usando ThreadPoolExecutor
    lat_long_list = df[['Latitude', 'Longitude']].values.tolist()
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(reverse_geocode, lat_long_list))
    
    # Adicionar os resultados ao DataFrame
    df[['País', 'Estado', 'Cidade']] = results
    
    # Salvar o DataFrame refinado em um novo arquivo Excel
    df.to_excel(output_filename, index=False)

# Função principal que chama o pipeline de funções
if __name__ == '__main__':
    
    print("Rodando API de Geolocalizacao Google")
    input_file = "Planilha com Lat e long.xlsx"
    output_file = "Planilha Processada.xlsx"
    process_location(input_file, output_file)

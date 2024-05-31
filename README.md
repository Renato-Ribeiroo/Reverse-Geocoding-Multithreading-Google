# Geocodificação Reversa com API do Google Maps

![Geocodificação Reversa](https://img.shields.io/badge/Geocodificação-Reversa-brightgreen)

Este projeto utiliza a API de Geocodificação do Google Maps para converter coordenadas geográficas (latitude e longitude) em endereços humanos legíveis, incluindo país, estado e cidade. O script lê uma planilha Excel com as coordenadas, realiza a geocodificação reversa e salva os resultados em uma nova planilha Excel.

## 🚀 Funcionalidades

- **Geocodificação Reversa:** Converte coordenadas (latitude e longitude) em endereços.
- **Paralelismo:** Utiliza `ThreadPoolExecutor` para chamadas assíncronas à API, aumentando a eficiência e performance em grandes solicitações.
- **Entrada e Saída em Excel:** Lê e escreve dados em arquivos Excel para facilidade de uso.

## 📦 Requisitos

- Python 3.x
- Bibliotecas: `requests`, `pandas`, `concurrent.futures`, `openpyxl`

## 🛠️ Configuração

1. Clone este repositório:
    ```bash
    git clone https://github.com/Renato-Ribeiroo/Reverse-Geocoding-Multithreading-Google
    ```
2. Instale as bibliotecas necessárias:
    ```bash
    pip install requests pandas openpyxl
    ```
3. Insira sua chave de API do Google Maps no script:
    ```python
    API_KEY = 'SUA_CHAVE_API_GOOGLE'
    ```
4. Prepare sua planilha Excel de entrada com as colunas "Latitude" e "Longitude".

## 📄 Uso

1. Coloque a planilha Excel de entrada no mesmo diretório do script.
2. Edite o nome do arquivo de entrada no script (se necessário):
    ```python
    input_file = "Planilha com Lat e long.xlsx"
    output_file = "Planilha Processada.xlsx"
    ```
3. Execute o script:
    ```bash
    python seu_script.py
    ```

## 🌟 Exemplos

### Planilha de Entrada

| Latitude | Longitude |
|----------|-----------|
| -23.5505 | -46.6333  |
| 40.7128  | -74.0060  |

### Planilha de Saída

| Latitude | Longitude | País        | Estado | Cidade     |
|----------|-----------|-------------|--------|------------|
| -23.5505 | -46.6333  | Brasil      | SP     | São Paulo  |
| 40.7128  | -74.0060  | Estados Unidos | NY   | Nova York  |

## 📝 Nota

- Certifique-se de que sua chave de API do Google Maps tenha permissões para geocodificação.
- O uso da API do Google Maps pode incorrer em custos, verifique a política de preços do Google.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📧 Contato

Para dúvidas, sugestões ou feedback, entre em contato:
- Email: renato_mry@hotmail.com
- GitHub: [Renato Ribeiro](https://github.com/Renato-Ribeiroo)

---

Divirta-se usando o projeto geocodificação reversa! 🌍🔄

---
# Reverse Geocoding with Google Maps API

![Reverse Geocoding](https://img.shields.io/badge/Reverse%20Geocoding-brightgreen)

This project uses the Google Maps Geocoding API to convert geographic coordinates (latitude and longitude) into human-readable addresses, including country, state, and city. The script reads an Excel spreadsheet with the coordinates, performs reverse geocoding, and saves the results in a new Excel spreadsheet.

## 🚀 Features

- **Reverse Geocoding:** Converts coordinates (latitude and longitude) into addresses.
- **Parallelism:** Uses `ThreadPoolExecutor` for asynchronous API calls, enhancing efficiency and performance for large requests.
- **Excel I/O:** Reads and writes data in Excel files for ease of use.

## 📦 Requirements

- Python 3.x
- Libraries: `requests`, `pandas`, `concurrent.futures`, `openpyxl`

## 🛠️ Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/Renato-Ribeiroo/Reverse-Geocoding-Multithreading-Google
    ```
2. Install the required libraries:
    ```bash
    pip install requests pandas openpyxl
    ```
3. Insert your Google Maps API key in the script:
    ```python
    API_KEY = 'YOUR_GOOGLE_API_KEY'
    ```
4. Prepare your input Excel spreadsheet with columns "Latitude" and "Longitude".

## 📄 Usage

1. Place the input Excel spreadsheet in the same directory as the script.
2. Edit the input file name in the script (if necessary):
    ```python
    input_file = "Spreadsheet with Lat and Long.xlsx"
    output_file = "Processed Spreadsheet.xlsx"
    ```
3. Run the script:
    ```bash
    python your_script.py
    ```

## 🌟 Examples

### Input Spreadsheet

| Latitude | Longitude |
|----------|-----------|
| -23.5505 | -46.6333  |
| 40.7128  | -74.0060  |

### Output Spreadsheet

| Latitude | Longitude | Country      | State | City       |
|----------|-----------|--------------|-------|------------|
| -23.5505 | -46.6333  | Brazil       | SP    | São Paulo  |
| 40.7128  | -74.0060  | United States| NY    | New York   |

## 📝 Note

- Ensure your Google Maps API key has geocoding permissions.
- Using the Google Maps API may incur costs, check the Google pricing policy.

## 🤝 Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📧 Contact

For questions, suggestions, or feedback, get in touch:
- Email: renato_mry@hotmail.com
- GitHub: [Renato Ribeiro](https://github.com/Renato-Ribeiroo)

---

Enjoy using the reverse geocoding project! 🌍🔄

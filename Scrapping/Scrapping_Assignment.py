
import requests
from bs4 import BeautifulSoup


headers = {
    "Referer": "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"
}


api_url = "https://qcpi.questcdn.com/cdn/browse_posting/"
project_url = "https://qcpi.questcdn.com/cdn/util/get_posting/?current_project_id={project_id}&next_project_id=&prev_project_id="

params = {
    "search_id": "",
    "postings_since_last_login": "",
    "draw": "1",
    "columns[0][data]": "render_my_posting",
    "columns[0][name]": "",
    "columns[0][searchable]": "false",
    "columns[0][orderable]": "false",
    "columns[0][search][value]": "",
    "columns[0][search][regex]": "false",
    "columns[1][data]": "render_post_date",
    "columns[1][name]": "",
    "columns[1][searchable]": "false",
    "columns[1][orderable]": "true",
    "columns[1][search][value]": "",
    "columns[1][search][regex]": "false",
    "columns[2][data]": "render_project_id",
    "columns[2][name]": "",
    "columns[2][searchable]": "true",
    "columns[2][orderable]": "true",
    "columns[2][search][value]": "",
    "columns[2][search][regex]": "false",
    "columns[3][data]": "render_category_search_string",
    "columns[3][name]": "",
    "columns[3][searchable]": "true",
    "columns[3][orderable]": "true",
    "columns[3][search][value]": "",
    "columns[3][search][regex]": "false",
    "columns[4][data]": "render_name",
    "columns[4][name]": "",
    "columns[4][searchable]": "true",
    "columns[4][orderable]": "true",
    "columns[4][search][value]": "",
    "columns[4][search][regex]": "false",
    "columns[5][data]": "bid_date_str",
    "columns[5][name]": "",
    "columns[5][searchable]": "true",
    "columns[5][orderable]": "true",
    "columns[5][search][value]": "",
    "columns[5][search][regex]": "false",
    "columns[6][data]": "render_city",
    "columns[6][name]": "",
    "columns[6][searchable]": "true",
    "columns[6][orderable]": "true",
    "columns[6][search][value]": "",
    "columns[6][search][regex]": "false",
    "columns[7][data]": "render_county",
    "columns[7][name]": "",
    "columns[7][searchable]": "true",
    "columns[7][orderable]": "true",
    "columns[7][search][value]": "",
    "columns[7][search][regex]": "false",
    "columns[8][data]": "state_code",
    "columns[8][name]": "",
    "columns[8][searchable]": "true",
    "columns[8][orderable]": "true",
    "columns[8][search][value]": "",
    "columns[8][search][regex]": "false",
    "columns[9][data]": "render_owner",
    "columns[9][name]": "",
    "columns[9][searchable]": "true",
    "columns[9][orderable]": "true",
    "columns[9][search][value]": "",
    "columns[9][search][regex]": "false",
    "columns[10][data]": "render_solicitor",
    "columns[10][name]": "",
    "columns[10][searchable]": "true",
    "columns[10][orderable]": "true",
    "columns[10][search][value]": "",
    "columns[10][search][regex]": "false",
    "columns[11][data]": "posting_type",
    "columns[11][name]": "",
    "columns[11][searchable]": "true",
    "columns[11][orderable]": "true",
    "columns[11][search][value]": "",
    "columns[11][search][regex]": "false",
    "columns[12][data]": "render_empty",
    "columns[12][name]": "",
    "columns[12][searchable]": "true",
    "columns[12][orderable]": "true",
    "columns[12][search][value]": "",
    "columns[12][search][regex]": "false",
    "columns[13][data]": "render_empty",
    "columns[13][name]": "",
    "columns[13][searchable]": "true",
    "columns[13][orderable]": "true",
    "columns[13][search][value]": "",
    "columns[13][search][regex]": "false",
    "columns[14][data]": "render_empty",
    "columns[14][name]": "",
    "columns[14][searchable]": "true",
    "columns[14][orderable]": "true",
    "columns[14][search][value]": "",
    "columns[14][search][regex]": "false",
    "columns[15][data]": "render_empty",
    "columns[15][name]": "",
    "columns[15][searchable]": "true",
    "columns[15][orderable]": "true",
    "columns[15][search][value]": "",
    "columns[15][search][regex]": "false",
    "columns[16][data]": "project_id",
    "columns[16][name]": "",
    "columns[16][searchable]": "true",
    "columns[16][orderable]": "true",
    "columns[16][search][value]": "",
    "columns[16][search][regex]": "false",
    "start": "0",
    "length": "25",
    "search[value]": "",
    "search[regex]": "false",
    "_": "1686072936017",
}

data = requests.get(api_url, params=params, headers=headers).json()

out = []
for i in data["data"]:
    project_id = i["project_id"]
    u = project_url.format(project_id=project_id)
    # print(f'Opening {u}...')
    soup = BeautifulSoup(requests.get(u, headers=headers).content, 'html.parser')
    # print some sample data from the page
    result = soup.find_all("div", {"class":"panel"})
    for res in result[0:5]:
        
        out.append(res.text)
for item in out:
    
    print(item)
    

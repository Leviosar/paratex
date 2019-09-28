from .scraper import get_sessions_on_month

if __name__ == '__main__':
    URL = 'http://transparencia.alesc.sc.gov.br/presenca_plenaria.php?periodo=09-2019'
    get_sessions_on_month(URL)

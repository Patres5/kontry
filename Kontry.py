import gspread
import keyword
import requests
import bs4
import lxml.html as lh


sa = gspread.service_account("lol.json")
sh = sa.open("Champions")


wks = sh.worksheet("Bohaterowie")
wks.update('Q23','Viego')


"""
leszek = wks.get('B4:B63')
chaos = wks.get('E4:E63')
lucek = wks.get('H4:H63')
kubmik = wks.get('K4:K63')
ja = wks.get('N4:N63')
comfort = 22
playable = 59

print(chaos[0:22])

playable_champ = chaos[0:22]
"""
"""
def program_name(champ_name):
   if champ_name == 'Wukong':
      return 'MonkeyKing'
   elif champ_name == 'Nunu & Willump':
      return "Nunu"
   elif champ_name == 'Renata Glasc':
      return "Renata"
   champ_name = champ_name.replace(" ", "")
   champ_name = champ_name.replace("'", "")
   champ_name = champ_name.replace(".", "")
   return champ_name


def counter(champ_name):
   res_player = requests.get(f'https://app.mobalytics.gg/pl_pl/lol/champions/{champ_name}/counters')
   soup_players = bs4.BeautifulSoup(res_player.text, 'lxml')
   table_players = soup_players.find_all('tr')
   main_stats = []
   for a in range(10,35):
      if a%3 == 1:
         chwila = []
         champion_info = table_players[a]
         all_stats = []
         for stat in champion_info:
            all_stats.append(stat.text)
         chwila.append(program_name(all_stats[2]))
         chwila.append(all_stats[4])
         main_stats.append(chwila)
   return main_stats



print(counter('viego'))






"""

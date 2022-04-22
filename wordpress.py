import requests

headers = {
  "Host": "public-api.wordpress.com",
  "content-length": "97",
  "sec-ch-ua-mobile": "?0",
  "user-agent": "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
  "sec-ch-ua-platform": "Android",
  "content-type": "application/json",
  "accept": "*/*",
  "origin": "https://public-api.wordpress.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://public-api.wordpress.com/wp-admin/rest-proxy/?v=2.0",
  "cookie": 'landingpage_currency=THB;_gcl_au=1.1.1573301268.1644291494;_fbp=fb.1.1644291494384.460823662;G_ENABLED_IDPS=google;_hjSessionUser_227769=eyJpZCI6IjA3NGEzZGQzLWNjZDUtNThiZC04NzRlLThlYmIxMmZkNGVhZSIsImNyZWF0ZWQiOjE2NDQyOTE0OTQ2MDEsImV4aXN0aW5nIjp0cnVlfQ==;_pin_unauth=dWlkPVlqZG1aakE0Tm1FdE0yUmxOeTAwTkRnd0xXRXdZV1F0Tm1Nek56VmlabVV6WTJOaA;recognized_logins=kVKyEuggwsZGlpnm3M1_9gOne4HICWvL530yLUsUClFtOFmgEaSxewwRgI7KvaTMc6HJGl-10EJY1GbGid_Sig%3D%3D;_wpndash=17dd1c12c0b2d92388e9f51b;_pubcid=2f79556b-edc8-48e4-8128-659ae95f3743;_cc_id=2455674b354c4849d1e3c3280bec9653;__utma=11735858.1101824902.1644291493.1648030290.1648951200.9;__utmz=11735858.1648951200.9.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);tk_ai=1NowKjbHtN76w9g4Cj2hFqbD;explat_test_aa_weekly_lohp_2022_week_16=control;dcmsid=lCORgcVM1M4RaE5jm3vHcDNv43r4ohLj;_gid=GA1.2.1065752017.1650638606;country_code=TH;ccpa_applies=false;usprivacy=1---;_uetsid=91451ba0c24a11ec9c903f265f1c111f;_uetvid=8b684b40889011ecb9af99a3c6a1ec8a;_gat=1;_ga=GA1.1.1101824902.1644291493;_hjSession_227769=eyJpZCI6IjY3ZmU1MjcwLTJlYjAtNGIyNS04NWIyLWYwOGYxMWFkYWI3OSIsImNyZWF0ZWQiOjE2NTA2Mzg2MDcyNjAsImluU2FtcGxlIjp0cnVlfQ==;_hjAbsoluteSessionInProgress=0;smart-pixel-session={"hash_parameters":{},"id":"3adb904c-41d7-4050-b982-936d9b89e496","last_action_ts":1650638608,"parameters":{},"start_ts":1650638608,"timers":{},"viewed_pages":1};_clck=1r3wqec|1|f0u|0;_clsk=2pd8ii|1650638609593|1|0|a.clarity.ms/collect;wordpress_test_cookie=WP%20Cookie%20check;_ga_1H4VG5F5JF=GS1.1.1650638606.1.0.1650638610.0;tk_qs='
}

json = {
  "email": "ohmdevpro@gmail.com",
  "password": "^SVVyeDE2huzdmk",
  "username": "ohmdevpro",
  "locale": "th"
}

wordpress = requests.post("https://public-api.wordpress.com/rest/v1.1/signups/validation/user?http_envelope=1&locale=th",json=json, headers=headers)
print(wordpress.text)